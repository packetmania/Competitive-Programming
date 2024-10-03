# https://people.bath.ac.uk/masjhd/2016.NWERC/
# https://open.kattis.com/problems/freeweights

def ok(p, n, weights):
    lsv = 0  # Last saved unmatched weight
    for i in range(n):
        if weights[i] > p:
            if lsv != 0:
                if lsv != weights[i]:
                    return False
                else:
                    lsv = 0  # Found a pair
            else:
                lsv = weights[i]  # Save unmatched weight
    if lsv != 0:
        return False  # Unmatched weight remaining
    return True

def find_min_max_lift_weight(n, a, b):
    l = 0
    r = int(1e9 + 10)
    while l < r:
        m = (l + r) // 2
        if ok(m, n, a) and ok(m, n, b):
            r = m  # Possible to arrange with max weight m
        else:
            l = m + 1  # Need a larger max weight
    return l

# Read input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Find and print the minimal maximum weight to lift
result = find_min_max_lift_weight(n, a, b)
print(result)
