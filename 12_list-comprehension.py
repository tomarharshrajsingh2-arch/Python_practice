# row=[]
# for i in range(8):
#     row.append("White Pawn")
# print(row)

# row=["White Pawn" for i in range(8)]
# print(row)

# squares=[x**2 for x in range(10)] 
# print(squares)

# twos=[2**x for x in range(10)]
# print(twos)

squares=[x**2 for x in range(10)] 
odds=[f"{x} is an odd number" for x in squares if x%2!=0]
print(squares)
print(odds)