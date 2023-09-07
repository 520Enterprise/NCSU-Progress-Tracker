import math
def cylinder_volume(radius, height):
    volume = math.pi * (radius**2) * height
    return volume
def test_cylinder_volume1():
    print("test_cylinder_volume(4,3)")
    print("Expected value:  150.79644737231007")
    actual =cylinder_volume(4,3)
    print("Actual value: " + str(actual))
def test_cylinder_volume2():
    print("test_cylinder_volume(10,1)")
    print("Expected value:  314.1592653589793")
    actual =cylinder_volume(10,1)
    print("Actual value: " + str(actual))
    test_cylinder_volume1()
    test_cylinder_volume2()
