def shipping_rate(weight):
    if weight <= 2:
        return 1.50 * float(weight)
    elif weight > 2 and weight < 6:
        return (1.50 * 2.0) + ((weight - 2.0) * 3.00)
