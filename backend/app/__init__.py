import os
from bson import json_util
from flask import Flask
from flask_cors import CORS
from .routes import routes
from .utils import MongoSingleton

app = Flask(__name__)

CORS(app, supports_credentials=True)

app.register_blueprint(routes, url_prefix='/api')

news_col = MongoSingleton.get_collection("news")
tags_col = MongoSingleton.get_collection("tags")


data_folder = os.path.join(os.path.dirname(__file__), 'data')
if os.path.exists(data_folder):
    for file in os.listdir(data_folder):
        if file.endswith(".json"):
            with open(os.path.join(data_folder, file), "r") as f:
                data = json_util.loads(f.read())
            for entry in data:
                for tag in entry["tags"]:
                    id = news_col.insert_one({"title": entry["title"], "description": entry["description"], "link": entry["link"], "pubDate": entry["pubDate"]}).inserted_id
                    tags_col.insert_one({"tag": tag, "news_id": id})