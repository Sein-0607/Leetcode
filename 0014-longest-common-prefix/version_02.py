class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if len(strs) == 0:
        #     return ""
        
        if len(strs) == 1:
            return strs[0]
        
        end = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[0][i] != strs[j][i]:
                    return strs[0][:end]
            end += 1
        
        return strs[0][:end]
