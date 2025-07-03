def switches(binary_list: list[int]) -> int:
    """
    Determines the minimum number of switches (from 1 to 0 or vice versa)
    needed to make all zeros in the list contiguous, considering the list as circular.
    
    Constraints: 1 ≤ length of list ≤ 10^5
                 list[i] is either 0 or 1
                 Runtime < 1 minute

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


if __name__ == "__main__":
    test_list = [0, 1, 1, 1, 0, 0, 0, 1, 1, 0]
    print(switches(test_list))  # Expected output: 2
