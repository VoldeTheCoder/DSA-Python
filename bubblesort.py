def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y

def bubble_sort(arr):
    last_index = len(arr) - 1
    while last_index > 1:
        for i in range(last_index):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = swap(arr[i], arr[i+1])
        last_index-=1
    print(arr)

bubble_sort([1, 3, 9, 20, 25, 6, 21, 14])
