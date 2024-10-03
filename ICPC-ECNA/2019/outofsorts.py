# https://vjudge.net/problem/Kattis-outofsorts
# https://icpc-ecna.ysu.edu/PastResults/2019/problemset.html

# Function to perform binary search on an unsorted sequence
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True  # Return True if the element is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False  # Return False if the element is not found


# Function to count the number of values that can be found
# using binary search without sorting
def count_searchable_values(sequence):
    count = 0
    for value in sequence:
        if binary_search(sequence, value):
            count += 1
    return count


n, m, a, c, x0 = map(int, input().split())

# Generate the sequence using the original formula
sequence = [x0]
for i in range(1, n + 1):
    # Use the distributive property modulo operation to speed up
    next_x = ((a % m) * (sequence[-1] % m) + c % m) % m
    sequence.append(next_x)

print(count_searchable_values(sequence[1:]))
