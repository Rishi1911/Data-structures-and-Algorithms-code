class deque:
    def __init__(self):
        self.item=[]
    def isempty(self):
        return len(self.item) ==0
    def insertfront(self,data):
        self.item.insert(0,data)
    def insertrear(self,data):
        self.item.append(data)
    def deletefront(self):
        if not self.isempty():
            self.item.pop(0)
        else:
            return None
    def deleterear(self):
        if not self.isempty():
            self.item.pop()
        else:
            return None
    def getfront(self):
        if not self.isempty():
            return self.item[0]
        else:
            raise IndexError("deque is empty")
    def getrear(self):
        if not self.isempty():
            return self.item[-1]
        else:
            raise IndexError("deque is empty")
    def size(self):
        return len(self.item)

d = deque()
d.insertfront(10)
d.insertfront(20)
d.insertrear(30)
d.insertrear(40)
print(d.getfront(),d.getrear())
d.deletefront()
d.deleterear()
print(d.getfront(),d.getrear())
