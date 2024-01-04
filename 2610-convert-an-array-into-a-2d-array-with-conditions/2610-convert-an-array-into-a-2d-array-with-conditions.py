class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = [] # 2d array 생성

        answer.append([nums[0]])
        prev = nums[0]
        row = 0

        # print('sort : ', nums)

        for i in range(1, len(nums)):
            if prev != nums[i]:
                row = 0
                answer[row].append(nums[i])
                prev = nums[i]
                continue
            
            # else
            row += 1
            if len(answer) <= row:
                answer.append([nums[i]])
            else:
                answer[row].append(nums[i])


        # print(answer)

        return answer