
TOTAL = 2020

f = open("day1.txt", "r")
val = f.readlines()

def searchMatching2(tot, values=val):
    seen = set()
    for element in values:
        element_int = int(element[:-1])
        if(tot-element_int in seen):
            return element_int*(tot-element_int)
        else:
            seen.add(element_int)
    return 0

def searchMatching3(tot):
    seen = set()
    for element in val:
        element_int = int(element[:-1])
        res = searchMatching2(tot-element_int, seen)
        if res:
            return res*element_int
        else:
            seen.add(element)
    return 0


print(searchMatching2(TOTAL))
print(searchMatching3(TOTAL))
f.close()
