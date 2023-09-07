def shipping_rate(weight):
    if 2 >= weight:
        return (1.50*weight)
    elif 2 < weight <= 6:
        return ((3.00*(weight-2))+3)
    elif 6 < weight <= 10:
        return ((4.00*(weight-6))+15)
    else:
        return ((4.75*(weight-10))+31)
    print('Testing shipping_rate(2)')
    print('Expected value: 3')
    actual = shipping_rate(2)
    print('Actual value: ' + str(actual))
    print('Testing shipping_rate(4.5)')
    print('Expected value: 10.5')
    actual1 = shipping_rate(4.5)
    print('Actual value: ' + str(actual1))
    print('Testing shipping_rate(12)')
    print('Expected value: 40.5')
    actual2 = shipping_rate(12)
    print('Actual value: ' + str(actual2))
