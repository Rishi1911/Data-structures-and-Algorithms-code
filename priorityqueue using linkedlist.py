class node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority = priority
        self.next=next
class priorityqueue:
    def __init__(self):
        self.start = None
        self.itemcount = 0
    def isempty(self):
        return self.start==None
    def push(self,data,priority):
        n = node(data,priority)
        if not self.start or priority<self.start.priority:
            n.next=self.start
            self.start=n
        else:
            temp = self.start
            while temp.next and temp.next.priority<=priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.itemcount+=1
    def pop(self):
        if self.isempty():
            raise IndexError("queue is empty")
        else:
            data = self.start.item
            self.start = self.start.next
            return data
        self.itemcount-=1
    def size(self):
        return self.itemcount

p = priorityqueue()
p.push("rishi",1)
p.push("kush",4)
p.push("satayam",2)
p.push("chirag",3)
while not p.isempty():
    print(p.pop())
