# JEWZ
# SoftDev
# P04:
# 2025-04-XX
# Time Spent: not enough hours

import random
import datetime
import os
import sqlite3
import sys
from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify
import json
import pandas as pd
import db

DB_FILE = "db.py"
app = Flask(__name__)
app.secret_key = os.urandom(32)
anchor = False

sp500Stocks = pd.read_csv('csv/all_stocks_5yr.csv')
index = pd.read_csv('csv/sp500_index.csv')
companyData = pd.read_csv('csv/sp500_companies.csv')
uniqueStocks = sp500Stocks['Name'].unique()
indexDates = index['Date'].tolist()
indexSP = index['S&P500'].tolist()

if (not os.path.isfile("stock.db")):
    db.setup()

@app.route("/", methods=['GET', 'POST'])
def home():
    loggedIn = 'username' in session
    if loggedIn:
        return render_template("home.html", logged_in=loggedIn, username=session['username'], stockNames=uniqueStocks)
    return render_template("home.html", logged_in=loggedIn)

@app.route("/stock_register", methods=['GET', 'POST'])
def stock_register():
    loggedIn = 'username' in session
    if loggedIn:
        db.addStock(session['username'], request.form.get('stock'))
        return redirect("/portfolio")
    else:
        return redirect("/")

@app.route("/update_CompData", methods=['GET', 'POST'])
def update():
    loggedIn = 'username' in session
    if loggedIn:

        return redirect("/portfolio")
    else:
        return redirect("/")

@app.route("/portfolio", methods=['GET', 'POST'])
def analysis():
    loggedIn = 'username' in session
    triggerView = False

    if loggedIn:
        if request.form.get('trigger') == "True":
            triggerView = True
        else:
            triggerView = False

        stock = request.form.get('stock')
        stockDates = sp500Stocks[sp500Stocks['Name'] == stock]['date'].tolist()
        stockHigh = sp500Stocks[sp500Stocks['Name'] == stock]['high'].tolist()

        portfolio = []
        numbers = []
        companies = []
        sectors = []
        industries = []
        currentPrice = []
        marketCap = []
        editSwap = []
        port = db.getAllTableData("portfolio", "username", session['username'])
        try:
            for item in port:
                portfolio.append(item[2])
        except:
            portfolio = ["None"]
        for count, item in enumerate(portfolio):
            numbers.append(count+1)
            data = companyData[companyData['Symbol'] == item]
            try:
                companies.append(data['Longname'].to_string().split("    ", 1)[1])
                sectors.append(data['Sector'].to_string().split("    ", 1)[1])
                industries.append(data['Industry'].to_string().split("    ", 1)[1])
                currentPrice.append(data['Currentprice'].to_string().split("    ", 1)[1])
                marketCap.append(data['Marketcap'].to_string().split("    ", 1)[1])
                editSwap.append(False)
            except:
                companies.append("None")
                sectors.append("None")
                industries.append("None")
                currentPrice.append("None")
                marketCap.append("None")
                editSwap.append(True)
            dataToPass = []
            for count, item in enumerate(numbers):
                dataToPass.append([item, portfolio[count], companies[count], sectors[count], industries[count], currentPrice[count], marketCap[count], editSwap[count]])
        return render_template("portfolio.html", logged_in=loggedIn, user=session['username']+'\'s', dataToPass=dataToPass, stockDates=stockDates, stockHigh=stockHigh, stock=stock, view=triggerView)
    else:
        return render_template("portfolio.html", logged_in=loggedIn, stockDates=[], stockHigh = [], stock="", view = triggerView)

@app.route("/battle", methods=['GET', 'POST'])
def battle():
    loggedIn = 'username' in session
    return render_template("battle.html", logged_in=loggedIn)

@app.route("/stock_list", methods=['GET', 'POST'])
def list():

    triggerView = False
    if request.form.get('trigger') == "True":
        triggerView = True
    else:
        triggerView = False

    loggedIn = 'username' in session

    stockName = request.form.get('stock')
    stockDates = sp500Stocks[sp500Stocks['Name'] == stockName]['date'].tolist()
    stockHighs = sp500Stocks[sp500Stocks['Name'] == stockName]['high'].tolist()

    return render_template(
        "stock_list.html",
        logged_in=loggedIn,
        stockNames=uniqueStocks,
        stock = stockName,
        stockDates=stockDates,
        stockHigh=stockHighs,
        view = triggerView
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    if not request.form:
        flash("You must use the menu to register", 'error')
        return redirect("/")
    else:
        username = request.form['username']
        password = request.form['password']
        password2 = request.form.get('password2')
        if password != password2:
            flash("Passwords do not match", 'error')
            return redirect("/")
        elif db.checkUser(username) >= 0:
            flash("Username already exists", 'error')
            return redirect("/")
        else:
            session['username'] = username
            flash("Registered Successfully!", "success")
            db.addUser(username, password)
            return redirect("/")

@app.route('/explore', methods=['GET', 'POST'])
def explore():
    publicUsers = []
    for item in db.getAllTableData("users", "Privacy", "Public"):
        publicUsers.append(item[1])
    print(publicUsers)

    return render_template("explore.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if not request.form:
        flash("You must use the menu to log in", 'error')
        return redirect("/")
    else:
        username = request.form['username']
        password = request.form['password']
        if db.checkUser(username) >= 0 and db.getTableData("users", "username", username)[2] == password:
            session['username'] = username
            db.updateLoginTime(session['username'])
            flash("Logged in", 'success')
        else:
            flash("Incorrect username or password.", 'error')
        return redirect("/")

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    if 'username' in session:
        flash("Logged out", 'success')
        session.pop('username', None)
    return redirect("/")
