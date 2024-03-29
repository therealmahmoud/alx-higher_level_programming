#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write((json.dumps(my_obj)))
