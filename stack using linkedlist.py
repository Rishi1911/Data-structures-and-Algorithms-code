class node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class stack:
    def __init__(self,start = None):
        self.start = start
        self.itemcount = 0
    def isempty(self):
        return self.start == None
    def push(self,data):
        n = node(data,self.start)
        self.start = n
        self.itemcount +=1
    def pop(self):
        item = self.start.data
        self.start= self.start.next
        self.itemcount -= 1
        return item
    def size(self):
        return self.itemcount
    def peek (self):
        return self.start.data
s = stack()
s.push(10)
print(s.peek()) #10
s.push(20)
print(s.peek()) # 20 10
s.push(30)
print(s.peek()) # 30 20 10
s.push(40)
print(s.peek()) # 40 30 20 10
print(s.size())
print(s.pop())
print(s.size())
print(s.peek())

        
            
