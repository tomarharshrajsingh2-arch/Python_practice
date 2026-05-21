#chess board
# board=[]
# for i in range(8):
#     row=["empty" for i in range(8)]
#     board.append(row)
# for index in board:
#     print(index)   
# print("______")

# board[0][0]="W Rook"
# board[0][7]="W Rook"
# board[7][0]="B Rook"
# board[7][7]="B Rook"

# board[0][1]="W Knight"
# board[0][6]="W Knight"
# board[7][1]="B Knight"
# board[7][6]="B Knight"

# board[0][2]="W Bishop"
# board[0][5]="W Bishop"
# board[7][2]="B Bishop"
# board[7][5]="B Bishop"

# board[0][3]="W Queen"
# board[0][4]="W King"
# board[7][3]="B Queen"
# board[7][4]="B King"

# for i in range(8):
#     board[1][i]="W pawn"
# for i in range(8):
#     board[6][i]="B pawn"

# for index in board:
#     print(index)

#temperature data
temps=[[0.0 for h in range(24)]for d in range(31)]
temp1=30
temp2=32
count=0
for day in temps:
    if count==0:
          day[11]=temp1
          count=1
    else:
        day[11]=temp2
        count=0
for day in temps:
    print(day)
print("______")

total=0.0
for day in temps:
        total+=day[11]
print(total)
avg=total/31
print(f"Average temperature at 12 PM: {avg}°C")

highest=-100.0
for day in temps:
    for temp in day:
        if temp>highest:
            highest=temp
            
print(f"Highest temperature: {highest}°C")

hot_days=0
for day in temps:
     if day[11]>30:
         hot_days+=1
print(f"Number of hot days: {hot_days}")