def shipping_rate(weight):
    if weight <= 2:
        return 1.50 * float(weight)
    elif weight > 2 and weight < 6:
        return (1.50 * 2.0) + ((weight - 2.0) * 3.00)
    elif weight > 6 and weight < 10:
        return 1.50 * 2.0 + (3.00 * float(weight)) + (4.00 * (float(weight) - 6.0))
    elif weight > 10:
        return (1.50 * 2.0) + (3.00 * 4) + (4.00 * 4) + (4.75 * (float(weight) - 10.0))
#@#
def testing_shipping_rate():
    print("testing shipping_rate(2)")
    expected = 3.0
    actual = shipping_rate(2)
    if expected == actual:
        print("test passed!")
    else:
        print("Test failed.")
        print("Expected: ", expected)
        print("Actual: ", actual)
    print("testing shipping_rate(4.5)")
    expected = 10.5
    actual = shipping_rate(4.5)
    if expected == actual:
        print("test passed!")
    else:
        print("Test failed.")
        print("Expected: ", expected)
        print("Actual: ", actual)
    print("testing shipping_rate(12)")
    expected = 40.5
    actual = shipping_rate(12)
    if expected == actual:
        print("test passed!")
    else:
        print("Test failed.")
        print("Expected: ", expected)
        print("Actual: ", actual)
    testing_shipping_rate()
#@#