def shipping_rate(weight):
    if weight <= 2:
        charge = weight * 1.5
        return charge
    elif 2 < weight <= 6:
        charge = 2 * 1.5 + (weight - 2) * 3
        return charge
    elif 6 < weight <= 10:
        charge = 2 * 1.5 + 4 * 3 + (weight - 6) * 4.00
        return charge
