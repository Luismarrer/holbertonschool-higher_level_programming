#!/usr/bin/python3
"""
This module contains BaseGeometry class.
"""


class BaseGeometry:
    """
    Base class.

    Methods:
        area(self): Raises an Exception indicating
        that it is not implemented.

        integer_validator(self, name, value): Validates that
        a parameter is a positive integer.
    """
    def area(self):
        """
        Base function.

        Raises:
            Exception: Always raises an exception with the
            message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a parameter is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value of the parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")