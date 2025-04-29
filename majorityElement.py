def majorityElement(nums):
    canidate = None
    count = 0

    for num in nums:
        if count == 0:
            canidate = num

        count += 1 if canidate == num else -1

    return canidate

print(majorityElement([2,2,1,1,1,2,2]))