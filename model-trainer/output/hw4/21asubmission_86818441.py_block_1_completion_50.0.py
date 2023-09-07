def shipping_rate(weight):
    if weight <= 2:
        return 1.50 * float(weight)
    elif weight > 2 and weight < 6:
        return (1.50 * 2.0) + ((weight - 2.0) * 3.00)
    elif weight > 6 and weight < 10:
        return 1.50 * 2.0 + (3.00 * float(weight)) + (4.00 * (float(weight) - 6.0))
    elif weight > 10:
        return (1.50 * 2.0) + (3.00 * 4) + (4.00 * 4) + (4.75 * (float(weight) - 10.0))
