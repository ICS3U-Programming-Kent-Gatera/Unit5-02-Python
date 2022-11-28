#!/usr/bin/env python3
# Created By: Kent Gatera
# Date: 10.26.22
# Calculating the area of a triangle using arguments.


# Defining the function that calculates the area using the arguments.
def calc_area(base, height):
    tri_area = (base * height) / 2
    print("The area of the triangle is {:.2f} cm".format(tri_area))


# Defining main, where we get our input, and call area function.
def main():

    # Try catch to get the input (dimensions of the triangle).
    try:
        user_base = float(input("What is the base of the triangle (cm)?: "))
        user_height = float(input("What is the height of the height (cm)?: "))
    except:
        print("Invalid input.")

    if user_base > 0 and user_height > 0:
        # Calling the area calculating function.
        calc_area(user_base, user_height)
    else:
        print("Invalid input. (Enter positive measurements)")


if __name__ == "__main__":
    # Calling the function.
    main()
