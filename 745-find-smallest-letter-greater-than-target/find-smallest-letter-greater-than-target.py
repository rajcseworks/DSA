class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        lo = 0
        hi = len(letters)-1
        ans = letters[0]
        while lo<=hi:
            mid = (lo+hi)//2
            if letters[mid] > target:
                ans = letters[mid]
                hi = mid-1
            else:lo = mid+1
        return ans