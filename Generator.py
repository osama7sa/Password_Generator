"""""
Characteristics of strong passwords
At least 8 characters—the more characters, the better.
A mixture of both uppercase and lowercase letters.
A mixture of letters and numbers.
Inclusion of at least one special character, e.g., ! @ # ? ] Note: do not use < or > in your password, as both can cause problems in Web browsers.
"""""
from tkinter import *
import random as R


Numbers="0123456789"
Characters='abcdefghijklmnopqrstuvwxyz'
Characters_Upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Symbols='_-@#?!'
AGG=Symbols+Characters+Characters_Upper+Numbers

def Strong_Password(level):# this function will generate the password
    global AGG
    if level==1:
        S="".join(R.sample(AGG,16))
        show(S)
    elif level==2:
        S = "".join(R.sample(AGG, 12))
        show(S)

    elif level==3:
        S = "".join(R.sample(AGG, 8))
        show(S)

    else:
        S = "".join(R.sample(AGG, int(level)))
        show(S)


def show(password):#function to show the password in the screen

    list_box.insert(END,password)


def custom_password():
    custom_label = Label(text="Number of characters")
    custom_label.grid(row=2, column=6)
    custom_input = Entry()
    custom_input.grid(row=3, column=6)
    enter_button = Button(text="Enter", width=7, command=lambda: Strong_Password(custom_input.get()))
    enter_button.grid(row=3, column=7, )

def Reset():
    list_box.delete(0,END)



#UI

Ui=Tk()
Ui.title("Password Generator")
Ui.geometry("500x300")
level_label = Label(text="press the level of the password:",font=("Arial", 15))
level_label.grid(row=0, column=0)
very_strong_button=Button(text="Very strong",width=15,command=lambda:Strong_Password(1))
very_strong_button.grid(row=1, column=0)

strong_button=Button(text="Strong",width=15,command=lambda:Strong_Password(2))
strong_button.grid(row=2, column=0,)

mid_button=Button(text="Mid",width=15,command=lambda:Strong_Password(3))
mid_button.grid(row=3, column=0)

custom_button=Button(text="Custom",width=15,command=custom_password)
custom_button.grid(row=3, column=0)

list_box = Listbox(width=22, selectmode=SINGLE)
list_box.grid(row=5, column=6, rowspan=5)

reset_button=Button(text="Reset",width=15,command=Reset)
reset_button.grid(row=4, column=0)


Ui.mainloop()
