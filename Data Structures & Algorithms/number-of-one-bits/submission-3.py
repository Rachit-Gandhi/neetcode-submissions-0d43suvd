class Solution:
    def hammingWeight(self, n: int) -> int:
        count= 0
        for i in range(33):
            if n//2**(32-i)>=1:
                count+=1
                n = n - 2**(32-i)

        return count


        