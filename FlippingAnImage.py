lst1 = [[1,0,0],[0,1,1],[0,1,0]]
for i in lst1:
    i.reverse()
    counter = 0
    for j in i:
        if j == 0:
            i[counter] = 1
            counter+=1
        else:
            i[counter] = 0
            counter+=1
print(lst1)
