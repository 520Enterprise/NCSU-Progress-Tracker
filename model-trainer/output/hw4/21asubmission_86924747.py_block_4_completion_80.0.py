def shipping_rate(weight):
    if 0 <= weight <= 2:
        price = weight*1.5
        return price
    elif 2 < weight <= 6:
        price = 1.5*2
        price += (weight - 2)*3
        return price
    elif 6 < weight <= 10:
        price = 1.5*2
        price += (6-2)*3
        price += (weight - 6)*4
        return price
    elif weight > 10:
        price = 1.5*2
        price += (6-2)*3
        price += (10-6)*4
        price += (weight-10)*4.75
        return price
