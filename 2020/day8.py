
f = open("day8_test.txt", "r")
lines = f.readlines()
n = len(lines)
f.close()

def accuValue(attempt):
    ens = set()
    accu = 0
    i = 0
    change = 0
    while(i not in ens):
        if(i == n):
            return (accu, True)
        if(i < 0 or i > n):
            print("ERROR")
            return
        ens.add(i)
        line = lines[i]
        action = line[:3]
        symb = line[4]
        value = int(line[5:-1])
        if(action == "acc"):
            if(symb == "+"):
                accu += value
            elif(symb == "-"):
                accu -= value
            i += 1
        elif(action == "jmp"):
            change += 1
            if(change == attempt):
                i+= 1
            elif(symb == "+"):
                i += value
            elif(symb == "-"):
                i -= value
        elif(action == "nop"):
            change += 1
            if(change == attempt):
                if(symb == "+"):
                    i += value
                elif(symb == "-"):
                    i -= value
            else:
                i += 1
    return (accu, False)


attempt = 0
while attempt < n:
    res, stop = accuValue(attempt)
    if(stop):
        print(res)
        break
    attempt += 1
