# databaseConnection.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDateTime
import pymongo

class DatabaseConnection():
    def dbSave(self, query, req):
        client = pymongo.MongoClient(
            "mongodb+srv://user1:pwd123@cluster0.wqt4f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        # print(client.list_database_names())
        db = client.get_database('software')
        if req == 1 : #alarm
            collection = db.get_collection('alarm')
        elif req == 2: #symptom
            collection = db.get_collection('symptom')
        elif req == 3: #action
            collection = db.get_collection('action')
        collection.insert_one(query)

    def loadDB(self, req):
        client = pymongo.MongoClient(
            "mongodb+srv://user1:pwd123@cluster0.wqt4f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        # print(client.list_database_names())
        db = client.get_database('software')
        query_lst = []
        # print("이까진 됨")
        if req == 1 : #alarm
            collection = db.get_collection('alarm')
            queries = collection.find()
            # print("111")
            for query in queries:
                query_lst.append([query["time"], query["inform"]])
        elif req == 2: #symptom
            collection = db.get_collection('symptom')
            queries = collection.find()
            for query in queries:
                query_lst.append( [query["time"], query["symptom"], query["level"]])
        elif req == 3: #action
            collection = db.get_collection('action')
            queries = collection.find()
            for query in queries:
                query_lst.append([query["time"], query["action"]])
        print(query_lst)

        return query_lst

