class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        ans = 0
        is_odd = False
        for f in freq.values():
            if f % 2 == 0:
                ans += f
            else:
                ans += f - 1
                is_odd = True
        if is_odd:
            ans += 1
        return ans
