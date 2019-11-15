from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from api import mongo, app


@app.route('/dreams', methods=['GET'])
def get_all_dreams():
    print("here")
    dreams = mongo.db.dreams
    output = []
    for dream in dreams.find():
        output.append({'title' : dream['title'], 'date': dream['date'], 'content': dream['content']})
    return jsonify({'result' : output})

@app.route('/dream/<title>', methods=['GET'])
def get_one_dream(title):
    dreams = mongo.db.dreams
    dream_cursor = dreams.find({'title' : title})
    dream = dream_cursor.__getitem__(0)
    if dream:
        output = {'title' : dream['title'], 'date' : dream['date'], 'content': dream['content']}
    else:
        output = "No such name"
    return jsonify({'result' : output})

@app.route('/dream', methods=['POST'])
def add_dream():
    dream = mongo.db.dreams
    title = request.json['title']
    date = request.json['date']
    content = request.json['content']
    dream_id = dream.insert({'title': title, 'date': date, 'content': content})
    new_dream = dream.find_one({'_id': dream_id })
    output = {'name' : new_dream['title'], 'date' : new_dream['date'], 'content': new_dream['content']}
    return jsonify({'result' : output})

@app.route('/update_dream/<title>', methods=['GET', 'PUT'])
def update_dream(title, data):
    dreams = mongo.db.dreams
    dreams.update_one({'title': title, 'date': data['date'], 'content': data['content']})

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : 'Hello, World!'})


if __name__ == '__main__':
    app.run(debug=True)