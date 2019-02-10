import flask
from flask import request, jsonify
from flask_cors import CORS
import sqlite3

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=["GET"])
def query():
    conn = sqlite3.connect('limebike.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    bikes = c.execute('''
        SELECT * FROM bikes''').fetchall()
    scooters = c.execute('''
        SELECT * FROM Scooters''').fetchall()
    res = {"Bikes": bikes, "Scooters": scooters}
    return jsonify(res)


app.run()