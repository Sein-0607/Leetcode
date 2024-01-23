class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 1:
        #     return 1
    
        arr = [0] * 46
        arr[1] = 1
        arr[2] = 2
 
        for i in range(3,n+1):
            arr[i] = arr[i-1] + arr[i-2]
        
        return arr[n]

# #손 코드
#     1. 크기가 46인 배열 arr를 생성하여 중간 결과 저장한다.
#     2. arr[i]: i번째 계단까지 도달하는 고유한 방법의 수
#     3. 배열의 처음 두 요소는 1과 2로 미리 지정해놓는다. arr[1], arr[2]
#     4. for문 사용하여 arr을 3번째 계단부터 n번째 계단까지 
#     5. 각 단계에서의 값은 이전 두 단계의 합
#     6. 총 단계의 수를 반환한다.