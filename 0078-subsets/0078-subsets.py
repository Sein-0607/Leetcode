class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
# 중복허용
#         output =[[]]
#         for i in nums:
#             for j in nums:
#                 for k in nums:
#                     subset = [i, j, k]
#                     output.append(subset)

#         return output


        output = [[]] 

        for num in nums:
            new_subsets = []  # 각 num에 대한 새로운 부분집합을 저장할 리스트 초기화
            for curr in output:
                subset = curr + [num]
                new_subsets.append(subset)
            output += new_subsets  # 새로운 부분집합들을 기존 output에 추가

        return output
