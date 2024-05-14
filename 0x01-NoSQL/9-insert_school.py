#!/usr/bin/env python3
"""
moongo db document
"""


def insert_school(mongo_collection, **kwargs):
    """
    function document
    """
    return mongo_collection.insert_one(kwargs).inserted_id
