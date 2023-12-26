
f = open("day9.txt", "r")
val = f.readlines()
f.close()


def searchMatching2(tot, values):
    seen = set()
    for element in values:
        element_int = int(element[:-1])
        if(tot-element_int in seen):
            return True
        else:
            seen.add(element_int)
    return False

def findInvalid():
    n = len(val)
    for i in range(25, n):
        if(not searchMatching2(int(val[i][:-1]), val[(i-25):i])):
            return int(val[i][:-1])
