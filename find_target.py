def find_target(grid_size: tuple[int, int], target_pos: tuple[int, int]) -> int:
    """
    Determines the number of steps needed to find a target in a 2D grid using a binary search-like approach.
    
    The grid has dimensions (n, m) and the target is located at (x, y).
    The algorithm narrows down both dimensions simultaneously.

    Constraints:
        - 0 ≤ n ≤ 10^140000
        - 0 ≤ m ≤ 10^140000
        - 0 ≤ x ≤ n
        - 0 ≤ y ≤ m
        - The function must return the result within 1 minute

    Args:
        grid_size (tuple[int, int]): Tuple with grid dimensions (n, m).
        target_pos (tuple[int, int]): Tuple with target coordinates (x, y).

    Returns:
        int: Number of steps required to locate the target.
    """
    low_x = 0
    high_x = grid_size[0]
    low_y = 0
    high_y = grid_size[1]

    steps = 0

    while low_x <= high_x and low_y <= high_y:
        steps += 1
        mid_x = (low_x + high_x) // 2
        mid_y = (low_y + high_y) // 2

        if mid_x == target_pos[0] and mid_y == target_pos[1]:
            break
        if mid_x < target_pos[0]:
            low_x = mid_x + 1
        elif mid_x > target_pos[0]:
            high_x = mid_x - 1

        if mid_y < target_pos[1]:
            low_y = mid_y + 1
        elif mid_y > target_pos[1]:
            high_y = mid_y - 1

    return steps


if __name__ == '__main__':
    grid = (35, 2)
    target = (2, 2)
    print(find_target(grid, target))  # Expected output: 5
