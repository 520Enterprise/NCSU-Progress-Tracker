def shipping_rate(weight):
    if 2 >= weight:
        return (1.50*weight)
    elif 2 < weight <= 6:
        return ((3.00*(weight-2))+3)
