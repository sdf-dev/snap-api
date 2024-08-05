from flask import Flask, jsonify
import csv

app = Flask(__name__)

@app.route("/")
def landing_function():
    return "<p>Marvel Snap Collection.</p>"

@app.route("/collection")
def collection():
    snap_file = "collection.csv"
    card_list = []

    with open(snap_file, "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            first_two_columns = row[:2]
            card_list.append(first_two_columns)
            print(row[:2])
           
            
    print(card_list)
    
    return jsonify(card_list)

