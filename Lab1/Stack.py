class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack hooson baina"
        return self.stack.pop()
    
    def top(self):
        if self.isEmpty():
            return "Stack hooson baina"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def length(self):
        return len(self.stack)
    