def max_distance(intervals: list[list[int]]) -> int:
    """
    Calculates the maximum difference between a minimum and a maximum value from different intervals,
    where the minimum and maximum cannot come from the same interval.
    
    Constraints: 2 <= len(intervals) <= 10^5
                 1 <= intervals[i].lengte <= 500
                 -10^4 <= intervals[i][j] <= 10^4
                 intervals[i] is sorted in ascending order
                 Runtime < 1 minute

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

    # If min and max come from the same interval, look for alternatives
    if index_min == index_max:
        # Remove the min and max values from that interval
        min_values.pop(index_min)
        max_values.pop(index_max)

        second_min = min(min_values)
        second_max = max(max_values)

        # Determine max difference considering second min and max values
        difference = max(global_max - second_min, second_max - global_min)
    else:
        difference = global_max - global_min

    return difference

if __name__ == '__main__':
    input_list = [[0, 6], [3, 4], [2, 5], [1, 3]]
    print(max_distance(input_list)) # Expected output: 5
