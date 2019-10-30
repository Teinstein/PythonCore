# Python Program to calculate area of different shapes
# This is a menu driven program to input what shape's
# area is required.

def circleArea(radius):
    return 3.142*float(radius)*(radius);

def rectangleArea(length,breadth):
    return float(length)*float(breadth);

def squareArea(side):
    return rectangleArea(side,side);

def traingleArea(base,height):
    return 0.5*float(base)*float*(height);

while True:
    print("Calculate Area of Following Figures:")
    print("1 for circle")
    print("2 for rectangle")
    print("3 for square")
    print("4 for triangle")
    print("0 to exit")
    option = int(input())
    if option == 0:
        break
    elif option == 1:
        radius = float(input("Enter radius:"))
        print("The area of cicle is :",circleArea(radius));
    elif option == 2:
        length = float(input("Enter length:"))
        breadth = float(input("Enter breadth:"))
        print("The area of rectangle is :",rectangleArea(length,breadth));
    elif option == 3:
        side = float(input("Enter side:"))
        print("The area of square is :",squareArea(side));
    elif option == 4:
        base = float(input("Enter base:"))
        height = float(input("Enter height:"))
        print("The area of triangle is :",traingleArea(base,height));    
    