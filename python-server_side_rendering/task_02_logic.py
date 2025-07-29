from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    items_list = []
    items_path = os.path.join(os.path.dirname(__file__), 'items.json')
    try:
        with open(items_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except Exception as e:
        items_list = []
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
