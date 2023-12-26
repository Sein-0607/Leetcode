class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
    
    # 손코드
    # 1. int로 이루어진 배열 nums의 길이를 구한다.(인덱스 설정을 위해서)
    # 2. two numbers와 target이 같다면,(조건) 그 two numbers의 인덱스를 출력하도록 한다.
        # 2-1. two numbers의 각각의 인덱스를 [i,j]로 정의한다.
        # 2-2. i가 0부터 n-1까지 반복
                    # j가 i+1부터 n까지 반복
        # 2-3. 그렇게 i와 j의 반복문을 돌면, 모든 인덱스 경우의 수를 돌게 된다.
        # 2-4. two numbers의 합이 target과 같다면, [i,j]를 반환하고
        #      그렇지 않다면 빈 [] 리스트를 뱉어낸다.