
# Part I - Data Types & Basic Mathematical Operations


def data_type(value):
    """
    Returns the data type of the input argument.

    Parameters:
        value (any): The value to determine the data type of

    Returns:
        str: The data type of the value as a string
    """
    return type(value).__name__

def add(a, b):
    """
    Returns the sum of two input arguments.

    Parameters:
        a (int): The first input argument
        b (int): The second input argument

    Returns:
        int: The sum of a and b
    """
    return a + b

def subtract(a, b):
    """
    Returns the difference of two input arguments.

    Parameters:
        a (int): The first input argument
        b (int): The second input argument

    Returns:
        int: The difference of a and b
    """
    return a - b

def multiply(a, b):
    """
    Returns the product of two input arguments.

    Parameters:
        a (int): The first input argument
        b (int): The second input argument

    Returns:
        int: The product of a and b
    """
    return a * b

def divide(a, b):
    """
    Returns the result of dividing the first input argument by the second input argument.

    Parameters:
        a (int): The first input argument (dividend)
        b (int): The second input argument (divisor)

    Returns:
        float: The division of a and b
    """
    return a / b

def floor_divide(a, b):
    """
    Returns the result of floor division of the first input argument by the second input argument.

    Parameters:
        a (int): The first input argument (dividend)
        b (int): The second input argument (divisor)

    Returns:
        int: The result of floor division of a and b
    """
    return a // b


def get_remainder(a, b):
    """
    Returns the remainder of dividing the first input argument by the second input argument.

    Parameters:
        a (int): The first input argument (dividend)
        b (int): The second input argument (divisor)

    Returns:
        int: The remainder of a and b
    """
    return a % b

def increment(a):
    """
    Returns the incremented value of the input argument.

    Parameters:
        a (int): The input argument to be incremented

    Returns:
        int: The incremented value of a
    """
    return a + 1

def decrement(a):
    """
    Returns the decremented value of the input argument.

    Parameters:
        a (int): The input argument to be decremented

    Returns:
        int: The decremented value of a
    """
    return a - 1

def exponent(a, b):
    """
    Returns the result of raising the first input argument to the power of the second input argument.

    Parameters:
        a (int): The first input argument (base)
        b (int): The second input argument (exponent)

    Returns:
        int: The result of raising a to the power of b
    """
    return a ** b
