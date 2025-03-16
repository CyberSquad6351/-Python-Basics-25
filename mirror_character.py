# Function to find mirror characters using a dictionary
def find_mirror_characters(string):
    mirror_dict = {}  # Dictionary to store mirror character mappings
    length = len(string)
    
    # Loop through the string and map characters to their mirror counterparts
    for i in range(length):
        # Find the mirror character index (from the end of the string)
        mirror_dict[string[i]] = string[length - 1 - i]
    
    return mirror_dict

# Example string
string = "abcdef"

# Find mirror characters
mirror_characters = find_mirror_characters(string)

# Print the result
print("Mirror character dictionary:", mirror_characters)
