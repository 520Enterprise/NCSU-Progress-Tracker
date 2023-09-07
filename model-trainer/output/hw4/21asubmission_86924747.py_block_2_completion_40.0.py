def shipping_rate(weight):
    if 0 <= weight <= 2:
        price = weight*1.5
        return price
    elif 2 < weight <= 6:
        price = 1.5*2
        price += (weight - 2)*3
        return price
