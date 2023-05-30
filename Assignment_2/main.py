#Travis Gibson
#SDEV 300

import string # Used for string manipulation and defining character sets for password generation
import secrets # Used for generating secure random numbers (e.g., for password generation)
import math # Used for mathematical calculations and functions
from datetime import datetime # Used for working with dates and times (e.g., calculating the number of days until a specific date)

# Function to generate a secure password
def generate_secure_password():
    length = int(input("Enter the length of the password: "))
    complexity = input("Enter the complexity (U for uppercase, L for lowercase, N for numbers, S for special characters): ")

    characters = ""
    if 'U' in complexity:
        characters += string.ascii_uppercase
    if 'L' in complexity:
        characters += string.ascii_lowercase
    if 'N' in complexity:
        characters += string.digits
    if 'S' in complexity:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    print("Generated Password:", password)

# Function to calculate and format a percentage
def calculate_percentage():
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    decimal_points = int(input("Enter the number of decimal points for formatting: "))

    percentage = (numerator / denominator) * 100
    formatted_percentage = "{:.{}f}".format(percentage, decimal_points)
    print("Formatted Percentage:", formatted_percentage, "%")

# Function to calculate the number of days until July 4, 2025
def days_until_july_4_2025():
    current_date = datetime.now()
    target_date = datetime(2025, 7, 4)
    remaining_days = (target_date - current_date).days
    print("Days until July 4, 2025:", remaining_days)

# Function to calculate the leg of a triangle using the Law of Cosines
def calculate_triangle_leg():
    side_a = float(input("Enter the length of side a: "))
    side_b = float(input("Enter the length of side b: "))
    angle_c = float(input("Enter the measure of angle C in degrees: "))

    angle_c_rad = math.radians(angle_c)
    side_c = math.sqrt(side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(angle_c_rad))
    print("Length of side c:", side_c)

# Function to calculate the volume of a right circular cylinder
def calculate_cylinder_volume():
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))

    volume = math.pi * radius**2 * height
    print("Volume of the cylinder:", volume)

# Main menu function
def main_menu():
    while True:
        print("\nMenu:")
        print("a. Generate Secure Password")
        print("b. Calculate and Format a Percentage")
        print("c. How many days from today until July 4, 2025?")
        print("d. Use the Law of Cosines to calculate the leg of a triangle")
        print("e. Calculate the volume of a Right Circular Cylinder")
        print("f. Exit program")

        choice = input("Enter your choice (a, b, c, d, e, or f): ")

        if choice == 'a':
            generate_secure_password()
        elif choice == 'b':
            calculate_percentage()
        elif choice == 'c':
            days_until_july_4_2025()
        elif choice == 'd':
            calculate_triangle_leg()
        elif choice == 'e':
            calculate_cylinder_volume()
        elif choice == 'f':
            print("Thank you for visiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main
main_menu()
