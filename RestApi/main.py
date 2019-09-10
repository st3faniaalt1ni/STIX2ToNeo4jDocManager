from app import app, mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request

# Push documents through route /add
# For example
# http://localhost/malicious_URL/add..
@app.route('/add', methods=['POST'])
# Create a method to push documents into mongo through our api
def add_document():
	_json = request.json
	_type = _json['type']
	# validate the received values
	if _type and request.method == 'POST':
		# save details
		id = mongo.db.threats.insert(_json)
	    # id = mongo.db.collection_name.insert(_json)

		resp = jsonify('STIX Object Document added successfully!')
		resp.status_code = 200
		return resp
	else:
		return not_found()

# function of API to return all inserted documents
@app.route('/documents')
def documents():
	documents = mongo.db.threats.find()
	#documents = mongo.db.collection_name.find()
	resp = dumps(documents)
	return resp

# function of API to find a document with a specific ID
@app.route('/object/<id>')
def object(id):
	document = mongo.db.threats.find_one({'_id': ObjectId(id)})
	#document = mongo.db.collection_name.find_one({'_id': ObjectId(id)})
	resp = dumps(document)
	return resp

@app.route('/update/<id>', methods=['PUT', 'PATCH'])
def update_document(id):
	_json = request.json
	# if '$oid' in _json['_id']:
	# 	id = _json['_id']
	# 	_id = ObjectId(id['$oid'])
	# else:
	# 	_id = ObjectId(_json['_id'])
	_id = ObjectId(id)
	# _id = ObjectId(_json['_id'])
	# _id = ObjectId('5d73abea93f48a8399d3ade6')
	# _description = _json["description"]
	# validate the received values
	if request.method == 'PUT' or request.method == 'PATCH':
		# save edits
		mongo.db.threats.find_one_and_update({'_id': _id},
									 { '$set':
									 { 'type': _json["type"] if "type" in _json else "No type",
									   'id': _json["type"] if "id" in _json else "No id",
								       'created': _json["created"] if "created" in _json else "No creation date",
									   'modified': _json["type"] if "modified" in _json else "No modifications",
									   'object_marking_refs': _json["object_marking_refs"] if "id" in _json else "No marking definitions",
									   'name': _json["name"] if "name" in _json else "No name",
									   'description': _json["description"] if "description" in _json else "No description",
									   'first_seen': _json["first_seen"] if "first_seen" in _json else "No first seen date",
									   'resource_level': _json["resource_level"] if "resource_level" in _json else "No resource level",
									   'primary_motivation': _json["primary_motivation"] if "primary_motivation" in _json else "primary_motivation",
									   'aliases': _json["aliases"] if "aliases" in _json else "aliases",
                                       'sophistication': _json["sophistication"] if "sophistication" in _json else "sophistication",
                                       'pattern': _json["pattern"] if "pattern" in _json else "pattern",
									   'roles': _json["roles"] if "roles" in _json else "roles"}
                                        })
		resp = jsonify('Document object  updated successfully!')
		resp.status_code = 200
		return resp
	else:
		# debugstr = 'method is ' + request.method + ' id is of type' + type(_id) + ' id is ' + _json['id']
		debugstr = "something else"
		message = {
			'status': 404,
			'message': debugstr,
		}
		resp = jsonify(message)
		resp.status_code = 404
		return resp
		
@app.route('/delete/<id>', methods=['DELETE'])
def delete_documents(id):
	mongo.db.threats.delete_one({'_id': ObjectId(id)})
	#mongo.db.collection_name.delete_one({'_id': ObjectId(id)})
	resp = jsonify('User deleted successfully!')
	resp.status_code = 200
	return resp
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run()