def containsDupe(nums:[int]):
    freq = {}
    for i in range(len(nums)):
        if nums[i] in freq:
            return True
        freq[nums[i]] = 1
    return False

def containsDupe2(nums:[int]):
    ns = set()
    for i in range(len(nums)):
        if nums[i] in ns:
            return True
        ns.add(nums[i])
    return False

print(containsDupe([1,2,3,1]))
print(containsDupe([1,2,3,4]))
print(containsDupe([1,1,1,3,3,4,3,2,4,2]))

print(containsDupe2([1,2,3,1]))
print(containsDupe2([1,2,3,4]))
print(containsDupe2([1,1,1,3,3,4,3,2,4,2]))
