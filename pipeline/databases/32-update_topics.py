#!/usr/bin/env python3
"""task32"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name

    mongo_collection will be the pymongo collection object
    name (string) will be the school name to update
    topics (list of strings) will be a list of topics approached in the school
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
