class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a = []
        do = {"+":lambda x,y:x+y, "-":lambda x,y:x-y, "*": lambda x,y:x*y, "/":lambda x,y:x//y if x//y > 0 else -((-x)//y)}
        for i in tokens:
            if i in do:
                x=a.pop()
                y=a.pop()
                a.append(do[i](y,x))
            else:
                a.append(int(i))
        return a.pop()