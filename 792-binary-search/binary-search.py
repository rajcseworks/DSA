class Solution:
    #DONE
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1

        while lo <= hi:
            mid=(lo+hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid-1
            else :
                lo = mid+1
        return -1

nums = [-1,0,3,5,9,12]
target = 9