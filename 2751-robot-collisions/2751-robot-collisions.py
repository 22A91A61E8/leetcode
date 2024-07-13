class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        tmp = []
        for i in range(len(healths)):
            tmp.append([positions[i], healths[i], directions[i], i])
        tmp.sort()
        for pos, health, direction, idx in tmp:
            stack.append((health, direction, idx))
            while len(stack) > 1:
                if stack[-1][1] == "L" and stack[-2][1] == "R":
                    left, right = stack.pop(), stack.pop()
                    if left[0] > right[0]:
                        stack.append((left[0]-1, left[1], left[2]))
                    elif right[0] > left[0]:
                        stack.append((right[0]-1, right[1], right[2]))
                else:
                    break
        stack.sort(key=lambda x:x[2]) 
        return map(lambda x:x[0], stack)