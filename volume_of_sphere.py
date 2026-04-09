#Uiin John Kim
#volume_of_sphere
#I310D


def calculate_volume_of_sphere(radius):
    pi = 3.14159
    volume = (4/3) * pi * (radius ** 3)
    return volume

# find values when the radius is 30, 40
r1 = 30
r2 = 40
print(f"The volume of a sphere with radius {r1} is: {calculate_volume_of_sphere(r1)}")
print(f"The volume of a sphere with radius {r2} is: {calculate_volume_of_sphere(r2)}")
