import vector

my_vector = vector.Vector([1,2,3])
my_vector2 = vector.Vector([1,2,3])
my_vector3 = vector.Vector([-1,2,3])

print my_vector
print my_vector2
print my_vector3

print my_vector == my_vector2
print my_vector == my_vector3

print my_vector.plus(my_vector2)
#print my_vector.minus(my_vector2)
#print my_vector.times_scalar(3)