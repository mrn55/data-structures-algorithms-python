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

def verify(result):
    print("Target found:", result)

number = list(range(10))

result = recursive_binary_search(number, 4)
verify(result)
