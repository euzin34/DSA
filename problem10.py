def solve_spices_box(weights):
    n = len(weights)
    target = 250
    total = sum(weights)

    # Quick check
    if total != 3 * target:
        print("NO")
        return

    # Sort descending for better pruning
    weights.sort(reverse=True)

    groups = [[], [], []]
    sums = [0, 0, 0]
    found = [False]  # mutable flag for result

    def backtrack(index):
        if found[0]:
            return True  # already found a valid configuration
        if index == n:
            # Check if all groups sum to target
            if all(s == target for s in sums):
                found[0] = True
                return True
            return False

        for i in range(3):
            if sums[i] + weights[index] <= target:
                # Place in group i
                groups[i].append(weights[index])
                sums[i] += weights[index]

                # Recurse
                if backtrack(index + 1):
                    return True

                # Backtrack (remove)
                groups[i].pop()
                sums[i] -= weights[index]

            # Optimization: avoid putting same item into empty groups repeatedly
            if sums[i] == 0:
                break

        return False

    if backtrack(0):
        print("YES")
        for g in groups:
            print(*g)
    else:
        print("NO")


# ---- Driver Code ----
if __name__ == "__main__":
    n = int(input().strip())
    weights = list(map(int, input().split()))
    solve_spices_box(weights)
