"""Provides basic arithmetic calculation functions."""


def sumar(a, b):
    """Adds two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
    """
    return a + b


def restar(a, b):
    """Subtracts the second number from the first.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The result of a - b.
    """
    return a - b


def multiplicar(a, b):
    """Multiplies two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.
    """
    return a * b


def dividir(a, b):
    """Divides the first number by the second.

    Args:
        a: The numerator.
        b: The denominator.

    Returns:
        The result of a / b.

    Raises:
        ZeroDivisionError: If the denominator (b) is zero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
