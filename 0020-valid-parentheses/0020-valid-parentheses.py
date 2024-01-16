class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')', '{':'}','[':']'}
        space = [] # open 괄호 저장공간

        for bracket in s:
            if bracket in pairs:
                space.append(bracket)
            else:
                if len(space) < 1:
                    return False

                if (bracket == ')' and space.pop() != '(') or \
                    (bracket == '}' and space.pop() != '{') or \
                    (bracket == ']' and space.pop() != '['):
                    return False
                                
        return len(space) == 0
