import datetime
import sqlite3


def request_log(endpoint_name, call_params, result):
    with sqlite3.connect("C:/Users/ConstantinIonescu/Desktop/flask_project/database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO requests (endpoint_name, call_params, result, timestamp)\
        VALUES(?, ?, ?, ?)", (endpoint_name, call_params, result, datetime.datetime.now()))
        con.commit()
        msg = "Record successfully added"
