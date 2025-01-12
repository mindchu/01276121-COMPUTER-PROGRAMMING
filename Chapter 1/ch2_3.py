print(" *** Finding circle area *** ")
diameter = input("Enter diameter : ")
diameter = float(diameter)
r = diameter/2
pi = 3.1415926
circleArea = pi*r*r
print("Circle area =", circleArea)
print(f"Circle area = {circleArea:0.2f}")     # Display the result to 2 decimal places.
print(f"whole number => {int(circleArea)}")   # Show only the integer part of the result.