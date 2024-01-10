class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count_set = {}
        output = 0
        
        for num in nums:
            if num in count_set:
                count_set[num] += 1
            else:
                count_set[num] = 1
        # print(count_set) {2: 4, 3: 3, 4: 2}

        for count in count_set.values():
            if count == 1:
                return -1
            output += floor((count + 2) / 3)
       
        return output
