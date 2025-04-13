def linear_search(list, target):
    """returns index of postion, prints number of iterations for each search"""
    iteration = 1
    for i in range(len(list)):
        print('iteration:', iteration)
        if list[i] == target:
            return i
        iteration += 1
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(numbers, 12)
verify(result)
result = linear_search(numbers, 6)
verify(result)
