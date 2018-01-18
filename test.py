import vector

my_vector = vector.Vector([1,2,3])
my_vector2 = vector.Vector([1,2,3])
my_vector3 = vector.Vector([-1,2,3])
zero_vector = vector.Vector([0,0,0])
test_vector = vector.Vector([1.996,3.108,-4.554])

print my_vector
print my_vector2
print my_vector3

print my_vector == my_vector2
print my_vector == my_vector3

print my_vector.plus(my_vector2)
print test_vector.magnitude()
print test_vector.direction()
print test_vector.normalized()
#print zero_vector.normalized()
#print my_vector.minus(my_vector2)
#print my_vector.times_scalar(3)