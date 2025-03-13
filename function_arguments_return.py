import math  # Import the math module for mathematical calculations

# Define a function to calculate the area of a circle
def circle_area(radius):
    """Calculate and return the area of a circle given its radius."""
    area = math.pi * (radius ** 2)  # Formula: π * radius^2
    return area  # Return the calculated area

# Define the radius value
radius_value = 5

# Call the function and store the result
area_result = circle_area(radius_value)

# Print the formatted result
print(f"The area of a circle with radius {radius_value} is: {area_result:.2f}")
