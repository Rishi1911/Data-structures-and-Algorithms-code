def insertion(list):
    for i in range(1,len(list)):
         j = i
         while list[j-1] > list[j] and j>0:
             list[j-1],list[j] = list[j],list[j-1]
             j-=1
l = [20,30,40,10,60,50]
insertion(l)
print(l)
