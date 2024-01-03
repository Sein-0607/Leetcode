class Solution:
    def romanToInt(self, s: str) -> int:
        set = {"I":1,
               "V":5,
               "X":10,
               "L":50,
               "C":100,
               "D":500,
               "M":1000}
        
        num = 0
        
        for i in range(0, len(s)-1):
            if set[s[i]] < set[s[i+1]]:
                num -= set[s[i]]
            else:
                num += set[s[i]]
        num += set[s[-1]]
        return num
        
        
# 대원칙: 큰수 -> 작은수 
# EX) "MXI" => 1000 10 1 ==> 1011

# 만약, 작은수 -> 큰수 (순서로 적혀있다면, 앞의 작은수는 "음수")
# EX) "CMXCVIII" 
# CM 100 1000 (작은 수가 앞이므로, 100은 음수처리 즉, 1000-100 = 900)
# XC 10 100 (100-10=90)
# VII => 5+1+1+1 =8

# result = 998
