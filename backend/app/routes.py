from flask import jsonify, request, Blueprint
from pymongo import *
from collections import defaultdict
from .utils import MongoSingleton

news_col = MongoSingleton.get_collection("news")
tags_col = MongoSingleton.get_collection("tags")


routes = Blueprint('app', __name__)

@routes.route('/', methods=['GET'])
def index():
    tags_list = []
    tags_mean_map = defaultdict(list)
    tags_title_map = defaultdict(list)
    for tags in tags_col.find():
        print(tags)
        entry =  {}
        entry["tag"] = tags["tag"]
        news = news_col.find_one({"_id": tags["news_id"]})
        tags_mean_map[entry["tag"]].append(news["sentimentalScore"])
        tags_title_map[entry["tag"]].append((news["title"], news["isGoodNews"], news["link"], news["summary"]))
    for tag in tags_mean_map:
        entry = {}
        entry["tag"] = tag
        entry["mean"] = round(sum(tags_mean_map[tag]) / len(tags_mean_map[tag]), 1)
        entry["news"] = tags_title_map[tag]
        tags_list.append(entry)
    return jsonify(tags_list)

@routes.route('/health', methods=['GET'])
def health():
    try:
        client = MongoSingleton.get_client("news")
        client.server_info()  
    except Exception as e:
        return jsonify({'message': 'Error: ' + str(e)}), 500
    return jsonify({'message': 'OK'})   
