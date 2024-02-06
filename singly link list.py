class node:
    def __init__(self,item = None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self,start = None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insertatfirst(self,data):
        n = node(data,self.start)
        self.start = n

    def insertatlast(self,data):
        n = node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insertafter(self,temp,data):
        if temp is not None:
            n = node(data,temp.next)
            temp.next = n

    def printlist(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next

    def deletefirst(self):
        if not self.is_empty():
            self.start = self.start.next

    def deletelast(self):
        if self.start is None:
            pass
        elif self.start.next == None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            
    def deleteitem(self,data):
        if self.start is None:
            pass
        elif not self.is_empty():
            if self.start.item == data:
                self.start = self.start.next
        else:
            temp = self.start
            while temp.next is not None:
                if temp.next.item == data:
                    temp.next = temp.next.next
                    break
                temp = temp.next

        
l1 = SLL()
l1.insertatfirst(20)
l1.insertatlast(50)
l1.insertatfirst(10)
l1.insertafter(l1.search(20),25)
l1.printlist()
print("\n")
l1.deleteitem(10)
l1.printlist()
