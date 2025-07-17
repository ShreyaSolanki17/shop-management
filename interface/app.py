
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect, url_for, flash
from store.sweet_store import SweetStore
from store.sweet_item import SweetItem

app = Flask(__name__)
app.secret_key = 'sweetsecret'  # Required for flashing messages

store = SweetStore()

@app.route('/', methods=['GET'])
def index():
    sort_by = request.args.get('sort_by', 'price')
    try:
        sweets = store.sort_sweets(sort_by)
    except:
        sweets = store.list_items()
    return render_template('index.html', sweets=sweets)

@app.route('/add', methods=['POST'])
def add_sweet():
    try:
        id = int(request.form['id'])
        name = request.form['name']
        category = request.form['category']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])

        sweet = SweetItem(id, name, category, price, quantity)
        store.add_sweet(sweet)
        flash("Sweet added successfully!", "success")
    except Exception as e:
        flash(f"Error adding sweet: {e}", "danger")
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['GET'])
def delete_sweet(id):
    try:
        store.delete_sweet(id)
        flash("Sweet deleted successfully!", "info")
    except Exception as e:
        flash(f"Error deleting sweet: {e}", "danger")
    return redirect(url_for('index'))

@app.route('/purchase', methods=['POST'])
def purchase_sweet():
    try:
        id = int(request.form['id'])
        quantity = int(request.form['quantity'])
        store.purchase_sweet(id, quantity)
        flash("Purchase successful!", "success")
    except Exception as e:
        flash(f"Purchase failed: {e}", "danger")
    return redirect(url_for('index'))

@app.route('/restock', methods=['POST'])
def restock_sweet():
    try:
        id = int(request.form['id'])
        quantity = int(request.form['quantity'])
        store.restock_sweet(id, quantity)
        flash("Restock successful!", "success")
    except Exception as e:
        flash(f"Restock failed: {e}", "danger")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
