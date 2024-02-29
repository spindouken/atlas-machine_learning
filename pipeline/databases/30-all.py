#!/usr/bin/env python3
"""task30"""


def list_all(mongo_collection):
    """list all documents in a collection"""
    return mongo_collection.find()
