def heap_sort(arr):
    size = len(arr)

    for i in range(size, 0, -1):
        heapify(arr, size, i)

    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def heapify(array, n, i):
    maximum = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[i] < array[left]:
        maximum = left

    if right < n and array[maximum] < array[right]:
        maximum = right

    if maximum != i:
        array[i], array[maximum] = \
            array[maximum], array[i]

        heapify(array, n, maximum)

my_array = [100, 84, 71, 60, 23, 12, 29, 1, 37, 4]

heap_sort(my_array)
print("Sorted array: ", my_array)