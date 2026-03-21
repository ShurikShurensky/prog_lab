#--------------1 задача-------------------    
class Solution(object):
        def twoSum(self, nums, target):
            seen = {}

            for i, x in enumerate(nums):
                need = target - x
                if need in seen:
                    return [seen[need], i]
                seen[x] = i

#--------------125 задача-------------------
class Solution:
    def isPalindrome(self, s: str) -> bool:
        t_list = []
        for ch in s:
            if ch.isalnum():
                t_list.append(ch.lower())
        t = "".join(t_list)

        return t == t[::-1]
    
#--------------3 задача-------------------

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        best = 0
        last = {}  # символ -> последний индекс

        for right in range(len(s)):
            ch = s[right]

            if ch in last and last[ch] >= left:
                left = last[ch] + 1

            last[ch] = right
            best = max(best, right - left + 1)
        return best
    
#--------------11 задача-------------------

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        best = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            best = max(best, h * w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best