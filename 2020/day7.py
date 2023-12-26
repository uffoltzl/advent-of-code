
f = open("day7.txt", "r")

def bags():
    ens = {}
    line = f.readline()
    while(line != ''):
        line = line.split(" bag")
        mere = ""
        for col in line:
            if "contain" in col:
                col = col[10:]
                j = col.index(" ")+1
                nb = col[:j]
                col = col[j:]
                if(col != "other"):
                    ens[mere].append((col, int(nb)))
            elif "," in col:
                j = col.index(" ")+1
                col = col[j:]
                j = col.index(" ")+1
                nb = col[:j]
                col = col[j:]
                if(col != "other"):
                    ens[mere].append((col, int(nb)))
            elif "\n" in col:
                continue
            else:
                if col not in ens:
                    ens[col] = []
                    mere = col
        line = f.readline()
    return ens

def parcours(ens, col, viewed):
    if(len(ens[col]) == 0):
        return (viewed, False)
    yes = False
    for (col2, nb) in ens[col]:
        viewed.add(col2)
        if(col2 == "shiny gold"):
            yes = True
    if(yes):
        return (viewed, True)
    for (col2, nb) in ens[col]:
        (viewed, yes2) = parcours(ens, col2, viewed)
        yes = yes or yes2
    return (viewed, yes)

def containShiny(ens):
    count = 0
    for col in ens.keys():
        if(col == "shiny gold"):
            continue
        else:
            (viewed, yes) = parcours(ens, col, set())
            if(yes):
                count += 1
    return count

def requireBags(ens, col):
    count = 1
    if(len(ens[col]) == 0):
        return count
    for (col2, nb) in ens[col]:
        count += nb*requireBags(ens, col2)
    return count

ens = bags()
print(containShiny(ens))
print(requireBags(ens, "shiny gold")-1)

f.close()
