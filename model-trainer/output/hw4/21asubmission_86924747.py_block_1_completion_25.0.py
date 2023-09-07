def shipping_rate(weight):
    if 0 <= weight <= 2:
        price = weight*1.5
        return price
