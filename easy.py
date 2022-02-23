

#Create a function that takes two numbers as arguments and return their sum.###

from turtle import width


def add(a,b):
    c = a +b
    return c

#Create a function that takes a number as an argument, increments the number by +1 and returns the result.###

def increment(num):
    num=+1
    return num

#Write a function that takes an integer minutes and converts it to seconds.###

def MinuteToSecond(minute):
    second = minute * 60
    return second

#Write a function that takes the base and height of a triangle and return its area.###

def AreaOfTriangle(base,height):
    Area = (base * height) / 2
    return Area

#Write a function that take the number and return cube of given number.###

def Cube(num):
    num ** 3
    return num

#Write a function that converts hours into seconds.###
def HoursToSeconds(hours):
    second = hours * 60 * 60
    return second

#Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.
def MaxRange(side1,side2):
    Max = (side1 + side2) - 1
    return Max

#Create a function that takes a string and returns it as an integer.

def StringToInteger(string):
    Int = int(string)
    return Int

#Create a function that takes the age in years and returns the age in days.

def AgeInDays(years):
    days = years * 365
    return days

#Create a function that takes length and width and finds the perimeter of a rectangle.

def Perimeter(length, width):
    perimeter = (length * 2) + (width * 2)
    return perimeter

#Create a function that takes voltage and current and returns the calculated power. v*C

def Power(voltage, current):
    power = voltage * current
    return power