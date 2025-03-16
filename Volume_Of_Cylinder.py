# Function to calculate the volume of a cylinder without using math module
def cylinder_volume(radius, height):
    pi = 3.14159  # Approximation of pi
    return pi * radius**2 * height

# Example values
radius = 5  # radius of the base of the cylinder
height = 10  # height of the cylinder

# Calculate the volume
volume = cylinder_volume(radius, height)

# Print the volume
print("Volume of the cylinder:", volume)
