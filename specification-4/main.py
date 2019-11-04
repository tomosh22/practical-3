from tkinter import Tk,Button,Entry,Label,Frame,Text,END
def add(name,values,text):
    text.insert(END,name.get()+":{"+values.get()+"}\n")
    name.delete(0,"end")
    values.delete(0,"end")
if __name__ == "__main__":
    window = Tk()



    listFrame = Frame(window)
    listText = Text(listFrame, width=20,height=10)
    listText.pack()


    addFrame = Frame(window)
    addTextName = Entry(addFrame, width=5)
    addTextNameLabel = Label(addFrame, text="Set Name")
    addTextSet = Entry(addFrame, width=30)
    addTextSetLabel = Label(addFrame, text="Set values")
    addButton = Button(addFrame, width=10, command=lambda:add(addTextName,addTextSet,listText), text="Add Set")
    addTextNameLabel.grid(row=0, column=0)
    addTextName.grid(row=0, column=1)
    addTextSetLabel.grid(row=1, column=0)
    addTextSet.grid(row=1, column=1)
    addButton.grid(row=2, column=0)

    listFrame.grid(row=0, column=0)
    addFrame.grid(row=0, column=1)

    window.mainloop()
