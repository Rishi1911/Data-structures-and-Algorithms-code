def merge(list1):
    if len(list1)>1:
        mid = len(list1)//2
        left = list1[:mid]
        right = list1[mid:]

        merge(left)
        merge(right)

        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                list1[k] = left[i]
                i+=1
            else:
                list1[k] = right[j]
                j+=1
            k+=1
        while i<len(left):
            list1[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            list1[k] = right[j]
            j+=1
            k+=1
list1  = [90,20,30,50,40,60,10,70,80]
merge(list1)
print(list1)
