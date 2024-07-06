from pymongo import MongoClient
from flask import Blueprint, request, jsonify

client = MongoClient('mongodb://localhost:27017')
db = client.Material_Design_Dashbaord
notes_collection = db.user_data