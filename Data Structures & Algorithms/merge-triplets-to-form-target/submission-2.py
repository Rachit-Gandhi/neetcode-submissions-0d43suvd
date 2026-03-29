class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # target should be maxes of respective positions of all triplets chosen
        maxtriplet = [0,0,0]
        for triplet in triplets:
            isValid = True
            for i in range(0,3):
                if triplet[i]>target[i]:
                    print(triplet[i],target[i])
                    isValid = False
            #print(triplet,isValid)
            if isValid:        
                for i in range(0,3):
                    maxtriplet[i] = max(maxtriplet[i],triplet[i])
        #print(maxtriplet)
        return maxtriplet == target
        