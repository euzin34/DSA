import sys
input = sys.stdin.readline

n, p = map(int, input().split())
events = []

if n == 0:
    print(p + 1)
    exit()

for _ in range(n):
    x, r = map(int, input().split())
    start = max(0, x - r)
    end = min(p + 1, x + r + 1)
    events.append((start, 1))  
    events.append((end, -1))   

events.sort()

max_dark_length = 0
current_lamp_count = 0
prev_coord = 0
i = 0

if events and events[0][0] > 0 and 0 <= p:
    if current_lamp_count != 1:
        dark_length = min(events[0][0], p + 1) - 0
        max_dark_length = max(max_dark_length, dark_length)

while i < len(events):
    coord = events[i][0]
    net_change = 0
    while i < len(events) and events[i][0] == coord:
        net_change += events[i][1]
        i += 1
    
    if current_lamp_count != 1 and prev_coord < coord and prev_coord <= p:
        dark_length = min(coord, p + 1) - prev_coord
        max_dark_length = max(max_dark_length, dark_length)
    
    current_lamp_count += net_change
    prev_coord = coord
if current_lamp_count != 1 and prev_coord <= p:
    dark_length = p + 1 - prev_coord
    max_dark_length = max(max_dark_length, dark_length)

print(max_dark_length)

def max_dark_segment(n, p, lamps):
    diff = [0] * (size)

    for x, r in lamps:
        l = max(0, x - r)
        r_ = min(p, x + r)
        diff[l] += 1
        if r_ + 1 < size:
            diff[r_ + 1] -= 1
    coverage = [0] * (p + 1)
    curr = 0
    for i in range(p + 1):
        curr += diff[i]
        coverage[i] = curr

    max_dark = 0
    curr_dark = 0
    for i in range(p + 1):
        if coverage[i] != 1:
            curr_dark += 1
            max_dark = max(max_dark, curr_dark)
        else:
            curr_dark = 0
    return max_dark

def run_samples():
    samples = [
        (1, 7, [(2, 0)]),
        (4, 4, [(1, 2), (3, 0), (0, 2), (3, 0)]),
    ]
    for idx, (n, p, lamps) in enumerate(samples, 1):
        print(f"Testcase {idx} Input:")
        print(f"{n} {p}")
        for x, r in lamps:
            print(f"{x} {r}")
        print(f"\nTestcase {idx} Output:")
        print(max_dark_segment(n, p, lamps))
        print()

if __name__ == "__main__":
    run_samples()