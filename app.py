from flask import Flask
import sqlite3
import pandas as pd


app = Flask(__name__)
    

@app.route('/')
def hello_world():
  return 'Hello world'