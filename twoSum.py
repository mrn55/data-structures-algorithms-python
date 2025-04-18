def twoSum(arr, target):
    hm = {}
    for i in range(len(arr)):
        if target - arr[i] in hm:
            return [hm.get(target-arr[i]), i]
        else:
            hm[arr[i]] = i

def twoSum2(arr, target):
    hm = {}
    for i, n in enumerate(arr):
        diff = target - n
        if diff in hm:
            return [hm[diff], i]
        hm[n] = i

print(twoSum([2, 7, 11, 15], 9))
print(twoSum2([2, 7, 11, 15], 9))
