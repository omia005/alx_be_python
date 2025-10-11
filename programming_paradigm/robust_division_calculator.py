def safe_divide(numerator, denominator):
  try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        result = num / den
        return str(result)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
