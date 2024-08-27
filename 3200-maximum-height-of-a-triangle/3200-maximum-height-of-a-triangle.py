class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def helper(red,blue):
            h = 1
            while True:
                if h%2 == 1:
                    if red>=h:
                        red-=h
                    else:
                        break
                else:
                    if blue>=h:
                        blue-=h
                    else:
                        break
                h+= 1
            return h-1
        return max(helper(red,blue),helper(blue,red))