    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1
        while left_pointer < right_pointer:
            tmp = numbers[left_pointer] + numbers[right_pointer]
            if tmp == target:
                return [left_pointer + 1, right_pointer+1]
            elif tmp > target:
                right_pointer -= 1
            else:
                left_pointer += 1
