class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        y = str(x)
        y= y[::-1]
        z= str(x) 
        if y==z:
            return True 
        else:
            return False 
        
        
        
        
        
        
        
        
        
# palindrome: 거꾸로 읽어도 제대로 읽는 것과 같은 문장이나 낱말, 숫자, 문자열(sequence of characters) 등