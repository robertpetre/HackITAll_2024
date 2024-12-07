from pymongo import *
from threading import RLock

app_db_map = {
    "news" : {
        "host": "db",
        "db": "hackitall",
        "collection": "news"
    },
    "tags": {
        "host": "db",
        "db": "hackitall",
        "collection": "tags"
    }
}

class MongoSingleton:
    _instance = None
    _mutex = RLock()

    @classmethod
    def allow_instance_creation(self, app):
        return (MongoSingleton._instance is None or app_db_map[app]["host"] != MongoSingleton._instance.host or
                app_db_map[app]["db"] != MongoSingleton._instance.db or
                app_db_map[app]["collection"] != MongoSingleton._instance.collection)

    def __init__(self, app):
        if not self.allow_instance_creation(app):
            raise RuntimeError("Instance from this class already exists")
        self.host = app_db_map[app]["host"]
        self.db = app_db_map[app]["db"]
        self.collection = app_db_map[app]["collection"]
        self._client = MongoClient(self.host)
        self._db = self._client[self.db]
        self._collection = self._db[self.collection]

    @classmethod
    def __get_instance(self, app):
        with MongoSingleton._mutex:
            MongoSingleton._instance = (
                MongoSingleton(app) if self.allow_instance_creation(app)
                else MongoSingleton._instance)
        return MongoSingleton._instance
    
    @classmethod
    def get_client(self, app):
        instance = self.__get_instance(app)
        return instance._client
    
    @classmethod
    def get_db(self, app):
        instance = self.__get_instance(app)
        return instance._db

    @classmethod
    def get_collection(self, app):
        instance = self.__get_instance(app)
        return instance._collection