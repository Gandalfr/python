import vector
import math

my_vector = vector.Vector([1,2,3])
my_vector2 = vector.Vector([1,2,3])
my_vector3 = vector.Vector([-1,2,3])
zero_vector = vector.Vector([0,0,0])
test_vector = vector.Vector([1.996,3.108,-4.554])



# print my_vector
# print my_vector2
# print my_vector3

# print my_vector == my_vector2
# print my_vector == my_vector3

# print my_vector.plus(my_vector2)
# print test_vector.magnitude()
# print test_vector.direction()
# print test_vector.normalized()

print my_vector.dotProduct(my_vector2)
print my_vector.angle(my_vector2)

exa_1 = vector.Vector([7.887,4.138])
exa_2 = vector.Vector([-8.802,6.776])

exb_1 = vector.Vector([3.183,-7.627])
exb_2 = vector.Vector([-2.668,5.319])

exc_1 = vector.Vector([-5.955,-4.904,-1.874])
exc_2 = vector.Vector([-4.496,-8.755,7.103])

exd_1 = vector.Vector([7.35,0.221,5.188])
exd_2 = vector.Vector([2.751,8.259,3.985])

print exa_1.dotProduct(exa_2)
print exc_1.dotProduct(exc_2)

print exb_1.angle(exb_2)
print exd_1.angle(exd_2) * 180 / math.pi
#print zero_vector.normalized()
#print my_vector.minus(my_vector2)
#print my_vector.times_scalar(3)