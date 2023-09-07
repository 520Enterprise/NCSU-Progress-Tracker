def shipping_rate(weight):
   if weight <= 2:
       rate=weight*1.50
       return rate
   elif 2<weight <=6:
       rate=3.00+(weight-2)*3.00
       return rate
   elif 6<weight <=10:
       rate=3.00+12.00+(weight-6)*4.00
       return rate
   elif weight>10:
       rate=3.00+12.00+16.00+(weight-10)*4.75
       return rate
