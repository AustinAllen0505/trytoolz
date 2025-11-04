"""
TestPylot Framework - Example Implementations
This module demonstrates how to implement functions for the TestPylot framework.
"""


def sum(*args):
    """
    Sum all arguments.

    Args:
        *args: Variable number of numeric arguments

    Returns:
        The sum of all arguments

    Examples:
        >>> sum(1, 2, 3)
        6
        >>> sum(5)
        5
        >>> sum()
        0
    """
    total = 0
    for num in args:
        total += num
    return total


def multiply(*args):
    """
    Multiply all arguments together.

    Args:
        *args: Variable number of numeric arguments

    Returns:
        The product of all arguments

    Examples:
        >>> multiply(2, 3, 4)
        24
        >>> multiply(5)
        5
        >>> multiply(2, 2, 2, 2)
        16
    """
    pass
