# dictionary={
#     "cat":"chat",
#     "dog":"chien",
#     "horse":"cheval"
# }

# phoneno={
#     "John":1234567890,
#     "Alice":9876543210
# }
# empty_dict={}
# print(dictionary)
# print(type(dictionary))
# print(phoneno)
# print(type(phoneno))
# print(empty_dict)
# print(type(empty_dict))
# print(phoneno["John"])
 
# dict=("cat","lion","dog","horse")
# for word in dict:
#     if word in dictionary:
#         print(word, ":", dictionary[word])
#     else:
#         print(word, ": Not found in dictionary")

# print(dictionary.keys())

# for key in dictionary.keys():
#     print(key,"->",dictionary[key])



# dictionary={
#     "cat":"chat",
#     "dog":"chien",
#     "horse":"cheval"
# }
# print(dictionary.items())
# for key, value in dictionary.items():
#     print(key,"->",value)
 
# print(dictionary.values())
# for value in dictionary.values():
#     print(value)

# dictionary={
#     "cat":"chat",
#     "dog":"chien",
#     "horse":"cheval"
# }
# copy_dict=dictionary
# copy_dict1=dictionary.copy()
# print(copy_dict)

# copy_dict["cat"]="chaton"
# print(dictionary)

# copy_dict1["dog"]="chiin"
# print(dictionary)

# print(copy_dict1)

# phonebook={}
# print(phonebook)
# phonebook["John"]=1234567890
# print(phonebook)
# del phonebook["John"]
# print(phonebook)

# dict1={"a":1}
# print(dict1)
# dict1.update({"b":2})
# print(dict1)
# dict1.popitem()
# print(dict1)
# dict2={1:"one", 2:"two", 3:"three"}
# print(dict2)
# dict2.popitem()
# print(dict2)

# dictionary={
#     "cat":"chat",
#     "dog":"chien",
#     "horse":"cheval"
# }

# if "cat" in dictionary:
#     print("cat is present in the dictionary")
# else:
#     print("cat is not present in the dictionary")


# if "lion" not in dictionary:
#     print("lion is not present in the dictionary")
# else:  
#      print("lion is present in the dictionary")


# print(dictionary)
# print(len(dictionary))
# del dictionary["cat"]
# print(dictionary)
# print(len(dictionary))
# dictionary.clear()
# print(dictionary)
# print(len(dictionary))

# del dictionary
# print(dictionary)



# dictionary.update({"lion":"lion"})
# print(dictionary)


student={}

while True:
    name=input("enter name of student :")
    if name=='':
        break
    else:
        marks=int(input("enter marks of student :"))
        if marks not in range(1,11):
            break
        if name in student :
            student[name]+=(marks,)
        else:
            student[name]=(marks,)
print (student) 

for name,mark in student.items():
    sum=0
    for m in mark:
        sum += m
    print(name,"-->",sum/len(mark))



