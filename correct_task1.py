def calculate_average_order_value(orders):
    if not orders:
        return 0.0
    
    total = 0
    valid_count = 0
    
    for order in orders:
        # Skip if status is missing or cancelled
        status = order.get("status")
        if status is None or status == "cancelled":
            continue
        
        # Skip if amount is missing or not numeric
        amount = order.get("amount")
        if amount is None:
            continue
        
        try:
            numeric_amount = float(amount)
            total += numeric_amount
            valid_count += 1
        except (ValueError, TypeError):
            # Skip orders with non-numeric amounts
            continue
    
    if valid_count == 0:
        return 0.0
    
    return total / valid_count
