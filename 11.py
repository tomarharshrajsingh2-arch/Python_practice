list=[8,10,6,2,4]
#list=[1,2,3,4,5]
swapped = True
count=0
while swapped:
    swapped=False 
    for i in range(len(list)-1):
        count+=1
        if list[i]>list[i+1]:
            swapped= True
            list[i],list[i+1]=list[i+1],list[i]
        
            
print(list)
print(count)