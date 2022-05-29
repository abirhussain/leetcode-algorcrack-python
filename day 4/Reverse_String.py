class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        string_length = len(s)
        left_pointer = 0
        right_pointer = string_length -1 
        tmp = ''
        while left_pointer < right_pointer:
            tmp = s[left_pointer]
            s[left_pointer] = s[right_pointer]
            s[right_pointer] = tmp
            left_pointer = left_pointer + 1
            right_pointer = right_pointer - 1
        
            
        
