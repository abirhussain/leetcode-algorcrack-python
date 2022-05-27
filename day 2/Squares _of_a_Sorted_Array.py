class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        rslt = [None] * nums_length
        left_pointer = 0
        right_pointer = nums_length - 1
        rslt_pointer = right_pointer
        while rslt_pointer >= 0:
            left_square = nums[left_pointer] * nums[left_pointer]
            right_square = nums[right_pointer] * nums[right_pointer]
            if left_square > right_square:
                rslt[rslt_pointer] = left_square
                left_pointer = left_pointer + 1
                rslt_pointer = rslt_pointer - 1
            else:
                rslt[rslt_pointer] = right_square
                right_pointer = right_pointer - 1
                rslt_pointer = rslt_pointer - 1
        return rslt
                
        
