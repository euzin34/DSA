def max_subarray_sum(arr, target):

    max_ending_here = 0
    max_so_far = float('-inf')
    
    for num in arr:
        max_ending_here = max(0, max_ending_here + num)
        if max_ending_here > target:
            max_ending_here = 0 
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far if max_so_far != float('-inf') else target

def can_achieve_sum(matrix, n, m, target):
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix[i][j] = (prefix[i-1][j] + prefix[i][j-1] - 
                          prefix[i-1][j-1] + matrix[i-1][j-1])
    
    # Checking all possible row pairs
    for r1 in range(1, n + 1):
        for r2 in range(r1, n + 1):

            col_sums = []
            for c in range(1, m + 1):
                sum_rect = (prefix[r2][c] - (prefix[r1-1][c] if r1 > 1 else 0) - 
                          (prefix[r2][c-1] if c > 1 else 0) + 
                          (prefix[r1-1][c-1] if r1 > 1 and c > 1 else 0))
                col_sums.append(sum_rect)
            
            # Find max subarray sum <= target
            max_sum = max_subarray_sum(col_sums, target)
            if max_sum <= target and max_sum != float('-inf'):
                return True
    return False

n, m, K = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

min_element = min(min(row) for row in matrix)


left = min_element
right = K  
result = -1

while left <= right:
    mid = (left + right) // 2
    if can_achieve_sum(matrix, n, m, mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1
