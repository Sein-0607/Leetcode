class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # nums.sort() #sort 사용하는 버전
        # min = nums[0]*nums[1]
        # max = nums[-1]*nums[-2]
        # return max - min
        
        # sort 사용 안하는 버전
        a = max(nums); nums.remove(a)
        b = max(nums)
        c = min(nums); nums.remove(c)
        d = min(nums)
        
        return (a * b) - (c * d)