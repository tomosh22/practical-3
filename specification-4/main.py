from tkinter import Tk,Button,Entry,Label,Frame,Text,END,messagebox
from calc import *
def add(name,values,text,sets):
    if "" in [name.get(),values.get()]:
        messagebox.showinfo("No name and value","Please enter a name and values")
        return
    text.insert(END,name.get()+":{"+values.get()+"}\n")
    sets.append(Set(values.get().split(","),name.get()))
    name.delete(0,"end")
    values.delete(0,"end")

def calc(sets,set_ids,cartList):
    cartList.insert(END,cart_product(sets,set_ids))
if __name__ == "__main__":
    window = Tk()
    sets = []

    listFrame = Frame(window)
    listText = Text(listFrame, width=20,height=10)
    listLabel = Label(listFrame,text = "Sets")
    listLabel.grid(row=0,column=0)
    listText.grid(row=1,column=0)


    addFrame = Frame(window,borderwidth=10,highlightcolor="black",highlightbackground="black",highlightthickness=1)
    addTextInstruct = Label(addFrame,text="Input values seperated by commas, e.g '1,2,3,4'")
    addTextName = Entry(addFrame, width=5)
    addTextNameLabel = Label(addFrame, text="Set Name")
    addTextSet = Entry(addFrame, width=30)
    addTextSetLabel = Label(addFrame, text="Set values")
    addButton = Button(addFrame, width=10, command=lambda:add(addTextName,addTextSet,listText,sets), text="Add Set")
    addTextNameLabel.grid(row=0, column=0)
    addTextName.grid(row=0, column=1)
    addTextInstruct.grid(row=1,column=0)
    addTextSetLabel.grid(row=2, column=0)
    addTextSet.grid(row=2, column=1)
    addButton.grid(row=3, column=0)

    cartFrame = Frame(window)
    cartList = Text(cartFrame, width=50,height=10)
    cartLabel = Label(cartFrame,text="Cartesian Product")
    cartLabel.grid(row=0,column=0)
    cartList.grid(row=1,column=0)

    calcCart = Frame(window,borderwidth=10,highlightcolor="black",highlightbackground="black",highlightthickness=1)
    calcInstruct = Label(calcCart,text="Input sets seperated by commas, e.g 'a,b,c'")
    calcLabel = Label(calcCart,text="Cartesian Sets")
    calcText = Entry(calcCart,width = 10)
    calcButton = Button(calcCart,command=lambda:calc(sets, calcText.get().split(","),cartList),text="Calculate Cartesian Product")
    calcInstruct.grid(row=0,column=0)
    calcLabel.grid(row=1,column=0)
    calcText.grid(row=1,column=1)
    calcButton.grid(row=2,column=0)

    listFrame.grid(row=0, column=0)
    addFrame.grid(row=0, column=1)
    cartFrame.grid(row=0,column=2)
    calcCart.grid(row=1,column=1)

    window.mainloop()
