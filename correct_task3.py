import math

def average_valid_measurements(values):

    if not values:
        return 0.0
    
    total = 0
    valid_count = 0
    
    for v in values:
        if v is None:
            continue
        
        try:
            numeric_value = float(v)
            # Skip NaN and Inf values
            if math.isnan(numeric_value) or math.isinf(numeric_value):
                continue
            total += numeric_value
            valid_count += 1
        except (ValueError, TypeError):
            # Skip values that cannot be converted to float
            continue
    
    if valid_count == 0:
        return 0.0
    
    return total / valid_count
