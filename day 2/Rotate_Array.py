class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_length = len(nums)
        k = k % nums_length
        break_point = nums_length - k
        rslt = [None] * nums_length
        j = 0
        for i in range(break_point, nums_length):
            rslt[j] = nums[i]
            j = j + 1
        for i in range(0, break_point):
            rslt[j] = nums[i]
            j = j + 1
        for i in range(0, nums_length):
            nums[i] = rslt[i]
            
