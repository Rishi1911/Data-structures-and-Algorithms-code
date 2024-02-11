class node:
    def __init__(self,item = None,next = None):
        self.item = item
        self.next = next
class cll:
    def __init__(self,last = None):
        self.last = last
    def isempty(self):
        return self.last == None
    def insertatfirst(self,data):
        n = node(data)
        if self.isempty():
            self.last = n #since it is circular so the node should refer
            #to itself to make it cicular 
            n.next = n
        else:
            n.next = self.last.next
            self.last.next = n
    def insertatlast(self,data):
        n= node(data)
        if self.isempty():
            self.last = n
            n.next = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n
    def insertafter(self,temp,data):
        if temp is not None:
            n = node(data,temp.next)
            temp.next = n
            if temp == self.last:
                self.last =n

    def printlist(self):
        if not self.isempty():
            temp = self.last.next
            while temp!= self.last:
                print(temp.item,end=" ")
                temp = temp.next
            print(temp.item)
    
                            
cli = cll()
cli.insertatfirst(10)
cli.insertatfirst(20)
cli.insertatlast(30)
cli.insertatlast(40)
cli.printlist()
