list = []
for i in range(1,11):
    l = input("Enter "+str(i)+" number:")
    while  len(l) == 0:
        print("Cant be null!")
        l = input("Enter "+str(i)+" number:")
    while(l.isalpha() == True):
        print("Not a string:")
        l = input("Enter " + str(i) + " number:")
    list.append(l)
print(list)