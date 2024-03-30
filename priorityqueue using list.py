class priorityqueue:
    def __init__(self):
        self.item = []
    def push(self,data,priority):
        index = 0
        while index<len(self.item) and self.item[index][1]<priority:
            index+=1
        self.item.insert(index,(data,priority))
    def isempty(self):
        return len(self.item) == 0
    def pop(self):
        if self.isempty():
            raise IndexError("queue is empty")
        else:
            return self.item.pop(0)[0]
    def size(self):
        return len(self.item)

p = priorityqueue()
a = int(input("enter the number of student"))
for x in range(a):
    data = input("enter the name")
    priority = int(input("enter the priority number"))
    p.push(data,priority)

while not p.isempty():
    print(p.pop())
