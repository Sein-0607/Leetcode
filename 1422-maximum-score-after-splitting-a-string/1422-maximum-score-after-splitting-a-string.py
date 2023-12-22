class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        cases = []
        slen = len(s)
        for i in range(0,slen):
            L = s[:i]
            R = s[i:]
            if L and R:
                score = L.count('0') + R.count('1')
                max_score = max(score, max_score)
        return max_score