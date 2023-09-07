def shipping_rate(weight):
    if weight <= 2:
        return 1.50 * float(weight)
