def insertionsort(arr):
    for i in range(len(arr) - 1):
        insert(arr, i + 1)


def insert(arr, key_index):
    for i in range(key_index):
        if arr[key_index] < arr[i]:
            key = arr[key_index]

            for j in range(key_index, i, -1):
                arr[j] = arr[j - 1]

            arr[i] = key
