def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        return f"The result of dividing by is: {result}"
    except ZeroDivisionError:
        return "Error: You can't divide by zero."
    except ValueError:
        return "Error: Please enter valid integers."