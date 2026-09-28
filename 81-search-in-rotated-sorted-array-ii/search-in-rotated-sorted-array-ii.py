class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        def binarysearch(lo,hi,target):
            while lo<=hi:
                mid = (lo+hi)//2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    lo = mid+1
                else:
                    hi = mid-1
            return False
        def count_rotation(nums):
            lo = 0
            hi = len(nums)-1

            while lo < hi:
                mid = (lo+hi)//2
                if nums[mid] > nums[hi]:
                    lo = mid+1
                elif nums[mid] < nums[hi]:
                    hi = mid
                else:
                    hi -= 1
            return lo
        count = count_rotation(nums)
        if count == 0:
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    count = i+1
                    break
        if count == 0:
            result = binarysearch(0,len(nums)-1,target)
        else:
            result = binarysearch(0,count-1,target)
            if result == False:
                result = binarysearch(count,len(nums)-1,target)
            else:
                return result
        return result