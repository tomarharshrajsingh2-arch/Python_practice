# sorting in ascending order 
# arr = [9, 4, 7, 1, 3]
# swap=True
# while swap:
#     swap=False
#     for i in range(len(arr)-1):
#         if arr[i]>arr[i+1]:
#             arr[i],arr[i+1]=arr[i+1],arr[i]
#             swap=True
# print(arr)

#sorting in descending order
arr=[3,1,5,2]
swap=True
while swap:
    swap=False
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            swap=True
print (arr)