class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # nums = [1, 2, 4, 6]
        #           0   1
        # output = [48,  24, ]

        # pre_prod_nums = [1, 1, 2, 8 ]

        # post_prod_nums [48, 24, 6, 1]
        
        output = [1] * (len(nums))
        #res = [1, 1, 1, 1]

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

            #res = [1, 1, 2, 8]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output