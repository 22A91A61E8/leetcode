class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        
        for i in s:
            l=[]
            if i==')':
                while stack and stack[-1]!='(':
                    x=stack.pop()
                    l.append(x)
                if stack and stack[-1]=='(':
                    stack.pop()
                for i in l:
                    stack.append(i)
            else:
                stack.append(i)
        return ''.join(stack)