
# 22nd March - starting skeleton for project from lab 5

from flask import Flask, url_for, request, redirect, abort

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/books', methods=['GET'])
def getall():
    return "get all"

@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
    return f"find by id {id}"

@app.route('/books/<int:id>', methods=['POST'])
def create(id):
    jsonstring = request.json
    return f"create {id} {jsonstring}"

@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    jsonstring = request.json
    return f"update {id} {jsonstring}"

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    return f"delete {id}"

if __name__ == '__main__':
    app.run(debug=True) 
