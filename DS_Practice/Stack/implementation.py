class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()

    def top(self):
        if not self.isEmpty():
            return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.top()


s = Stack()
s.push(5)
s.push(6)
print(s.top())
