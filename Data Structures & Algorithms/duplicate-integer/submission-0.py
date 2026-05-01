class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set(nums)
        print(s)
        print(len(s))
        print(len(nums))

        return not len(nums)==len(s)
        