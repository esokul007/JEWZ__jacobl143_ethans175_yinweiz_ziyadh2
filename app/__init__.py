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

DB_FILE = "db.py"
app = Flask(__name__)
app.secret_key = os.urandom(32)
anchor = False

@app.route("/", methods=['GET', 'POST'])
def home():
    stocks = pd.read_csv('csv/sp500_stocks.csv')
    index = pd.read_csv('csv/sp500_index.csv')
    companies = pd.read_csv('csv/sp500_companies.csv')

    dates = index['Date'].tolist()
    sp = index['S&P500'].tolist()

    return render_template("home.html", data1=dates, data2=sp)

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
            active_sessions[session['username']] = db.getUserID(session['username'])
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
        if username in active_sessions:
            flash("You already have an active session.", 'error')
        elif db.getUserID(username) >= 0 and db.getTableData("users", "username", username)[2] == password:
            session['username'] = username
            active_sessions[session['username']] = db.getUserID(session['username'])
            db.updateLoginTime(session['username'])
            flash("Logged in", 'success')
        else:
            flash("Incorrect username or password.", 'error')
        return redirect("/")

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    if 'username' in session:
        flash("Logged out", 'success')
        active_sessions.pop(session['username'])
        session.pop('username', None)
    return redirect("/")
