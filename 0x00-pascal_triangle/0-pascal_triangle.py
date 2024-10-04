def pascal_triangle(n):
    if n <= 0:
        return []  # Return an empty list for non-positive n

    triangle = []  # Initialize the triangle list

    for i in range(n):
        row = [1] * (i + 1)  # Start with a row of 1s
        for j in range(1, i):  # Fill in the values for the inner elements
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)  # Add the completed row to the triangle

    return triangle  # Return the complete triangle
