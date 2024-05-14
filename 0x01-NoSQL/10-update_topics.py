#!/usr/bin/env python3
"""
mongodb document
"""


def update_topics(mongo_collection, name, topics):
    """
    function document
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
