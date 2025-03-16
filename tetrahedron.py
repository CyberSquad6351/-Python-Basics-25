# Function to calculate the cross product of two vectors
def cross_product(v1, v2):
    return [
        v1[1] * v2[2] - v1[2] * v2[1],  # x-component
        v1[2] * v2[0] - v1[0] * v2[2],  # y-component
        v1[0] * v2[1] - v1[1] * v2[0]   # z-component
    ]

# Function to calculate the magnitude of a vector
def magnitude(v):
    return (v[0]**2 + v[1]**2 + v[2]**2) ** 0.5

# Function to calculate the area of a triangle given its vertices
def triangle_area(A, B, C):
    # Vectors AB and AC
    AB = [B[0] - A[0], B[1] - A[1], B[2] - A[2]]
    AC = [C[0] - A[0], C[1] - A[1], C[2] - A[2]]
    
    # Cross product of AB and AC
    cross_prod = cross_product(AB, AC)
    
    # Area is half the magnitude of the cross product
    area = 0.5 * magnitude(cross_prod)
    
    return area

# Function to calculate the surface area of a tetrahedron
def tetrahedron_area(A, B, C, D):
    # Calculate areas of the four triangular faces
    area_ABC = triangle_area(A, B, C)
    area_ABD = triangle_area(A, B, D)
    area_ACD = triangle_area(A, C, D)
    area_BCD = triangle_area(B, C, D)
    
    # Total surface area is the sum of the areas of the four faces
    total_area = area_ABC + area_ABD + area_ACD + area_BCD
    
    return total_area

# Example coordinates for the vertices of the tetrahedron
A = [1, 0, 0]  # Vertex A
B = [0, 1, 0]  # Vertex B
C = [0, 0, 1]  # Vertex C
D = [1, 1, 1]  # Vertex D

# Calculate the surface area of the tetrahedron
surface_area = tetrahedron_area(A, B, C, D)

# Print the result
print("Surface area of the tetrahedron:", surface_area)
