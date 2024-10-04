def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n.
    
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
        # Start each row with 1
        row = [1]
        # Calculate the values in the middle of the row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # End each row with 1
        row.append(1)
        # Add the row to the triangle
        triangle.append(row)
    
    return triangle
