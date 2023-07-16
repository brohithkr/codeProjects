def min_operations(n, m, grid):
    row_count = [0] * n
    col_count = [0] * m

    # Count the number of black tiles in each row and column
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                row_count[i] += 1
                col_count[j] += 1

    # Find the maximum count between rows and columns
    max_count = max(max(row_count), max(col_count))

    # Return the sum of the maximum count and the remaining white rows/columns
    return max_count + (n - max_count) + (m - max_count)

# Read input
n, m = map(int, input().split())
grid = [input() for _ in range(n)]

# Calculate and print the minimum number of operations
print(min_operations(n, m, grid))
