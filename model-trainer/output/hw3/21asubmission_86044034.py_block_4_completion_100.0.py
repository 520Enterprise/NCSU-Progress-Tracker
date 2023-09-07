import math
def cylinder_volume(radius, height):
    volume=math.pi*radius**2*height
    return volume
def testing_cylinder_volume():
    print('Cylinder volume(4,3)')
    print('Expected value: 150.79644737231007')
    actual=cylinder_volume(4, 3)
    print('Volume: ' +str(actual))
    print('Cylinder volume(10,1)')
    print('Expected value: 314.1592653589793')
    actual=cylinder_volume(10,1)
    print('Volume: ' +str(actual))
    print('Cylinder volume(2,5)')
    print('Expected value: 62.83185307179586')
    actual=cylinder_volume(2,5)
    print('Volume: ' +str(actual))
    testing_cylinder_volume()
