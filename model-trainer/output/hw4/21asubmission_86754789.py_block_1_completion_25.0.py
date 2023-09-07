def shipping_rate(weight):
    if weight ==0:
        return 0
    elif 0<weight<=2:
        shipping_charges= weight *1.50
        return shipping_charges
