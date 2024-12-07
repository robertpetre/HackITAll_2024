from flask import jsonify, request, Blueprint
from pymongo import *

MONGO_URL = 'mongodb://db:27017/'
DB_NAME = 'hackitall'
NEWS_COL = 'news'   

client = MongoClient(MONGO_URL)
db = client[DB_NAME]
news = db[NEWS_COL]


routes = Blueprint('app', __name__)

@routes.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello, World!'})

@routes.route('/health', methods=['GET'])
def health():
    try:
        client.admin.command('ping')  
    except Exception as e:
        return jsonify({'message': 'Error: ' + str(e)}), 500
    return jsonify({'message': 'OK'})   
