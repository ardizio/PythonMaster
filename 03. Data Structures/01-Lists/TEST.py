def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



my_list = [64, 34, 25, 12, 22, 11, 90]

# Call the bubble_sort function to sort the list in place
bubble_sort(my_list)

# The sorted list is now in my_list
print(my_list)