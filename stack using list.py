class stack:
    def __init__(self):
        self.item =[]
    def isempty(self):
        return len(self. item)==0
    def push(self,data):
        self.item.append(data)
    def pop(self):
        if not self.isempty():
            return self.item.pop()
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.isempty():
            return self.item[-1]
        else:
            raise IndexError("stack is empty")
    def size(self):
        return len(self.item)

s1 = stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("top element is",s1.peek())
print("removed element",s1.pop())
print("top element is",s1.peek())
