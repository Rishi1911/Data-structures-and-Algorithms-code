class node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
class queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.itemcount = 0
    def isempty(self):
        return self.itemcount == 0
    def enqueue(self,data):
        n = node(data)
        if self.isempty():
            self.front=n
            self.rear=n
        else:
            self.rear.next=n
            self.rear = n
        self.itemcount+=1
    def dequeue(self):
        if self.isempty():
            raise IndexError("queue is empty")
        elif self.rear == self.front:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.itemcount-=1
    def getfront(self):
        if self.isempty():
            raise IndexError("stack is empty")
        else:
            return self.front.item
    def getrear(self):
        if self.isempty():
            raise IndexError("queue is empty")
        else:
            return self.rear.item
    def size(self):
        return self.item.count

q = queue()
q.enqueue(50)
q.enqueue(10)
q.enqueue(20)
print(q.getfront())
print(q.getrear())
q.dequeue()
print(q.getfront())
print(q.getrear())
q.dequeue()
print(q.getfront())
print(q.getrear())
q.dequeue()
