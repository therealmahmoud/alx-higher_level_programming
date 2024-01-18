#!/usr/bin/python3
""" A class which can be accessed. """
import json


class Base:
    """Base model.

    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ JSON string representation of list_dictionaries. """
        if len(list_dictionaries) == 0 or list_dictionaries == None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
