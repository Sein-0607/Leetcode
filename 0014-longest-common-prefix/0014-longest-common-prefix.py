class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = "" 
        # print(len(strs[0])) # 6 flower
        for i in range(len(strs[0])):
            contrast = strs[0][i] # f,l,o,w,e,r 반복
            for j in range(1, len(strs)):
                if (i>=len(strs[j])) or (strs[j][i] != contrast):
                    return prefix
       
            prefix += contrast
        
        return prefix
            