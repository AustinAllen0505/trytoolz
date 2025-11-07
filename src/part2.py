
# Part II - Comparisons

def is_equal(a, b):
    """
    Check if two values are equal.

    Parameters:
        a (Any): First value
        b (Any): Second value

    Returns:
        bool: True if a is equal to b, False otherwise
    """
    return a == b

def greater_than(a, b):
    """
    Check if a is greater than b.

    Parameters:
        a (Any): First value
        b (Any): Second value

    Returns:
        bool: True if a greater than b, False otherwise
    """
    return a > b

def less_than(a, b):
    """
    Check if a is less than b.

    Parameters:
        a (Any): First value
        b (Any): Second value

    Returns:
        bool: True if a less than b, False otherwise
    """
    return a < b

def greater_than_or_equal_to(a, b):
    """
    Check if a is greater than or equal to b.

    Parameters:
        a (Any): First value
        b (Any): Second value

    Returns:
        bool: True if a is greater than or equal to b, False otherwise
    """
    return a >= b

def less_than_or_equal_to(a, b):
    """
    Check if a is less than or equal to b.

    Parameters:
        a (Any): First value
        b (Any): Second value

    Returns:
        bool: True if a is less than or equal to b, False otherwise
    """
    return a <= b

def falsy_or_truthy(value):
    """
    Check if a value is falsy or truthy.

    Parameters:
        value (Any): Value to check

    Returns:
        str: "truthy" if value is truthy, "falsy" if value is falsy
    """
    return "truthy" if value else "falsy"

def both(a, b):
    """
    Check if both a and b are truthy.

    Parameters:
        a (Any): First value
        b (Any): Second value

    Returns:
        bool: True if both a and b are truthy, False otherwise
    """
    return bool(a and b)

def either(a, b):
    """
    Check if either a or b is truthy.

    Parameters:
        a (Any): First value
        b (Any): Second value

    Returns:
        bool: True if either a or b is truthy, False otherwise
    """
    return bool(a or b)


