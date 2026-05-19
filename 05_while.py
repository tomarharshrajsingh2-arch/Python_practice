i=int (input("Enter a number: "))
even=0
odd=0
while i>0:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
    i=i-1
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")    