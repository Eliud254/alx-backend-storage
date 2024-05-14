#!/usr/bin/env python3
"""
mongo document
"""


def list_all(mongo_collection):
    """
    function document
    """
    return list(mongo_collection.find())
