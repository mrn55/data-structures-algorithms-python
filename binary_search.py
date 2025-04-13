def binary_search(list, target):
    """implements binary search, rememerb input needs to be sorted, prints iterations"""
    first = 0
    last = len(list) - 1

    iteration = 1
    while first <= last:
        print('iteration:', iteration)
        midpoint = (first + last) // 2
        
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

        iteration += 1

    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = binary_search(numbers, 12)
verify(result)
result = binary_search(numbers, 6)
verify(result)

int_array = list(range(1000000))
result = binary_search(int_array, 9999)
verify(result)
