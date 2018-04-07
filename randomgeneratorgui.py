from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import random 

class GUI():
    def __init__(self,master):
        master.title("RANDOM NUMBER GENERATOR")
        self.frame = Frame(master)
        self.frame.pack()

        self.frameb = Frame(master)
        self.frameb.pack()

        self.myText1 = StringVar()
        self.myText1.set(15*'_')
        self.mylabel = Label(self.frame,textvariable = self.myText1 , font = "Arial 20")
        self.mylabel.pack()

        self.myText2 = StringVar()
        self.myText2.set(15*'_')
        self.mylabel = Label(self.frame,textvariable = self.myText2 , font = "Arial 20")
        self.mylabel.pack()

        self.myText3 = StringVar()
        self.myText3.set(15*'_')
        self.mylabel = Label(self.frame,textvariable = self.myText3 , font = "Arial 20")
        self.mylabel.pack()

        self.myText4 = StringVar()
        self.myText4.set(15*'_')
        self.mylabel = Label(self.frame,textvariable = self.myText4 , font = "Arial 20")
        self.mylabel.pack()

        self.myText5 = StringVar()
        self.myText5.set(15*'_')
        self.mylabel = Label(self.frame,textvariable = self.myText5 , font = "Arial 20")
        self.mylabel.pack()


        self.gener1 = Button(self.frameb , text="generate 5 numbers",command=self.gener1bpre)
        self.gener1.pack(side=LEFT )

        self.myText = StringVar()
        self.myText.set(15*'_')
        self.mylabel = Label(self.frame,textvariable = self.myText , font = "Arial 20")
        self.mylabel.pack()

        self.gener2 = Button(self.frameb , text="generate 1 number",command=self.gener2bpre)
        self.gener2.pack(side=LEFT)
		
		
		 #menu
        self.menu = Menu(master)
        master.config(menu=self.menu)
    
        self.aboutmenu = Menu(self.menu)
        master.config(menu=self.menu)

        self.aboutmenu = Menu(self.menu)
        self.menu.add_cascade(label = "About", menu=self.aboutmenu)
        self.aboutmenu.add_command(label = "About",command = self.about)
        self.aboutmenu.add_command(label = "Help",command= self.helpgene)

    def about(self):
        showinfo("INFO", 'Developped by:\nKOSTAS KARAGIORGOS')


        
    def helpgene(self):
        showinfo("HELP",'THIS IS A RANDOM NUMBER GENERATOR.\nTHIS IS JUST FOR STUDY PURPOSE.\n')

    def gener1bpre(self):  #generates five
        self.myText1.set('FIRST NUMBER:'+str(random.randint(1,45)))
        self.myText2.set("SECOND NUMBER:"+str(random.randint(1,45)))
        self.myText3.set('THIRD NUMBER:'+str(random.randint(1,45)))
        self.myText4.set("FOURTH NUMBER:"+str(random.randint(1,45)))
        self.myText5.set("FIFTH NUMBER:"+str(random.randint(1,45)))
  
    def gener2bpre(self): #generates one
        self.myText.set("SPECIAL NUMBER:"+str(random.randint(1,20)))
        
def main():
   root = Tk()
   root.geometry("300x270+270+270")
   app = GUI(root)
   

   root.mainloop()


if __name__ == "__main__":
    main()
