def pascal_triangle(n):
    # Step 2: Return an empty list if n <= 0
    if n <= 0:
        return []
    
    triangle = []  # Step 3: Initialize the triangle list
    
    for i in range(n):
        # Step 4: Create a new row
        row = [1] * (i + 1)  # Start with all 1s
        
        # Step 4: Calculate the values for the inner elements
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        triangle.append(row)  # Append the row to the triangle
    
    return triangle  # Step 6: Return the completed triangle

# Example usage
if __name__ == "__main__":
    n = 5
    triangle = pascal_triangle(n)
    
    # Print the triangle
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))
