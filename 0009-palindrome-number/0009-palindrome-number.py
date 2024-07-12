class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        temp=x
        while(x>0):
            p=x%10
            rev=rev*10+p
            x=x//10
        if(rev==temp):
            return True
        else:
            return False