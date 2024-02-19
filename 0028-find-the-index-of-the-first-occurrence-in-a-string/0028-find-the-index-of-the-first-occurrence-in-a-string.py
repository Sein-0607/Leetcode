class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        need_range = h-n+1

        for i in range(0, need_range):
            if haystack[i:i+n] == needle:
                return i
        return -1

# 알고리즘 풀이

# 1) 반복문 설정 (haystack을 순회한다.)
# - needle의 길이만큼 haystack의 끝에서 멈춘다.
# - len(haystack) - len(needle) + 1 을 범위의 끝으로 설정한다.
# 이렇게 되면, needle이 haystack의 남은 부분보다 길어질 수 있는 범위를 넘어서지 않게끔 한다.

# for i in range(0, len(haystack)-len(needle)+1)

# ex) haystack = hello / needle = ll
# len(haystack) = 5
# len(needle) = 2
# len(haystack) - len(needle) + 1 = 5-2+1 = 4

# for i in range(0,4)
# --> haystack의 가능한 시작 인덱스가 0,1,2,3 인 경우를 확인하겠다.
# i = 0 --> "he"
# i = 1 --> "el"
# i = 2 --> "ll" -- needle과 일치함. (return index 후 종료)
# i = 3 --> "lo"

        