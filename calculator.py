"""team-calculator: общий модуль калькулятора."""

# --- операции ---


def add(a, b):
    """Сложение двух чисел."""
    return a + b


def subtract(a, b):
    """Вычитание: a - b."""
    return a - b


def multiply(a, b):
    """Умножение двух чисел."""
    return a * b


def divide(a, b):
    """Деление: a / b, на ноль делить нельзя."""
    if b == 0:
        raise ValueError("Деление на ноль")
    return a / b


def power(a, b):
    """Возведение в степень."""
    return a ** b

def mod(a, b):
    """Остаток от деления."""
    return a % b

