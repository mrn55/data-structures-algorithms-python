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

big_int = 100000000
print(f"creating large int array: {big_int}")
int_array = list(range(100000000))
print(f"created large int array: {big_int}")
result = binary_search(int_array, 99999999)
verify(result)


#https://www.youtube.com/watch?v=s2Yyk3qdy3o
def treeSum(root):
    if root is None:
        return 0
    else:
        leftSum = treeSum(root.left)
        rightSum = treeSum(root.right)
        return root.data + leftSum + rightSum