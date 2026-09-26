class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = (lo + hi)//2
            if mid > 0 and nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] < nums[hi]:
                hi = mid-1
            else:
                lo = mid+1
        return nums[0]