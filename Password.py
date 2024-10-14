from tkinter import *
from tkinter import messagebox


window= Tk()
window.title("LOCK")
window.config(padx=50,pady=50,bg="white")
import random
import pyperclip
import json

def generator():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','@',"#","4",'%',"^",'&',"*",'(',')']

    l = random.randint(8,10)
    n = random.randint(2,4)
    s = random.randint(2,4)

    p_list = []

    for c in range(l):
        p_list.append(random.choice(letters))

    for no in range(n):
        p_list.append(random.choice(numbers))

    for sym in range(s):
        p_list.append(random.choice(symbols))

    random.shuffle(p_list)

    password = ""
    for i in p_list:
        password += i
    b3.insert(0,password)
    pyperclip.copy(password)
    # print(f"Your Password: {password}")





def save():
    website = b1.get()
    email = b2.get()
    password = b3.get()
    new_data = {
        website: {
            "email": email,
            "password" : password,
        }
    } 

    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please Fill All The Details!")
    else:
        ok = messagebox.askokcancel(title=website,message=f"Details Entered by You are: \n Email: {email} \n Password: {password} \n If All The Information is Correct Then Press OK!")
        if ok:
            def load():
                try:
                    with open("projects/tkinter/data.json","r") as data:
                        info = json.load(data)
                        info.update(new_data)
                except:
                    with open("projects/tkinter/data.json","w") as data:
                        json.dump(new_data, data, indent=4)
                else:
                    with open("projects/tkinter/data.json","w") as data:
                        json.dump(info, data, indent=4)         
                finally:
                    b1.delete(0,END)
                    b3.delete(0,END)
            load()          

def search():
    website = b1.get()
    try:
        with open("projects/tkinter/data.json","r") as data:
            info = json.load(data)
    except:
        messagebox.showerror(title="Error" ,message="File Not Found!")
            
    
    else:
        if website in info:
            email = info[website]["email"]
            password = info[website]["password"]
            messagebox.showinfo(title="searched data", message=f"Email : {email}\n Password : {password}")
        else:
            messagebox.showerror(title="Error" ,message="No Data Found!")

        

canva = Canvas(width=300,height=350,bg="white",highlightthickness=0)

pic = PhotoImage(file="projects/tkinter/lock.png")
canva.create_image(155,155, image = pic)
canva.create_text(150,30, text = "PASSLOCK", font=("courier",35,"bold"), fill="dark blue")
canva.grid(row=0,column=1)

web = Label(text="Website : ", font=("Arial",20,"bold"),highlightthickness=0,bg="white")
user = Label(text="Email/Username : ", font=("Arial",20,"bold"),highlightthickness=0,bg="white")
pas = Label(text="Password : ", font=("Arial",20,"bold"),highlightthickness=0,bg="white")
b1 = Entry(width=17,font=("Arial",20,"normal"))
b2 = Entry(width=36,font=("Arial",20,"normal"))
b3 = Entry(width=17,font=("Arial",20,"normal"))
b2.insert(0,"new@gmail.com")
web.grid(row=1,column=0)
user.grid(row=2,column=0)
pas.grid(row=3,column=0)
b1.grid(row=1,column=1)
b2.grid(row=2,column=1,columnspan=2)
b3.grid(row=3,column=1)

but = Button(text="Generate Password",font=("Arial",20,"bold"),command=generator)
but1 = Button(text="Add",font=("Arial",20,"bold"),width=30, command=save)
but2 = Button(text="Search",font=("Arial",20,"bold"),width=16,command=search)
but.grid(row=3,column=2)
but2.grid(row=1,column=2)
but1.grid(row=4,column=1,columnspan=2)

window.mainloop()