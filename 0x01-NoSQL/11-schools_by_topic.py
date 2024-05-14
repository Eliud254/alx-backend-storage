#!/usr/bin/env python3
"""
mongodb document
"""


def schools_by_topic(mongo_collection, topic):
    """
    function document
    """
    return mongo_collection.find({"topics": topic})
