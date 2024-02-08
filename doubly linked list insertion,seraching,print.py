class node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next
        
class dll:
    def __init__(self,start=None):
        self.start = start
        
    def isempty(self):
        return self.start == None
    
    def insertatfirst(self,data):
        n = node(None,data,self.start)
        if not self.isempty():
            self.start.prev = n
        self.start = n
        
    def insertatlast(self,data):
        temp = self.start
        if self.start is not None:
            while temp.next is not None:
                temp = temp.next
        n = node(temp,data,None)
        if temp == None:
            self.start = n
        else:
            temp.next = n
            
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
            if temp.item == data:
                print("\nThe Item is found")
        
    def insertafter(self,temp,data):
        if temp is not None:
            n = node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n
            
    def println(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp = temp.next
    

li = dll()
li.insertatfirst(20)
li.insertatlast(30)
li.insertafter(li.search(20),25)
li.insertatfirst(50)
li.insertatlast(10)
li.println()
li.search(25)

