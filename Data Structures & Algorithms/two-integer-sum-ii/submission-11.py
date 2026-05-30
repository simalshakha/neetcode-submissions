class Solution:
    def twoSum(self, numbers: list[int], target: int) -> numbers[int]:
        l=0
        r=len(numbers)-1
        # print(r)
        while l<=r:
            x=numbers[l]+numbers[r]
            # print([numbers[l],numbers[r]])
            if x<target:
                l=l+1
            elif x>target:
                r=r-1
            else: 
               return [l+1,r+1]
