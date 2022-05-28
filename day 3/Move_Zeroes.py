class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_length = len(nums)
        if nums_length == 1:
            return
        left_pointer = -1
        right_pointer = 0
        for right_pointer in range(0, nums_length):
            if nums[right_pointer] != 0:
                left_pointer = left_pointer + 1
                nums[left_pointer] = nums[right_pointer]
            right_pointer = right_pointer + 1
        for i in range(left_pointer + 1, nums_length):
            nums[i] = 0
            
