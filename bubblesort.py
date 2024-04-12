def bubble_sort(ilist):
    for r in range(1,len(ilist)):
        for i in range(len(ilist)-r):
            if ilist[i]>ilist[i+1]:
                ilist[i],ilist[i+1] = ilist[i+1],ilist[i]

def mod_bubblesort(ilist):
    swap = False
    for r in range(1,len(ilist)):
        for i in range(len(ilist)-r):
            if ilist[i]>ilist[i+1]:
                swap = False
                ilist[i],ilist[i+1] = ilist[i+1],ilist[i]
        if not swap:
            return
l = [25,40,20,15,90,70]
bubble_sort(l)
print(l)
mod_bubblesort(l)
print(l)
