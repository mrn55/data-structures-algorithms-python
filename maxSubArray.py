class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

    def maxSubArraySeeSlice(self, nums: list[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        start = end = temp_start = 0

        for i in range(len(nums)):
            if curSum < 0:
                curSum = 0
                temp_start = i # start a new sub array from here (for see slice)
            curSum += nums[i]

            if curSum > maxSub:
                maxSub = curSum
                start = temp_start
                end = i

        print(nums[start:end+1]) # see slice, the end+1 because whe taking a slice end is not inclusive
        return maxSub

sol = Solution()
result = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(result)




sol = Solution()
result = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(result)
