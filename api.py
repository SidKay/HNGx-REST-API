from flask import Flask as Flask
from flask import request, jsonify
# 10/10 code right here :)
import os
import db
from models import Person

app = Flask(__name__)

if not os.path.isfile('people.db'):
	db.connect()

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/api', methods=['POST'])
def createPersonData():
	new_person = request.get_json()
	name = new_person['name']
	track = new_person['track']
	age = new_person['age']
	if db.check(name):
		return jsonify({'error': f'Person {name} already exists.'}), 400
	pe = Person(name, track, age)
	db.insert(pe)
	return jsonify({'message': f'Person {name} added successfully.'}), 200

@app.route('/api/<int:personid>', methods=['GET'])
def readPersonData(personid):
	person = request.view_args
	if not db.view(person['personid']):
		return jsonify({'error': f'User {name} not found.'}), 404
	persondata = Person(*db.view(person['personid']))
	return jsonify(persondata.serialize()), 200

@app.route('/api/<int:personid>', methods=['PUT'])
def editPersonData(personid):
	person = request.get_json()
	misc = request.view_args
	name = person['name']
	track = person['track']
	age = person['age']
	id = misc['personid']
	try:
		db.update(name, track, age, id)
		return jsonify({'message': f'Person has been updated successfully.'}), 200
	except Exception as e:
		return jsonify({'error': 'Failed to update person.'}), 400

@app.route('/api/<int:personid>', methods=['DELETE'])
def deletePersonData(personid):
	req_args = request.view_args
	if db.view(req_args['personid']):
		db.delete(req_args['personid'])
		return jsonify({'message': 'Person deleted successfully.'}), 200
	return jsonify({'error': 'Unable to delete Person'}), 400

if __name__ == '__main__':
	app.run(debug=True)
  