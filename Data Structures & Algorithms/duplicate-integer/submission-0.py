class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # dumb way
        # for i in range(len(nums)-1):
        #   for j in range(i+1,len(nums)):
        #        if nums[j] == nums[i]:
        #            return False
        # return True

        # smart way HashSet
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                return True
            else:
                visited.add(nums[i])
        return False