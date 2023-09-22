#pip install tkinter
from tkinter import*
#pip install pyperclip
import pyperclip
import random
 
root =Tk()
root.geometry(700*190)
password=StringVar()
passlen=IntVar()
passlen.set(0)



def generate():   #function generate the password
  def pass1():
    pass1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
    '1','2','3','4','5','6','7','8','9','0'
    '!','@','#','$','%','^','&','*','(',')','{','}','[',']']
password=""
for x in range(passlen.get()):
    password=password+random.choice(pass1)
    password.set(password)
    #function to copy the password
def copyclipboard():
    random_password=password.get()
    pyperclip.copy(random_password)
    #labels
    Label(root,text="strong password generator",font="courier 30 bold").pack()
    Label(root,text="enter the number to get password").pady(pady=7)
    Button(root,textvariable=passlen).pady(pady=3)
    Entry(root,textvariable=password).pady(pady=3)
    Button(root,text="tap to copyboard",command=copyclipboard).pack()
    root.mainloop()



