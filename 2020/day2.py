
f = open("day2.txt", "r")

def countCorrectPwdByOcc():
    line = f.readline()
    correct = 0
    while(line != ''):
        entry = line.split()
        mini, maxi = map(int, entry[0].split('-'))
        letter = entry[1][:-1]
        count = 0
        for l in entry[2]:
            if l == letter:
                count += 1
                if(count > maxi):
                    break
        if count <= maxi and count >= mini:
            correct += 1
        line = f.readline()
    return correct

def countCorrectPwdByPosition():
    line = f.readline()
    correct = 0
    while(line != ''):
        entry = line.split()
        pos1, pos2 = map(int, entry[0].split('-'))
        letter = entry[1][:-1]
        if(entry[2][pos1-1] == letter or entry[2][pos2-1] == letter) and not(entry[2][pos1-1] == letter and entry[2][pos2-1] == letter):
            correct += 1
        line = f.readline()
    return correct

# pas les 2 ensembles > mettre dans un seul tableau
#print(countCorrectPwdByOcc())
print(countCorrectPwdByPosition())

f.close()
