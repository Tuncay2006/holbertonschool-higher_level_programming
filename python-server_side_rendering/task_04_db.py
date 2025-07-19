# task_04_db.py
from flask import Flask, render_template, request
import csv
import json
import sqlite3

app = Flask(__name__)

def get_products_from_csv(filename='products.csv'):
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    except Exception as e:
        return f"CSV error: {str(e)}"

def get_products_from_json(filename='products.json'):
    try:
        with open(filename) as jsonfile:
            return json.load(jsonfile)
    except Exception as e:
        return f"JSON error: {str(e)}"

def get_products_from_sqlite(db='products.db'):
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute("SELECT name, price, category FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [{"name": name, "price": price, "category": category} for name, price, category in rows]
    except Exception as e:
        return f"SQL error: {str(e)}"

@app.route('/')
def index():
    source = request.args.get('source', 'json')
    if source == 'json':
        data = get_products_from_json()
    elif source == 'csv':
        data = get_products_from_csv()
    elif source == 'sql':
        data = get_products_from_sqlite()
    else:
        return render_template('product_display.html', error="Wrong source", products=[])

    # Hata mesajı döndüyse string olur
    if isinstance(data, str):
        return render_template('product_display.html', error=data, products=[])
    
    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True)
