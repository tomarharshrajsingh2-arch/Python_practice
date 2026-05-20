list=[8,10,6,2,4]
#list=[1,2,3,4,5]
n=len(list)
swapped = True
count=0
while swapped:
    swapped=False 
    for i in range(n-1):
        count+=1
        if list[i]>list[i+1]:
            swapped= True
            list[i],list[i+1]=list[i+1],list[i]
        #n=n-1
            
print(list)
print(count)