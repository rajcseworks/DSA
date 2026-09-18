# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n):
        i = 1
        j = n
        while (i < j):
            mid = (i+j) // 2
            if (isBadVersion(mid)):
                j = mid       # keep track of the leftmost bad version
            else:
                i = mid + 1   # the one after the rightmost good version
        return i
        
        