class node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next
class deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.itemcount = 0
    def isempty(self):
        return self.itemcount==0
    def insertfront(self,data):
        n = node(data,None,self.front)
        if self.isempty():
            self.front=n
            self.rear=n
        else:
            self.front.prev = n
            self.front=n
        self.itemcount+=1
    def insertrear(self,data):
        n = node(data,self.rear,None)
        if self.isempty():
            self.front=n
            self.rear=n
        else:
             self.rear.next=n
             self.rear=n
        self.itemcount+=1
    def deletefront(self):
        if self.isempty():
            return None
        if self.front == self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.front.prev = None
        self.itemcount-=1
    def deleterear(self):
        if self.isempty():
            return None
        if self.front == self.rear:
             self.front = None
             self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.itemcount-=1
    def getfront(self):
        if self.isempty():
            return None
        else:
            return self.front.item
    def getrear(self):
        if self.isempty():
            return None
        else:
            return self.rear.item
    def size(self):
        return self.itemcount

d=deque()
d.insertfront(10)
d.insertfront(20)
d.insertrear(30)
d.insertrear(40)
print(d.getfront(),d.getrear())
d.deletefront()
d.deleterear()
print(d.getfront(),d.getrear())
