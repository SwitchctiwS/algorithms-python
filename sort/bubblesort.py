def bubblesort(arr):
    for i in range(len(arr) - 1, 0, -1):
        swapped = False

        for j in range(i):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
                swapped = True

        if not swapped:
            return


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
