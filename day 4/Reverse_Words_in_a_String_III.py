class Solution:
    def reverseWords(self, s: str) -> str:
        s_length = len(s)
        right_pointer = s_length - 1
        res = ""
        word = ""
        for i in range(s_length-1, -1, -1):
            if s[i] != " ":
                word = word + s[i]
            else:
                res = " "+ word + res
                word = ""
        
        return word+res
            
