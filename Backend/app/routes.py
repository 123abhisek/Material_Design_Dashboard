from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from app.models import notes_collection

main = Blueprint('main', __name__)

@main.route('/dashboard', methods=['GET'])
def dashboard():
    notes = list(notes_collection.find())
    for note in notes:
        note['_id'] = str(note['_id'])
    return jsonify(notes)

@main.route('/', methods=['GET'])
def home():
    return 'Sucessfully Connected'

@main.errorhandler(404)
def page_not_found(e):
    return 'No Route Found !!!',404
