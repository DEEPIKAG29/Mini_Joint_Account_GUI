from tkinter import *

win = Tk()
win.geometry("400x300")
win.title("Mini_Joint_Account")
win.resizable(False,False)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __add__(self, other):
        # Merge balances into a new joint account
        return BankAccount(f"{self.owner} & {other.owner}", self.balance + other.balance)

    def __str__(self):
        return f"{self.owner}: ${self.balance}"

def submit_action():
    try:
        #convert Amounts to Numberss
        acc1 = BankAccount(name1.get(), float(amt1.get()))
        acc2 = BankAccount(name2.get(), float(amt2.get()))
        result.set(str(acc1+acc2))
    except ValueError:
        #Handle Invalid Input
        result.set("Please enter valid numeric amounts!")

#Heading
head_bg = Frame(win, height = 50, bg = "pink")
head_bg.pack(side = "top", fill = X)

head_txt = Label(win, text = "Mini Joint Account", bg = "pink", font = ("Bell MT", 15, "bold"))
head_txt.place(x = 100, y= 12)

#First Account Holder
lb1 = Label(win, text = "Enter name of First Account Holder : ", font = ("Bell MT", 10, "bold"))
lb1.place(x = 30, y= 60)

name1 = StringVar()
txt1 = Entry(win, textvariable = name1)
txt1.place(x = 250, y= 60)

#Amount1
lb2 = Label(win, text = "Enter Amount : ", font = ("Bell MT", 10, "bold"))
lb2.place(x = 30, y= 85)

amt1 = StringVar()
txt2 = Entry(win, textvariable = amt1)
txt2.place(x = 250, y= 85)

#Second Account Holder
lb3 = Label(win, text = "Enter name of Second Account Holder : ", font = ("Bell MT", 10, "bold"))
lb3.place(x = 30, y= 120)

name2 = StringVar()
txt3 = Entry(win, textvariable = name2)
txt3.place(x = 250, y= 120)

#Amount2
lb4 = Label(win, text = "Enter Amount : ", font = ("Bell MT", 10, "bold"))
lb4.place(x = 30, y= 145)

amt2 = StringVar()
txt4 = Entry(win, textvariable = amt2)
txt4.place(x = 250, y= 145)

#Submit Button
sub = Button(win, text = "Submit", command = submit_action)
sub.place(x = 170, y= 180)

#Result
lb5 = Label(win, text = "The Joint Account Holders \nand Total Amount : ", font = ("Bell MT", 11, "bold"))
lb5.place(x = 30, y= 220)

result = StringVar()
lb6 = Label(win, textvariable = result)
lb6.place(x = 225, y= 223)

#Thankyou message
foot_bg = Frame(win, height = 25, bg = "pink")
foot_bg.pack(side = "bottom", fill = X)

foot_txt = Label(win, text = "--Thank you for visitng--", bg = "pink", font = ("Bell MT", 10, "bold"))
foot_txt.place(x = 130, y= 275)
