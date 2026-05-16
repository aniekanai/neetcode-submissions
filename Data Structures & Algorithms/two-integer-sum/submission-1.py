class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Input: 
        # nums = [3,4,5,6], target = 7
        # declare an empty list
        A = []

        #append all elements and thir indices to the empty list
        for i, num in enumerate(nums):
            A.append([num, i])

        # A = [[3, 0],[4, 1],[5, 2],[6, 3]]

        # sort new array
        A.sort()
        # A = [[3, 0],[4, 1],[5, 2],[6, 3]]
        #traget = 7

        i, j = 0, len(nums) - 1

        while i < j:
            cur = A[i][0] + A[j][0]

            if cur == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []



        