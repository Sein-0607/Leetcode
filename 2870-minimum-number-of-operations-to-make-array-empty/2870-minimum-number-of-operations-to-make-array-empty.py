class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count_set = Counter(nums)
        output = 0
        
        for count in count_set.values():
            if count == 1:
                return -1

            if count % 3 == 0:
                output += count // 3

            elif count % 3 == 2:
                output += (count // 3) + 1
            
            else:
                output += (count - 1) // 3 + 1

        return output