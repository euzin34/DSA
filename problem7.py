n = int(input())
b = list(map(int, input().split()))


left_max = [0] * n 
right_max = [0] * n  


left_max[0] = b[0]
for i in range(1, n):
    left_max[i] = max(left_max[i-1], b[i] + i)

right_max[n-1] = b[n-1] - (n-1)
for i in range(n-2, -1, -1):
    right_max[i] = max(right_max[i+1], b[i] - i)


max_value = float('-inf')
for i in range(1, n-1):  
        value = left_max[i-1] + b[i] + right_max[i+1]
        max_value = max(max_value, value)

print(max_value)