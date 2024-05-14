from typing import List, Dict, Tuple, Set

# 1. 1D Array DP (Fibonacci)


def fib(n: int) -> int:
    """
    Fibonacci sequence using 1D array dynamic programming.

    Assumption: n is a non-negative integer.
    Type Annotations:
        n: int - Input integer.
    Time Complexity: O(n)
    Space Complexity: O(n)
    Trick: Use memoization to store previously computed values.
    """
    if n <= 1:
        return n
    memo = [0] * (n + 1)
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]

# 2. 2D Array DP (Grid Traveler)


def grid_traveler(m: int, n: int) -> int:
    """
    Grid traveler using 2D array dynamic programming.

    Assumption: m and n are non-negative integers.
    Type Annotations:
        m: int - Number of rows.
        n: int - Number of columns.
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    Trick: Use memoization to store previously computed values.
    """
    memo = [[0] * (n + 1) for _ in range(m + 1)]
    memo[1][1] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            memo[i][j] += memo[i - 1][j] + memo[i][j - 1]
    return memo[m][n]

# 3. Knapsack Problem (0/1)


def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    """
    0/1 Knapsack problem using dynamic programming.

    Assumption: weights and values have the same length, and capacity is a non-negative integer.
    Type Annotations:
        weights: List[int] - List of item weights.
        values: List[int] - List of item values.
        capacity: int - Knapsack capacity.
    Time Complexity: O(n * capacity) where n is the number of items.
    Space Complexity: O(n * capacity)
    Trick: Use memoization to store previously computed values.
    """
    n = len(weights)
    memo = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                memo[i][j] = max(memo[i - 1][j], values[i - 1] +
                                 memo[i - 1][j - weights[i - 1]])
            else:
                memo[i][j] = memo[i - 1][j]
    return memo[n][capacity]

# 4. Longest Common Subsequence (LCS)


def lcs(X: str, Y: str) -> int:
    """
    Longest Common Subsequence (LCS) using dynamic programming.

    Assumption: X and Y are strings.
    Type Annotations:
        X: str - First string.
        Y: str - Second string.
    Time Complexity: O(m * n) where m and n are the lengths of the input strings.
    Space Complexity: O(m * n)
    Trick: Use memoization to store previously computed values.
    """
    m, n = len(X), len(Y)
    memo = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                memo[i][j] = memo[i - 1][j - 1] + 1
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
    return memo[m][n]

# 5. Coin Change Problem


def coin_change(coins: List[int], amount: int) -> int:
    """
    Coin change problem using dynamic programming.

    Assumption: coins is a list of positive integers, and amount is a non-negative integer.
    Type Annotations:
        coins: List[int] - List of coin denominations.
        amount: int - Total amount to make change for.
    Time Complexity: O(n * amount) where n is the number of coins.
    Space Complexity: O(amount)
    Trick: Use memoization to store previously computed values.
    """
    memo = [float('inf')] * (amount + 1)
    memo[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            memo[i] = min(memo[i], memo[i - coin] + 1)
    return memo[amount] if memo[amount] != float('inf') else -1


# Example usage of all functions:
if __name__ == "__main__":
    # 1. Fibonacci
    print("Fibonacci:", fib(5))  # Output: 5

    # 2. Grid Traveler
    print("Grid Traveler:", grid_traveler(3, 3))  # Output: 6

    # 3. Knapsack Problem
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    print("Knapsack Problem:", knapsack(weights, values, capacity))  # Output: 7

    # 4. Longest Common Subsequence (LCS)
    X = "ABCBDAB"
    Y = "BDCAB"
    print("Longest Common Subsequence (LCS):", lcs(X, Y))  # Output: 4

    # 5. Coin Change Problem
    coins = [1, 2, 5]
    amount = 11
    print("Coin Change Problem:", coin_change(coins, amount))  # Output: 3
