# LeetCode 875

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)

            if hours <= h:
                res = mid
                right = mid - 1 
            else:
                left = mid + 1 
                
        return res
    
# LeetCode 33

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1


# LeetCode 704

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1

# LeetCode 128

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

# LeetCode 347

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        hash_map = sorted(hash_map, key=lambda x: hash_map[x], reverse=True)
        return hash_map[:k]

# LeetCode 49

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in anagrams:
                anagrams[sorted_s] = []
            anagrams[sorted_s].append(s)
        return list(anagrams.values())