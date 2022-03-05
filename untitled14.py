from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk

root=Tk()
root.geometry("800x800")
root.title("amogus")

label_heading=Label(root,text="Juice Center",bg="orange",font=("Sylfaen",18,"bold","italic"))
label_heading.place(relx=0.05,rely=0.1,anchor=W)

juice = ImageTk.PhotoImage(Image.open("logo.png"))
juice_image=Label(root,image=juice,bg="orange2")
juice_image.place(relx=0.2,rely=0.4,anchor=CENTER)

apple=ImageTk.PhotoImage(Image.open("apple_img.png"))
mango=ImageTk.PhotoImage(Image.open("mango_img.png"))
orange=ImageTk.PhotoImage(Image.open("orange.png"))

fruit_image=Label(root,bg="orange2")
fruit_image.place(relx=0.75,rely=0.8,anchor=CENTER)

label_name=Label(root,text="Select fruit",bg="orange2",font=("BahnschriftLight",15))
label_name.place(relx=0.6,rely=0.2,anchor=E)

fruit_list=["apple","mango","orange"]
fruit_dropdown=ttk.Combobox(root,state="readonly",values=fruit_list,justify="right")
fruit_dropdown.place(relx=0.95,rely=0.25,anchor=E)

label_quantity=Label(root,text="enter quantity",bg="orange2",font=("BahnschriftLight",15))
label_quantity.place(relx=0.96,rely=0.35,anchor=E)

quantity_dropdown=Entry(root)
quantity_dropdown.place(relx=0.95,rely=0.4,anchor=E)

label_show_amount=Label(root,bg="orange2",font=("BahnschriftLight",12))
label_show_amount.place(relx=0.95,rely=0.7,anchor=E)

label_show_quantity=Label(root,bg="orange2",font=("BahnschriftLight",12))
label_show_quantity.place(relx=0.95,rely=0.8,anchor=E)

class juice():
    def __init__(self,fruit,quantity):
        self.SELFfruit=fruit
        self.SELFfruitquantity=quantity
        self.__SELFfruitcost=250
    def __calculatecost(self):
        calories=0
        print(str(self.SELFfruitquantity)+"x"+str(self.__SELFfruitcost))
        cost=str(int(self.__SELFfruitcost)*int(self.SELFfruitquantity))
        label_show_amount["text"]="You need to pay: $"+cost
        if (self.SELFfruit=="Apple"):
            calories=self.SELFfruitquantity*52
            fruit_image['image']=apple
        if (self.SELFfruit=="Orange"):
            calories=self.SELFfruitquantity*40
            fruit_image['image']=mango
        if (self.SELFfruit=="Pinapple"):
            calories=self.SELFfruitquantity*80
            fruit_image['image']=orange
        label_show_quantity['text']=""+"X"+str(self.SELFfruitquantity)+"="+str(calories)+" calories"
        print(str(calories)+" calories")
        print(str(cost)+" USD")
    def getcost(self):
        self.__calculatecost()
def getjuice():
    fruit=fruit_dropdown.get()
    quantity=quantity_dropdown.get()
    print(fruit)
    print(quantity)
    obj1=juice(fruit,quantity)
    obj1.getcost()
Btn=Button(root,text="order 200 chunguses",command=getjuice)
Btn.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()