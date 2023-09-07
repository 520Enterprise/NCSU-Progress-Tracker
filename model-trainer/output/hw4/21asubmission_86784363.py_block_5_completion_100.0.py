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
def test_shipping_rate():
    print("Testing shipping_rate(2)")
    expected=3.0
    actual=shipping_rate(2)
    if expected == actual:
        print("Test passed!")
    else:
        print("Test failed.")
        print("Expected:", expected)
        print("Actual:", actual)
    print("Testing shipping_rate(4.5)")
    expected=10.5
    actual=shipping_rate(4.5)
    if expected == actual:
        print("Test passed!")
    else:
        print("Test failed.")
        print("Expected:", expected)
        print("Actual:", actual)
    test_shipping_rate()
