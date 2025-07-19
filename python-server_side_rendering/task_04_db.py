from flask import Flask, render_template_string, request
import json
import csv
import sqlite3

app = Flask(__name__)

TEMPLATE_HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Product List</title>
</head>
<body>
    <h1>Product List</h1>
    {% if error %}
        <p style="color:red;">{{ error }}</p>
    {% else %}
        <ul>
        {% for product in products %}
            <li>{{ product['name'] }} - ${{ product['price'] }} ({{ product['category'] }})</li>
        {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
'''

def get_products_from_json():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception as e:
        return f"JSON error: {e}"

def get_products_from_csv():
    try:
        with open('products.csv', newline='') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except Exception as e:
        return f"CSV error: {e}"

def get_products_from_sqlite():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name, price, category FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [{"name": name, "price": price, "category": category} for name, price, category in rows]
    except Exception as e:
        return f"SQL error: {e}"

@app.route('/products')
def products():
    source = request.args.get('source', 'json')

    if source == 'json':
        data = get_products_from_json()
    elif source == 'csv':
        data = get_products_from_csv()
    elif source == 'sql':
        data = get_products_from_sqlite()
    else:
        return render_template_string(TEMPLATE_HTML, error="Wrong source", products=[])

    if isinstance(data, str):
        return render_template_string(TEMPLATE_HTML, error=data, products=[])

    return render_template_string(TEMPLATE_HTML, products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True)
