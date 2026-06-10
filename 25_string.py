# # city = "bhopal"
# # print(city[0])
# # print(city[2])

# # print(city[-1])
# # print(city[-5])

# # print(city[-3])
# # print(city[3])


# # name ="priya sharma"
# # print(name[0:5])
# # print(name[6:])
# # print(name[:5])
# # print(name[::2])
# # print(name[::-1])

# # print (len(name))

# text = "  Hello python World  "
# print(text.upper())
# print(text.lower())
# print(text.strip())
# print(text.title())
# print(text.capitalize())


# print(text.find("Python"))
# print('Python' in text)
# print(text.count("l"))

# print (text.replace("Hello", "Hi"))

# csv='rahul,22,bhopal,engineer'
# data=csv.split(',')
# print(data)
# print(data[0])
# rejoined= ' | '.join(data)
# print(rejoined)

# print ('hello123'.isalnum())# `True` because it contains only letters and numbers
# print('12345'.isdigit())# `True` because it contains only digits
# print('Hello'.isalpha())# `True` because it contains only letters
# print('   '.isspace())# `True` because it contains only whitespace

# email = "harsh@gmail.com"
# print(email.endswith(".com"))# `True` because the email ends with ".com"
# print(email.startswith("harsh"))# `True` because the email starts with "harsh"


# name, marks ,rank = "Rahul", 85.999, 1
# print(f"hello {name}")

# print(f"marks: {marks:.2f}")
# print(f"marks: {marks:.0f}")
# print(f"count:{1000000:,}")


# print(f"{name:<10}|{marks:<8.2f}|{rank}")

# price , gst = 500, .18
# print(f"Price: rs{price:.2f}| GST: rs{price*gst:.2f}| Total: rs{price*(1+gst):.2f}")


# print(f"hello {name:>10}")
# print(f"hello {name:^10}")
# print(f"hello {name:*^10}")
# print(f"hello {name:<10}")

string = "hello , how are you doing today "
count=0
string=string.upper()

for i in string:
    if i=='A'or i=='E' or i=='I'or i=='O'or i=='U':
        count=count+1
print(count)


print(string[16:20])

