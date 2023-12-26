import math

f = open("day5.txt", "r")

def place(entry):
    row_bottom = 0
    row_top = 127
    for i in range(7):
        mid = (row_top-row_bottom)/2 + row_bottom
        if(entry[i] == "F"):
            row_top = math.floor(mid)
        elif(entry[i] == "B"):
            row_bottom = math.ceil(mid)
    col_bottom = 0
    col_top = 7
    for i in range(7, 10):
        mid = (col_top-col_bottom)/2 + col_bottom
        if(entry[i] == "L"):
            col_top = math.floor(mid)
        elif(entry[i] == "R"):
            col_bottom = math.ceil(mid)
    assert(row_bottom == row_top)
    assert(col_top == col_bottom)
    return (row_bottom, col_bottom)

def seatID(value):
    row, col = value
    return row*8+col

line = f.readline()
#maxi = 0
ens = set()
while(line != ''):
    res = seatID(place(line))
    #if(maxi == 0 or res > maxi):
    #    maxi = res
    ens.add(res)
    line = f.readline()

maxiSeatId = seatID((127, 7))
for seat in range(1, maxiSeatId):
    if(seat not in ens) and ((seat+1) in ens) and ((seat-1) in ens):
        print(seat)
        break

#print(maxi)

f.close()
