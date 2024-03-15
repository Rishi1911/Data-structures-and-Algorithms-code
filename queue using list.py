class queue:
    def __init__(self):
        self.item = []
    def isempty(self):
        return len(self.item) == 0
    def enqueue(self,data):
        self.item.append(data)
    def dequeue(self):
        if not self.isempty():
            self.item.pop(0)
        else:
            raise IndexError("queue is empty")
    def getfront(self):
        if not self.isempty() :
            return self.item[0]
        else:
            raise IndexError("queue is empty")
    def getrear(self):
        if not self.isempty():
            self.item[-1]
        else:
            raise IndexError("stack is empty")
    def size(self):
        return len(self.item)
    
qi = queue()
try:
    print(qi.getfront())
except IndexError as e:
    print(e.args[0])
qi.enqueue(5)
print(qi.getfront())
qi.enqueue(10)
print(qi.getfront())
qi.enqueue(50)
print(qi.getfront())
qi.dequeue()
print(qi.getfront())
qi.dequeue()
print(qi.getfront())
qi.dequeue()
print(qi.getfront())

