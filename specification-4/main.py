from tkinter import Tk,Button,Entry,Label,Frame,Text,END
def add(name,values,text):
    if "" in [name.get(),values.get()]:
        print("Please enter a name and values")
        return
    text.insert(END,name.get()+":{"+values.get()+"}\n")
    name.delete(0,"end")
    values.delete(0,"end")
def calc():
    print("dummy")
if __name__ == "__main__":
    window = Tk()


    listFrame = Frame(window)
    listText = Text(listFrame, width=20,height=10)
    listLabel = Label(listFrame,text = "Sets")
    listLabel.grid(row=0,column=0)
    listText.grid(row=1,column=0)


    addFrame = Frame(window,borderwidth=10,highlightcolor="black",highlightbackground="black",highlightthickness=1)
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

    cartFrame = Frame(window)
    cartList = Text(cartFrame, width=30,height=20)
    cartLabel = Label(cartFrame,text="Cartesian Product")
    cartLabel.grid(row=0,column=0)
    cartList.grid(row=1,column=0)

    calcCart = Frame(window)
    calcLabel = Label(calcCart,text="Cartesian Sets")
    calcText = Entry(calcCart,width = 10)
    calcButton = Button(calcCart,command=calc,text="Calculate Cartesian Product")
    calcLabel.grid(row=0,column=0)
    calcText.grid(row=0,column=1)
    calcButton.grid(row=1,column=0)

    listFrame.grid(row=0, column=0)
    addFrame.grid(row=0, column=1)
    cartFrame.grid(row=0,column=2)
    calcCart.grid(row=1,column=1)

    window.mainloop()
