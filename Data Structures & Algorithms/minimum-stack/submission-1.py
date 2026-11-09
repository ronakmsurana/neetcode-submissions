class MinStack:

    def __init__(self):
        self.stack = []

    def top(self) -> int:
        return self.stack[-1][0]

    def push(self, val: int) -> None:
        print(val,self.top() if self.stack else val)
        self.stack.append((val,min(val,self.getMin() if self.stack else val)))

    def pop(self) -> None:
        self.stack.pop()


    def getMin(self) -> int:
        return self.stack[-1][1]
