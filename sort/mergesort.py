def mergesort(arr, start, end):
    if start < end:
        middle = (start + end) // 2

        mergesort(arr, start, middle)
        mergesort(arr, middle + 1, end)

        merge(arr, start, middle, end)


def merge(arr, start, middle, end):
    left = []
    right = []

    for i in range(start, middle + 1):
        left.append(arr[i])

    for i in range(middle + 1, end + 1):
        right.append(arr[i])

    arr_iter = start
    left_iter = 0
    right_iter = 0

    while left_iter < len(left) and right_iter < len(right):
        if (left[left_iter] < right[right_iter]):
            arr[arr_iter] = left[left_iter]
            left_iter += 1

        else:
            arr[arr_iter] = right[right_iter]
            right_iter += 1

        arr_iter += 1

    while left_iter < len(left):
        arr[arr_iter] = left[left_iter]
        arr_iter += 1
        left_iter += 1

    while right_iter < len(right):
        arr[arr_iter] = right[right_iter]
        arr_iter += 1
        right_iter += 1
