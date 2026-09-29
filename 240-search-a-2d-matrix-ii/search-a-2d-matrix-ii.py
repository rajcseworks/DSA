class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(nums,target):
            lo = 0
            hi = len(nums)-1
            while lo<=hi:
                mid = (lo+hi)//2
                if nums[mid]==target:
                    return True
                elif nums[mid] < target:
                    lo = mid+1
                else:
                    hi = mid-1
            return False
        for i in matrix:
            bin = binary_search(i,target)
            if bin:
                return True
        return False
