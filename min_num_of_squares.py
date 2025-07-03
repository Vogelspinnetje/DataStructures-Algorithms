import math

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

    return dp[n]


if __name__ == "__main__":
    print(min_num_of_squares(12))  # Expected output: 3
