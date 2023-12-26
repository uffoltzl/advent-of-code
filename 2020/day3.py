
f = open("day3.txt", "r")
values = f.readlines()
f.close()


def countTrees(step_j, step_i=1):
    count = 0
    n = len(values)
    m = len(values[0])-1
    j = 0
    for i in range(step_i, n, step_i):
        j = (j+step_j)%m
        if(values[i][j] == "#"):
            count += 1
    return count

print(countTrees(1, 1)*countTrees(3, 1)*countTrees(5, 1)*countTrees(7, 1)*countTrees(1, 2))
