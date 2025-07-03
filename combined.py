import math
from collections import deque

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

def min_num_of_squares(n: int) -> int:
    """
    Determines the minimum number of perfect square numbers that sum up to the given integer n.

    Constraints:
        - 1 ≤ n ≤ 250,000
        - Runtime < 1 minute

    Args:
        n (int): The target integer.

    Returns:
        int: The minimal number of perfect squares that sum to n.
    """
    perfect_squares = [i ** 2 for i in range(1, int(math.isqrt(n)) + 1)]
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for sq in perfect_squares:
            if sq > i:
                break
            dp[i] = min(dp[i], dp[i - sq] + 1)

    return int(dp[n])

def mirrored_numbers(lower: str, upper: str) -> int:
    """
    Counts the amount of valid mirrored numbers between a given lower and upper bound (inclusive).
    
    A mirrored number reads the same when flipped upside down. Only the digits 0, 1, 2, 5, 6, 8, and 9
    can be used, where 6 becomes 9 and 9 becomes 6 upon mirroring.

    Constraints:
        - 0 <= int(lower) <= 10^16
        - 0 <= int(upper) <= 10^16
        - int(lower) <= int(upper)
        - Runtime < 1 minute

    Args:
        lower (str): Lower bound as a string (to support large numbers).
        upper (str): Upper bound as a string.

    Returns:
        int: Total number of mirrored numbers within the range.
    """
    mirror_map = {'0': '0', '1': '1', '2': '2', '5': '5', '8': '8', '6': '9', '9': '6'}
    center_digits = ['0', '1', '2', '5', '8']
    valid_numbers = []
    lower_int, upper_int = int(lower), int(upper)

    for length in range(len(lower), len(upper) + 1):
        queue = deque()

        if length % 2 == 1:
            queue.extend(center_digits)
        else:
            queue.append('')

        while queue:
            current = queue.popleft()

            if len(current) == length:
                if (current == '0' or current[0] != '0') and lower_int <= int(current) <= upper_int:
                    valid_numbers.append(current)

            elif len(current) + 2 <= length:
                for left, right in mirror_map.items():
                    new_number = left + current + right
                    queue.append(new_number)

    return len(valid_numbers)

def max_distance(intervals: list[list[int]]) -> int:
    """
    Calculates the maximum difference between a minimum and a maximum value from different intervals,
    where the minimum and maximum cannot come from the same interval.
    
    Constraints: 
        - 2 <= len(intervals) <= 10^5
        - 1 <= intervals[i].lengte <= 500
        - -10^4 <= intervals[i][j] <= 10^4
        - intervals[i] is sorted in ascending order
        - Runtime < 1 minute

    Args:
        intervals (list[list[int]]): A list of intervals, each represented as a list of two integers [min, max].

    Returns:
        int: The maximum difference between a minimum and a maximum from different intervals.
    """
    min_values = [interval[0] for interval in intervals]
    max_values = [interval[-1] for interval in intervals]

    global_min = min(min_values)
    global_max = max(max_values)

    index_min = min_values.index(global_min)
    index_max = max_values.index(global_max)

    if index_min == index_max:
        min_values.pop(index_min)
        max_values.pop(index_max)

        second_min = min(min_values)
        second_max = max(max_values)

        difference = max(global_max - second_min, second_max - global_min)
    else:
        difference = global_max - global_min

    return difference

def switches(binary_list: list[int]) -> int:
    """
    Determines the minimum number of switches (from 1 to 0 or vice versa)
    needed to make all zeros in the list contiguous, considering the list as circular.
    
    Constraints: 
        - 1 ≤ length of list ≤ 10^5
        - list[i] is either 0 or 1
        - Runtime < 1 minute

    Args:
        binary_list (list[int]): A list of zeros and ones.

    Returns:
        int: The minimum number of switches required.
    """
    if len(binary_list) == 1:
        return 0

    zero_count = binary_list.count(0)
    max_zeros_in_window = binary_list[:zero_count].count(0)
    zeros_in_window = max_zeros_in_window

    circular_list = binary_list + binary_list[:zero_count]
    
    for i in range(zero_count, len(binary_list) + zero_count):
        if circular_list[i] == 0:
            zeros_in_window += 1
        if circular_list[i - zero_count] == 0:
            zeros_in_window -= 1
        max_zeros_in_window = max(max_zeros_in_window, zeros_in_window)

    return zero_count - max_zeros_in_window


if __name__ == '__main__':
    print(find_target((35,2), (2,2)))  # Expected output: 5    
    print(min_num_of_squares(12))  # Expected output: 3
    print(mirrored_numbers("1001", "1200"))  # Expected output: 2
    print(max_distance([[0, 6], [3, 4], [2, 5], [1, 3]])) # Expected output: 5
    print(switches([0, 1, 1, 1, 0, 0, 0, 1, 1, 0])) # Expected output: 2
