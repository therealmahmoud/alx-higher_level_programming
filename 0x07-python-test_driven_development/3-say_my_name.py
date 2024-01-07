#!/usr/bin/python3
"""
 Function that divides all
 elements of a matrix.
"""


def say_my_name(first_name, last_name=""):

    """_summary_

    Args:
        first_name (string)
        last_name (str, optional)

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
