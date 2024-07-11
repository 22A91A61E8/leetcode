class Solution:
    def reverseParentheses(self, s: str) -> str:
        st=[]
        l=''
        for i in s:
            if i=='(':
                st.append(l)
                l=''
            elif i.isalpha():
                l=l+i
            elif i==')':
                l=l[::-1]
                l=st.pop()+l
        return l
                
                
                
                