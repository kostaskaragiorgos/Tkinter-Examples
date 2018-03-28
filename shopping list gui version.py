from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *



class GUI():
    def __init__(self,master):
        master.title("SHOPPING LIST")

        self.lista = []

        self.frame = Frame(master)
        self.frame.pack()

        self.label = Label(self.frame, text = "Insert iteam")
        self.label.grid(row=0)


        self.enter = Entry(self.frame, width=5, bg='white')
        self.enter.grid(row=0, column=1)

        self.frameb = Frame(master)
        self.frameb.pack()

        
        self.bins = Button(self.frameb, text="insert",command=self.insert)
        self.bins.pack(side=LEFT)

        self.binsh = Button(self.frameb, text="save", command=self.save)
        self.binsh.pack(side=LEFT)

        self.bclear = Button(self.frameb,text="clear", command = self.clear)
        self.bclear.pack(side = LEFT)

        self.bcdel = Button(self.frameb,text="delete", command = self.deletei)
        self.bcdel.pack(side = LEFT)

        self.menu = Menu(master)
        master.config(menu=self.menu)
      
          # help menu
        self.helpmenu = Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="About", command=self.about)


    def about(self):
        showinfo('Info', 'Developped by:\nKOSTAS KARAGIORGOS')

    def insert(self):
         self.lista.append(str(self.enter.get()))

    def clear(self):
        self.enter.delete(0,len(str(self.enter.get())))

    def save(self):
         export_file = asksaveasfilename(defaultextension='.txt', title='Write on File...', initialfile='shoppinglist', filetypes=[('Text Files', '*.txt')])
         with open(export_file,'w') as f:
             for i in self.lista:
                 f.write(str(i))
                 f.write("\n")

    def deletei(self):
        self.lista.pop()
        
                
                
def main():
   root = Tk()
   app = GUI(root)

   root.mainloop()


if __name__ == "__main__":
    main()
