#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a Square, inheriting from the Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, size, size)
    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y}\
 - {self.width}/{self.height}"
 