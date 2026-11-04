class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        #nums = [1, 2, 4, 6]
        #res = [1, 1, 1, 1]

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            #res = [1, 1, 2, 8]
            prefix *= nums[i]
            #prefix = 8

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            #res = [1, 24, 12, 8]
            postfix *= nums[i]
            #postfix = 48
        return res



        