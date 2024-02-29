#!/usr/bin/env python3
"""task33"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic

    mongo_collection will be the pymongo collection object
    topic (string) will be topic searched
    """
    return list(mongo_collection.find({"topics": topic}))
