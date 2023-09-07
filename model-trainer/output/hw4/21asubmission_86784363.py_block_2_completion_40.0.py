def shipping_rate(weight):
   if weight <= 2:
       rate=weight*1.50
       return rate
   elif 2<weight <=6:
       rate=3.00+(weight-2)*3.00
       return rate
