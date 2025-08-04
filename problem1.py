def three_part_harmony(n, a):
    MOD = 10**9 + 7
    total = sum(a)

    if total % 3 != 0:
        return 0

    target = total // 3
    prefix_sum = 0
    count_target = 0
    ways = 0

    for i in range(n - 1):
        prefix_sum += a[i]

        if prefix_sum == 2 * target:
            ways = (ways + count_target) % MOD
        if prefix_sum == target:
            count_target += 1

    return ways % MOD

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(three_part_harmony(n, a))
