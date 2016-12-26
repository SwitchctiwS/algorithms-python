def quicksort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot - 1)
        quicksort(arr, pivot + 1, right)


def partition(arr, left, right):
    pivot = arr[right]
    less = left

    for greater in range(left, right):
        if arr[greater] <= pivot:
            swap(arr, less, greater)
            less += 1

    swap(arr, less, right)
    return less


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
