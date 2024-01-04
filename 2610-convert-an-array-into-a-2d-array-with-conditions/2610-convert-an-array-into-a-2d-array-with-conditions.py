class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        answer = [] # 2d array 생성
         
        for num in nums:
            if len(answer) == 0:
                answer.append([num])
                continue

            inserted = False
            for row in range(0, len(answer)):
                exist = False

                for col in range(0, len(answer[row])):
                    if answer[row][col] == num:
                        exist = True
                        break
                
                if exist == False:
                    answer[row].append(num)
                    inserted = True
                    break

            if inserted == False:
                answer.append([num]) # insert new row

        print(answer)

        return answer