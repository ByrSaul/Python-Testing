def sum(a, b):
    """
    >>> sum(5, 7)
    12

    >>> sum(5, -5)
    0
    """
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a * b

def division(a, b):
    """
    >>> division(15, 3)
    5

    >>> division(5, 0)
    
    """
    try:
        return a/b
    except ZeroDivisionError:
        raise ZeroDivisionError("No se puede dividir entre cero")