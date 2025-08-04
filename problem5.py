from math import gcd
from functools import reduce


N, Q = map(int, input().split())
A = list(map(int, input().split()))

prefix_gcd = [0] * N
prefix_gcd[0] = A[0]
for i in range(1, N):
    prefix_gcd[i] = gcd(prefix_gcd[i-1], A[i])


suffix_gcd = [0] * N
suffix_gcd[-1] = A[-1]
for i in range(N-2, -1, -1):
    suffix_gcd[i] = gcd(suffix_gcd[i+1], A[i])

for _ in range(Q):
    L, R = map(int, input().split())
    L, R = L-1, R-1 
    
    if L == 0:
        result = suffix_gcd[R+1] if R+1 < N else prefix_gcd[L-1]

    elif R == N-1:
        result = prefix_gcd[L-1]

    else:
        result = gcd(prefix_gcd[L-1], suffix_gcd[R+1])
    
    print(result)