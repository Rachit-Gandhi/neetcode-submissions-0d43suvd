class Solution:
    def confusingNumber(self, n: int) -> bool:
        nums = list(str(n))
        valid_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        finalValue = 0
        for i, num in enumerate(nums):
            if num not in valid_map:
                return False
            finalValue += int(valid_map[num]) * (10 ** i)
        return finalValue != n