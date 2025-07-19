from flask import Flask, render_template_string, request
import json
import csv

app = Flask(__name__)

# JSON ve CSV verilerini okuyup dönen fonksiyonlar
def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception:
        return None

def read_csv():
    try:
        products = []
        with open('products.csv', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['price'] = float(row['price'])
                row['id'] = int(row['id'])
                products.append(row)
        return products
    except Exception:
        return None

# HTML şablon (template) - dosya yerine string olarak direkt burada
TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <title>Products</title>
</head>
<body>
    <h1>Product List</h1>

    {% if error %}
        <p style="color:red;">{{ error }}</p>
    {% else %}
        <table border="1" cellpadding="5">
            <thead>
                <tr>
                    <th>Name</th><th>Category</th><th>Price</th>
                </tr>
            </thead>
            <tbody>
                {% for product in products %}
                <tr>
                    <td>{{ product.name }}</td>
                    <td>{{ product.category }}</td>
                    <td>{{ product.price }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    {% endif %}
</body>
</html>
"""

@app.route('/products')
def products():
    source = request.args.get('source')
    id_str = request.args.get('id')
    product_id = None
    if id_str:
        try:
            product_id = int(id_str)
        except ValueError:
            return render_template_string(TEMPLATE, error="Invalid id parameter")

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        return render_template_string(TEMPLATE, error="Wrong source")

    if data is None:
        return render_template_string(TEMPLATE, error="Error reading data")

    if product_id is not None:
        filtered = [p for p in data if p.get('id') == product_id]
        if not filtered:
            return render_template_string(TEMPLATE, error="Product not found")
        data = filtered

    return render_template_string(TEMPLATE, products=data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
