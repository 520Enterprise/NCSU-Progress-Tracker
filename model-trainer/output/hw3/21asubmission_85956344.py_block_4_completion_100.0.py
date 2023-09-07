def cylinder_volume(radius, height):
    volume = math.pi*radius**2*height 
    return volume 
def testing_cylinder_volume():
    print("Testing cylinder_volume(4,3)")
    print("Expected value: 150.79644737231007")
    actual = cylinder_volume(4,3)
    print("Actual value:" + str(actual))
    print("Testing cylinder_volume(10,1)")
    print("Expected value: 314.1592653589793")
    actual = cylinder_volume(10,1)
    print("Actual value:" + str(actual))
import math
testing_cylinder_volume()
