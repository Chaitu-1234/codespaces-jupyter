def find_pairs(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs

arr = [1, 2, 3, 4, 5]
target = 7
pairs = find_pairs(arr, target)
for pair in pairs:
    print(pair)
