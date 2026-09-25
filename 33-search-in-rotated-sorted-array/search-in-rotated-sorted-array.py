class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binary_search(lo,hi,target):
            while lo <= hi:
                mid = (lo + hi)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    hi = mid-1
                else :
                    lo = mid+1
            return -1
        def count_rotation(nums):
            lo = 0
            hi = len(nums)-1

            while lo <= hi:
                mid = (lo + hi)//2
                if mid > 0 and nums[mid] < nums[mid-1]:
                    return mid
                elif nums[mid] < nums[hi]:
                    hi = mid-1
                else:
                    lo = mid+1
            return 0
        if count_rotation(nums) == 0:
            index = binary_search(0,len(nums)-1,target)
        else:
            index = binary_search(0,count_rotation(nums)-1,target)
            if index == -1:
                index = binary_search(count_rotation(nums),len(nums)-1,target)
        return index if index != -1 else -1