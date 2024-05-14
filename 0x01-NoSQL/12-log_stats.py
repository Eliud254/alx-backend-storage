#!/usr/bin/env python3
"""The script that providing some stats about Nginx logs stored in Mdb"""
from pymongo import MongoClient


if __name__ == "__main__":
    '''Stats about Nginx logs'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    col = client.logs.nginx
    print("{} logs".format(col.estimated_document_count()))
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = col.count_documents({'method': method})
        print("\tmethod {}: {}".format(method, count))
    status_get = col.count_documents({'method': 'GET', 'path': "/status"})
    print("{} status check".format(status_get))
