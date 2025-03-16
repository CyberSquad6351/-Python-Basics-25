# Function to find vertex, focus, and directrix of a parabola
def parabola_properties(a, h, k):
    # Vertex is at (h, k)
    vertex = (h, k)
    
    # Focus is at (h, k + 1/(4a))
    focus = (h, k + 1 / (4 * a))
    
    # Directrix is y = k - 1/(4a)
    directrix = k - 1 / (4 * a)
    
    return vertex, focus, directrix

# Example values for a parabola y = a(x - h)^2 + k
a = 1  # coefficient a
h = 2  # x-coordinate of the vertex
k = 3  # y-coordinate of the vertex

# Get the vertex, focus, and directrix
vertex, focus, directrix = parabola_properties(a, h, k)

# Print the results
print("Vertex:", vertex)
print("Focus:", focus)
print("Directrix: y =", directrix)
