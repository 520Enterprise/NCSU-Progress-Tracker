def shipping_rate(weight):
    if weight ==0:
        return 0
    elif 0<weight<=2:
        shipping_charges= weight *1.50
        return shipping_charges
    elif 2<weight<=6:        
        shipping_charges=(weight-2)*3 + 2*1.5
        return shipping_charges    
