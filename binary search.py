def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    while low <= high:
        mid = (low + high)//2
        if input_array[mid] < value:
            low = mid + 1
        elif input_array[mid] == value:
            return mid
        else:
            high = mid - 1
    return -1


input_array = [2, 4, 5 ,6, 12, 14, 15, 20]
print(len(input_array))
print(binary_search(input_array, 15))