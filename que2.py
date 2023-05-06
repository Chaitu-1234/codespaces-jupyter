def reverse_array(arr):
    n = len(arr)
    for i in range(n//2):
        temp = arr[i]
        arr[i] = arr[n-i-1]
        arr[n-i-1] = temp

arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr)  # Output: [5, 4, 3, 2, 1]
