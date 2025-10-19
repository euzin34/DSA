import sys
# Set the recursion limit higher for potentially deep calls in a large number of test cases
sys.setrecursionlimit(10**6)

def power(base, exp, mod):

    res = 1
    base %= mod
    
    while exp > 0:
        # If exp is odd, multiply base with the result
        if exp % 2 == 1:
            res = (res * base) % mod
        
        # exp must be even now
        exp //= 2
        base = (base * base) % mod
        
    return res

def solve():

    try:
        # Fast input reading
        input = sys.stdin.read
        data = input().split()
    except Exception:
        # Handle case where no data is provided (e.g., in some online judges' environments)
        return

    if not data:
        return

    MOD = 10**9 + 7
    
    # The first element is the number of test cases t
    t = int(data[0])
    
    # The remaining elements are the values of n
    results = []
    
    # Process all test cases
    for i in range(1, t + 1):
        n = int(data[i])
        
        # Calculate 2^n mod MOD
        two_pow_n = power(2, n, MOD)
        
        result = (two_pow_n - 2 + MOD) % MOD
        
        results.append(str(result))
    
    # Print all results separated by newlines
    sys.stdout.write('\n'.join(results) + '\n')

# Execute the main function
solve()
