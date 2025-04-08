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

if (not os.path.isfile("stock.db")):
    db.setup() # sets up databases

@app.route("/", methods=['GET', 'POST'])
def home():
    sp500Stocks = pd.read_csv('csv/all_stocks_5yr.csv')

    stockNames = sp500Stocks['Name'].unique()

    passValue = 'username' in session
    if 'username' in session:
        return render_template("home.html", logged_in = passValue, username=session['username'], stockNames = stockNames)
    return render_template("home.html", logged_in = passValue)

@app.route("/view_stock", methods=['GET','POST'])
def view():
    stockName = request.form['stock']
    sp500Stocks = pd.read_csv('csv/all_stocks_5yr.csv')

    stockDates = sp500Stocks[sp500Stocks['Name'] == stockName]['date'].tolist()
    stockHigh = sp500Stocks[sp500Stocks['Name'] == stockName]['high'].tolist()

    return render_template("home.html", logged_in = 'username' in session, username = session['username'], stockDates = stockDates, stockHigh = stockHigh)

@app.route("/portfolio", methods=['GET', 'POST'])
def analysis():
    passValue = 'username' in session
    return render_template("portfolio.html", logged_in = passValue)

@app.route("/battle", methods=['GET', 'POST'])
def battle():
    passValue = 'username' in session
    return render_template("battle.html", logged_in = passValue)

@app.route("/stock_list", methods=['GET', 'POST'])
def list():
    passValue = 'username' in session
    index = pd.read_csv('csv/sp500_index.csv')
    companies = pd.read_csv('csv/sp500_companies.csv')

    dates = index['Date'].tolist()
    sp = index['S&P500'].tolist()
    # # Exchange,Symbol,Shortname,Longname,Sector,Industry,Currentprice,Marketcap,Ebitda,Revenuegrowth,City,State,Country,
    # print(companies['Shortname'])
    # print(companies.nlargest(10, 'Currentprice'))

    sp500Stocks = pd.read_csv('csv/all_stocks_5yr.csv')
    stockNames = sp500Stocks['Name'].unique()

    return render_template("stock_list.html", data1=dates, data2=sp, logged_in = passValue, stockNames = stockNames)

@app.route('/register', methods=['GET','POST'])
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
        elif db.getUserID(username) >= 0:
            flash("Username already exists", 'error')
            return redirect("/")
        else:
            session['username'] = username
            flash("Registered Sucessfully!", "success")
            db.addUser(username, password)
            return redirect("/")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if not request.form:
        flash("You must use the menu to log in", 'error')
        return redirect("/")
    else:
        username = request.form['username']
        password = request.form['password']
        if db.getUserID(username) >= 0 and db.getTableData("users", "username", username)[2] == password:
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
