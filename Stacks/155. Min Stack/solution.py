class MinStack:

    def __init__(self):
        self.stck=[]
        self.min_stack=[]
        

    def push(self, val: int) -> None:
        self.stck.append(val)
        if len(self.min_stack)<=0:
            self.min_stack.append(val)
        elif self.min_stack[-1]<val:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        self.stck.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stck[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()