list = [1,2.3,"Dipesh",3,4.6,"Koirala"]
listint = []
listfloat = []
liststr = []
for x in list:
    if type(x) == int:
        listint.append(x)
    elif type(x) == float:
        listfloat.append(x)
    else:
        liststr.append(x)
print(list)
print(listint)
print(listfloat)
print(liststr)