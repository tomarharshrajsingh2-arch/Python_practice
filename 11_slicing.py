# before slicing
list1=[1]
list2=list1
list1[0]=2
print(list1)
print(list2)

#slicing makes the copy of the list 
list1=[1]
list2=list1[:]
list1[0]=2
print(list1)
print(list2)

#list[:]-> cosiders full list
#list[start:end]-> here end is excluded
#-1 is the last index

list=[1,2,3,4,5]
list3=list[1:4]
print(list3)
list4=list[1:-1]
print(list4)
list5=list[-1:1]
print(list5)
list6=list[-5:3]
print(list6)
list7=list[:4]
print(list7)
list8=list[1:]
print(list8)
# deletion
del list[2:4]
print(list)
del list3[:]
print (list3)

print(1 in list)
print(1 not in list)

print(6 in list)
print(6 not in list)