def heapsort(arr):
    build_max_heap(arr)

    end = len(arr) - 1
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i)

        end -= 1
        max_heapify(arr, end, 0)


def build_max_heap(arr):
    for i in range((len(arr) - 1) // 2, -1, -1):
        max_heapify(arr, len(arr) - 1, i)


def max_heapify(arr, end, parent):
    left = 2 * parent + 1
    right = 2 * parent + 2

    if left <= end and right <= end:
        if arr[left] > arr[parent] or arr[right] > arr[parent]:
            if (arr[left] > arr[right]):
                swap(arr, left, parent)
                max_heapify(arr, end, left)
            else:
                swap(arr, right, parent)
                max_heapify(arr, end, right)

    elif left <= end:
        if arr[left] > arr[parent]:
            swap(arr, left, parent)
            max_heapify(arr, end, left)
    else:
        return


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
