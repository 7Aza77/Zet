#task1
import math 
d = int(input('Enter degree: '))
radian = round(d * (math.pi/180), 6)
print(radian)


#task2
height = int(input('enter height: '))
a = int(input('enter first value: '))
b = int(input('enter second value: '))
S = (a+b) * height / 2
print('area of a trapezoid: ', S)


#task3
def calculate_polygon_area(sides, length):
    if sides < 3:
        return "polygon must have at least 3 sides."
    area = (sides * length**2) / (4 * math.tan(math.pi / sides))
    
    return area

sides = int(input("Enter number of sides: "))

length = float(input("Enter the length of a side: "))

area = round(calculate_polygon_area(sides, length), 2)
print("area of the polygon is: ", area)


#task4
a_parallelogram = float(input('Length of base: '))
h_parallelogram = float(input('Height of parallelogram: '))
print(a_parallelogram*h_parallelogram)