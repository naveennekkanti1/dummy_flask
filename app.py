
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from pymongo import MongoClient
import os

app = Flask(__name__)

# Connect to MongoDB using MongoDB Compass URI (replace with your URI)
client = MongoClient("mongodb://localhost:27017/")
db = client['dummy_flask']
collection = db['users']

@app.route('/')
def index():
    # Fetch data from MongoDB
    data = collection.find()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        # Insert data into MongoDB
        collection.insert_one({'name': name})
        return redirect(url_for('index'))

@app.route('/download')
def download():
    return send_from_directory(os.getcwd(), 'flask_mongo_app.zip', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
