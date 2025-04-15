def recursive_binary_search(list, target):
    if len(list) == 0:
        return None
    else:
        midpoint = len(list)//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


def recursive_binary_search_no_splice(arr, target, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    if start > end:
        return False

    mid = (start + end) // 2

    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return recursive_binary_search_no_splice(arr, target, mid + 1, end)
    else: 
        return recursive_binary_search_no_splice(arr, target, start, mid -1)


def verify(result):
    print("Target found:", result)

number = list(range(10))

result = recursive_binary_search(number, 4)
verify(result)


result = recursive_binary_search_no_splice(number, 4)
verify(result)