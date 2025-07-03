from collections import deque

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


if __name__ == "__main__":
    print(mirrored_numbers("1001", "1200"))  # Expected output: 2
