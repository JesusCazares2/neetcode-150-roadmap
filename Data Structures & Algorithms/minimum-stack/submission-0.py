class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        tmp = []
        returnMin = self.stack[-1]

        while len(self.stack):
            returnMin = min(self.stack[-1], returnMin)
            tmp.append(self.stack.pop())

        while len(tmp):
            self.stack.append(tmp.pop())

        return returnMin
