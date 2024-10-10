#!/usr/bin/python3

def canUnlockAll(boxes):
    # Initialize the visited list
    visited = [False] * len(boxes)
    visited[0] = True  # The first box is unlocked
    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()  # Get the last box in the stack
        for key in boxes[current_box]:  # Check the keys in the current box
            if key < len(boxes) and not visited[key]:  # If the box is valid and not visited
                visited[key] = True  # Mark it as visited
                stack.append(key)  # Add the box to the stack to explore later

    # Check if all boxes have been visited
    return all(visited)

# Sample test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Should return True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Should return True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Should return False

