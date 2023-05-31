def bubbleSort(array):
    condition = 0
    while condition <= len(array):
        for n in range(len(array)-1):
            lowest = min(array[n:])
            lowest_index = array[n:].index(lowest) + n
            if array[n:][0] > array[n:][1]:
                array[n], array[lowest_index] = array[lowest_index], array[n]
        condition += 1
    return array

print("bubbleSort: ", bubbleSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]))

def quickSort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) - 1]
    greater = [c for c in array if c > pivot]
    equal = [c for c in array if c == pivot]
    lesser = [c for c in array if c < pivot]
    return quickSort(lesser) + equal + quickSort(greater)

print("quicksort: ", quickSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]))