
f = open("day6.txt", "r")

def anyone():
    line = f.readline()
    ens = set()
    count = 0
    while line != '':
        if(line == '\n'):
            count += len(ens)
            ens = set()
        n = len(line)-1
        for i in range(n):
            ens.add(line[i])
        line = f.readline()
    count += len(ens)
    return count

def everyone():
    line = f.readline()
    ens = []
    first = True
    count = 0
    while line != '':
        if(line == '\n'):
            count += len(ens)
            ens = []
            first = True
        elif first:
            n = len(line)-1
            first = False
            for i in range(n):
                ens.append(line[i])
        else:
            n = len(ens)#non opti, calculer à chaque fois
            i = 0
            while i < n:
                if(ens[i] not in line):
                    del ens[i]
                    n -= 1
                else:
                    i +=1
        line = f.readline()
    count += len(ens)
    return count

print(everyone())

f.close()
