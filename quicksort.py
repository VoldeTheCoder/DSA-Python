def partition(arr, low, high):
    pivotIndex = low
    storeIndex = pivotIndex + 1
    i = low + 1
    while i<=high:
        if arr[i] < arr[pivotIndex]:
            arr[i], arr[storeIndex] = arr[storeIndex], arr[i]
            storeIndex+=1
        i+=1
    arr[pivotIndex], arr[storeIndex-1] = arr[storeIndex-1], arr[pivotIndex]
    return storeIndex - 1


def quick_sort(arr, low, high):
    if low < high:
        partitionIndex = partition(arr, low, high)

        quick_sort(arr, low, partitionIndex - 1)
        quick_sort(arr, partitionIndex + 1, high)

arr = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
quick_sort(arr, 0, len(arr)-1)
print(arr)