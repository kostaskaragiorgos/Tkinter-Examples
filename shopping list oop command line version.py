import sys

class shoppinglist:
    #constructor

    def __init__(self,name , listrange , flag,filename = 'shoppinglist.txt'):
        self.name = name
        self.lista = []
        self.listrange = 0
        self.flag = 0
        self.blist = []


#insert input
    def addinplist(self,inp):
        self.lista.append(inp)


#showthelist
    def showlist(self):
        print("This is your list",self.lista)

    def showlistb(self):
        if len(self.blist) != 0:
            print("This is your added iteams",self.blist)


#an
    def ans(self , ans ,flag ):
            while flag == 0:
                if ans == "y":
                    flag = 1
                    morein = int(input("how many?"))
                    for e in range(morein):
                        e = input("Insert the list iteam:")
                        self.blist.append(e)
                elif ans == "n":
                    print ("ok bye")
                    flag  = 1
                    self.file('shoppinglist.txt')
                    sys.exit()
                else:
                    flag = 0
                    ans = input("DO YOU WANT TO ADD MORE ITEAMS TO YOUR LIST(Y/N)?")


    
# file
    def file(self,filename):
        with open('shoppinglist.txt' , 'w') as f:
            for i in self.lista:
                f.write(str(i))
                f.write("\n")

        with open('shoppinglist.txt','a') as f:
            for i in self.blist:
                f.write(str(i))
                f.write("\n")


    
rangenumber = int(input("Insert the range of your shopping list:"))

while rangenumber <= 0:
    rangenumber = int(input("Insert an integer bigger than zero:"))

s = shoppinglist('sc', rangenumber , 0 , shoppinglist)
for e in range(rangenumber):
    insertval = input("Insert the list iteam:")
    s.addinplist(insertval)
s.showlist()
ans = str(input("DO YOU WANT TO ADD MORE ITEAMS TO YOUR LIST(Y/N)?"))
s.ans( ans,0)
s.showlist()
s.showlistb()
s.file('shoppinglist.txt')


