class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        hi = len(nums)
        count = 0
        for i in range(hi):
            if k > nums[i]:
                count+=1
        return(count)     
        