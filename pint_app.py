
# 22nd March - starting skeleton for project from lab 5
# Will do pints prices of pubs in maynooth

from flask import Flask, url_for, request, redirect, abort

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "Hello, Pints!"

@app.route('/pints', methods=['GET'])
def getall():
    return "get all pints"

@app.route('/pints/<int:id>', methods=['GET'])
def findbyid(id):
    return f"find by id {id}"


@app.route('/pints', methods=['POST'])
def create():
    jsonstring = request.json
    return f"create {jsonstring}"

@app.route('/pints/<int:id>', methods=['PUT'])
def update(id):
    jsonstring = request.json
    return f"update {id} {jsonstring}"

@app.route('/pints/<int:id>', methods=['DELETE'])
def delete(id):
    return f"delete {id}"

if __name__ == '__main__':
    app.run(debug=True) 
