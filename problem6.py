def diamond_sum(i, j, r, n, grid):

    total = grid[i][j] 
    if r >= 1:
  
        if i - 1 >= 0:
            total += grid[i-1][j]  # Up
        if i + 1 < n:
            total += grid[i+1][j]  # Down
        if j - 1 >= 0:
            total += grid[i][j-1]  # Left
        if j + 1 < n:
            total += grid[i][j+1]  # Right
    return total


n = int(input())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)


prefix = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix[i][j] = (prefix[i-1][j] + prefix[i][j-1] - 
                       prefix[i-1][j-1] + grid[i-1][j-1])

# Finding maximum diamond sum
max_sum = float('-inf')
for i in range(n):
    for j in range(n):
        max_r = min(i, n-1-i, j, n-1-j)
        for r in range(max_r + 1):
            current_sum = diamond_sum(i, j, r, n, grid)
            max_sum = max(max_sum, current_sum)
            
#Unfinished couldnot do