class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # initialize the array with 1
        ans = [1] * n

        # multiply all the preffix with each array element 
        preffix = 1
        for i in range(n):
            ans[i]= preffix
            preffix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans