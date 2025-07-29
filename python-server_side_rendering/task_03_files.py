from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def read_products_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                item['id'] = int(item['id'])
            return data
    except Exception:
        return None

def read_products_csv(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = []
            for row in reader:
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                except Exception:
                    pass
                data.append(row)
            return data
    except Exception:
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    data = []

    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, 'products.json')
    csv_path = os.path.join(base_dir, 'products.csv')

    if source == 'json':
        products = read_products_json(json_path)
    elif source == 'csv':
        products = read_products_csv(csv_path)
    else:
        products = None
        error = "Wrong source"

    if products is None:
        if not error:
            error = "Could not read data file."
        return render_template('product_display.html', products=[], error=error)

    if product_id:
        try:
            product_id_int = int(product_id)
        except Exception:
            return render_template('product_display.html', products=[], error="Invalid product id")
        filtered = [p for p in products if int(p.get('id', 0)) == product_id_int]
        if not filtered:
            return render_template('product_display.html', products=[], error="Product not found")
        data = filtered
    else:
        data = products

    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
