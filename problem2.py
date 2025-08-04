from collections import deque

def max_potholes_removed(n, A, B):
    prefixA = [0] * (n + 1)
    prefixB = [0] * (n + 1)
    suffixA = [0] * (n + 1)
    suffixB = [0] * (n + 1)
    for i in range(n):
        prefixA[i+1] = prefixA[i] + (1 if A[i] == 'X' else 0)
        prefixB[i+1] = prefixB[i] + (1 if B[i] == 'X' else 0)
    for i in range(n-1, -1, -1):
        suffixA[i] = suffixA[i+1] + (1 if A[i] == 'X' else 0)
        suffixB[i] = suffixB[i+1] + (1 if B[i] == 'X' else 0)

    max_removed = 0
    for i in range(n+1):
        if (i == n) or (A[i] != 'X' and B[i] != 'X'):
            max_removed = max(max_removed, prefixA[i] + suffixB[i])
        if (i == n) or (A[i] != 'X' and B[i] != 'X'):
            max_removed = max(max_removed, prefixB[i] + suffixA[i])
    return max_removed

# Input handler
def main():
    n = int(input())
    A = input().strip()
    B = input().strip()
    result = max_potholes_removed(n, A, B)
    print(result)
    
if __name__ == "__main__":
    main()