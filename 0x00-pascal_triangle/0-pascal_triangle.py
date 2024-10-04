def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal’s triangle of n.
    
    Args:
    n (int): The number of rows in Pascal's triangle.
    
    Returns:
    List[List[int]]: A list of lists containing the integers in Pascal's triangle.
    """
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    for i in range(1, n):
        # Create the next row starting with 1
        row = [1]
        
        # Use a list comprehension to calculate the middle values of the row
        row.extend([triangle[i - 1][j - 1] + triangle[i - 1][j] for j in range(1, i)])
        
        # End each row with 1
        row.append(1)
        
        # Add the completed row to the triangle
        triangle.append(row)
    
    return triangle
