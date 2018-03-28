

import sys
a = []
filename = input("Insert the name of the file were your list will be saved:")

def insertrange(rangenumber):
    while type(rangenumber) != int:
        rangenumber = int(input("Insert an integer bigger than zero:"))
    return rangenumber
def insert(a,coreins):
    for e in range(coreins):
        e = input("Insert the list iteam:")
        a.append(e)
    return a
    
def listoutput(a):
    print("this is your list\n",a)

flag = 0
b = []

def anse(ans , flag ,b,filename):
    while flag == 0:
           if ans == "y":
               flag = 1
               morein = int(input("how many?"))
               for e in range(morein):
                   e = input("Insert the list iteam:")
                   b.append(e)
               return b
           elif ans == "n":
               with open(filename, 'a') as f:
                   for i in a:
                       f.write(str(i))
                       f.write("\n")
               print ("ok bye")
               flag  = 1
               sys.exit()
           else:
               flag = 0
               ans = input("DO YOU WANT TO ADD MORE ITEAMS TO YOUR LIST(Y/N)?")

rangenumber = input("Insert the range of your shopping list:")
corins = insertrange(rangenumber)
insert(a,corins)
listoutput(a)
ans = input("DO YOU WANT TO ADD MORE ITEAMS TO YOUR LIST(Y/N)?")
with open(filename, 'a') as f:
    for i in a:
        f.write(str(i))
        f.write("\n")

anse(ans,flag,b,filename)
n = len(b)
if n != 0:
    print(b)
    with open(filename, 'a') as f:
        for i in b:
            f.write(str(i))
            f.write("\n")
