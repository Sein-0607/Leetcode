# SET 이용해서 푸는 방법

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_set = set()
        
        i = 0  

        for num in nums:
            if num not in unique_set:
                unique_set.add(num)
                nums[i] = num
                i += 1

        return i​
