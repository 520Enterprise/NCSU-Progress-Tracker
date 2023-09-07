def shipping_rate(weight):
    if weight <= 2:
        charge = weight * 1.5
        return charge
