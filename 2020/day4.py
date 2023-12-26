import re


f = open("day4.txt", "r")

def countValues(cid=0):
    count = 0
    line = f.readline()
    passport_fields = set()
    while(line != ''):
        if(line == "\n"):
            if(len(passport_fields) == (7+cid)):
                count += 1
            passport_fields = set()
        else:
            fields = line.split()
            n = len(fields)
            for i in range(n):
                field = fields[i][:3]
                value = fields[i][4:]
                if(not(cid) and field == "cid"):
                    continue
                elif(field == "byr" and int(value) >= 1920 and int(value) <= 2002):
                    passport_fields.add(field)
                elif(field == "iyr" and int(value) >= 2010 and int(value) <= 2020):
                    passport_fields.add(field)
                elif(field == "eyr" and int(value) >= 2020 and int(value) <= 2030):
                    passport_fields.add(field)
                elif(field == "hgt"):
                    if(value[-2:] == "cm" and int(value[:-2]) >= 150 and int(value[:-2]) <= 193):
                        passport_fields.add(field)
                    elif(value[-2:] == "in" and int(value[:-2]) >= 59 and int(value[:-2]) <= 76):
                        passport_fields.add(field)
                elif(field == "hcl" and re.search("^#([a-f]|[0-9]){6}$", value)):
                    passport_fields.add(field)
                elif(field == "ecl" and value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                    passport_fields.add(field)
                elif(field == "pid" and re.search("^[0-9]{9}$", value)):
                    passport_fields.add(field)
        line = f.readline()
    if(len(passport_fields) == (7+cid)):
        count += 1
    return count


print(countValues())

f.close()
