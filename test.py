def reverse(t):
    n = ""
    for i in t:
        n = i + n
    return n

arr = "qwerasdfzxcv"
arr = reverse(arr)
print(arr)
