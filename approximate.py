#Challenge: Given the ability to get random numbers between 0 and 1, can you calculate (approximate) the value of pi? Proposed by Joma Tech 
import math, random

#Get user input for amount of random numbers to be generated
points_n = int(input("\nPlease input the desired amount of points: "))

#Initialize variables for the approximation of circle and square areas
area_circle = 0
area_square = 0

#Insert points into the square
for p in range(points_n):
    x = random.random()
    y = random.random()

    #Get distance between the origin and the inserted point
    distance = math.sqrt(x**2 + y**2)

    if(distance < 1):
        area_circle += 1
        area_square += 1
    else:
        area_square += 1

pi = (area_circle/area_square) * 4

print(f'\nApproximated value of pi: {pi}')