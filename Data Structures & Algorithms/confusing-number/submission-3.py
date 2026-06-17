class Solution:
    def confusingNumber(self, n: int) -> bool:
        nums = list(str(n))
        invalidNums = [2,3,4,5,7]
        finalValue = 0
        for i,num in enumerate(nums):
            if num in invalidNums:
                return False
            elif num == '6':
                finalValue +=(9*(10**i))
            elif num == '9':
                finalValue +=(6*(10**i))
            else:
                finalValue += (int(num)*(10**i))
        return finalValue != n