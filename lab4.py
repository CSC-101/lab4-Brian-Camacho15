import math

import data

# Write your functions for each part in the space below.

# Part 1
#1 A function that returns a list that contains the first element of each nested list from the input
#2 Input: [2,5,4,5[7,5,2,4,0,1]]
#3 output:list[7]
#Name first_element

def first_element(list:list[list[int]]) -> list[int]:
    empty_check= [x for x in list if x]
    return [x[0] for x in empty_check]

# Part 2
#A function that returns a list containg the x-coordinate of each point in the iput list
#Input: [x,y],[3,8],[6,9]
#Output: [x,3,6]
#Name x_coordinates
def x_coordinates(points: list[float])-> list[int]:
    return [point.x for point in points]

# Part 3
#a function that retruns all points from the imput list that are in the first quadrant which means both x and y have to be postive.
 #Input: (4,6),(-2,-4),(-2,4),(2,-2)
 #Output: (4,6)
 #Name are_in_postive_quadrant
def are_in_positive_quadrant(points: list[data.Point]) -> list[data.Point]:
    return[point for point in points if point.x> 0 and point.y > 0]

# Part 4
#Write a function that returns the magnitude/distance from two points
# Make a function that takes the two points and subtracts d1 from d2 and square both, add them, then squareoot them
#Input: d1(4,6), d2(7,2)
#Output: distance=5
def distance(d1:data.Point, d2: data.Point) -> float:
    x= d2.x - d1.x
    y= d2.y - d1.y
    total= math.sqrt(x**2 + y**2)
    return total

# Part 5
#Write a fucntion that returns the distance in mahhatan or the ablsulte value.
#Input: d1(8,6), d2(2,4)
#Output:manhattan_distance = 8
#
def manhattan_distance(d1:data.Point, d2:data.Point) -> float:
   x= abs(d2.x - d1.x)
   y= abs(d2.y - d1.y)
   return x+y

# Part 6
# Write function that returns a list that shows the distance from the origin.
#Input: [(4,6),(7,8),(35,4)]
#Output:[(4,6),(7,8),(35,4)]
#name distance_all
def distance_all(points: list[data.Point]) -> list[float]:
#create the origin variable
    origin= data.Point(0,0)
    return [manhattan_distance(origin,points) for points in points]

