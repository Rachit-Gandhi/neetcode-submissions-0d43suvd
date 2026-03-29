class Solution:
    def hammingWeight(self, n: int) -> int:
        binaryArray = []
        for i in range(33):
            if n//2**(32-i)>=1:
                binaryArray.append(1)
                n = n - 2**(32-i)
            else:
                binaryArray.append(0)

        return sum(binaryArray)


        