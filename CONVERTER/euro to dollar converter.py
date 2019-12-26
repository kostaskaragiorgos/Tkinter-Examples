from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *



class GUI():
    def __init__(self,master,):
        master.title("€ TO $ CONVERTER")

        global dollarv
        dollarv =1.2369
        self.frame = Frame(master)
        self.frame.pack()

        self.label = Label(self.frame, text = "Insert iteam")
        self.label.grid(row=0)


        self.enter = Entry(self.frame, width=5, bg='white')
        self.enter.grid(row=0, column=1)


        self.frameb = Frame(master)
        self.frameb.pack()

        
        self.bins = Button(self.frameb, text="Convert",command=self.convert)
        self.bins.pack(side=LEFT)

        self.binsh = Button(self.frameb, text="save", command=self.save)
        self.binsh.pack(side=LEFT)

        self.frameb = Frame(master)
        self.frameb.pack()

        self.myText = StringVar()
        self.myText.set(50*'_')
        self.mylabel = Label(self.frameb,textvariable = self.myText,font = "Arial 20")
        self.mylabel.pack()

        

    def convert(self):
        global final1
        global eurov
        final1 = dollarv * float(self.enter.get())
        self.myText.set('The dollar value of  '+(str(float(self.enter.get())))+'€ is '+str(final1)+"$")
        

                     
        

def main():
   root = Tk()
   app = GUI(root)

   root.mainloop()


if __name__ == "__main__":
    main()
