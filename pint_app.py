
# 22nd March - starting skeleton for project from lab 5
# Will do pints prices of pubs in maynooth

from flask import Flask, url_for, request, redirect, abort , jsonify
from pint_dao import pintDAO
from flask import send_from_directory

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return send_from_directory('staticpages', 'index.html')

@app.route('/pints', methods=['GET'])
def getall():
    results = pintDAO.getAll()
    return jsonify(results)
    #return "get all pints"

@app.route('/pints/<int:id>', methods=['GET'])
def findbyid(id):
    result = pintDAO.findByID(id)
    return jsonify(result)
    #return f"find by id {id}"


@app.route('/pints', methods=['POST'])
def create():
    pint = request.json
    created = pintDAO.create(pint)
    return jsonify(created)
    
    #jsonstring = request.json
    #return f"create {jsonstring}"

@app.route('/pints/<int:id>', methods=['PUT'])
def update(id):
    pint = request.json
    updated = pintDAO.update(id, pint)
    return jsonify(updated)
    #jsonstring = request.json
    #return f"update {id} {jsonstring}"

@app.route('/pints/<int:id>', methods=['DELETE'])
def delete(id):
    pintDAO.delete(id)
    return jsonify({"done": True})
    #return f"delete {id}"

if __name__ == '__main__':
    app.run(debug=True) 
