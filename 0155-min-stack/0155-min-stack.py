class MinStack:

    def __init__(self):
        self.st = []

    def push(self, value: int) -> None:
        
        cur_min = min(value, self.st[-1][1] if self.st else value)
        self.st.append((value, cur_min))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()