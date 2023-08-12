import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
import bcrypt

backgrounds = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

mac = tk.Tk()
mac.title("Login System")
mac.geometry("1250x700+210+100")
mac.config(bg=backgrounds)
mac.resizable(False, False)

# Simulated user and admin credentials
user_credentials = {"Azhar": "password1", "Ainee": "password2", "Masyii":"password3"}
admin_credentials = {"lc Amir": "adminpassword" , "Lc Jason": "adminpassword2"}

def login():
    username =user.get()
    password =password.get()

    if username in user_credentials and user_credentials[username] == password:
        messagebox.showinfo("Login", "Student login successful!")
    elif username in admin_credentials and admin_credentials[username] == password:
        messagebox.showinfo("Login", "Admin login successful!")
    else:
        messagebox.showerror("Login", "Invalid credentials")

#Password Encryption
def login():
    username = user.get()
    password = password.get()

    if username in user_credentials and bcrypt.checkpw(password.encode('utf-8'), user_credentials[username].encode('utf-8')):
        messagebox.showinfo("Login", "Student login successful!")
    elif username in admin_credentials and bcrypt.checkpw(password.encode('utf-8'), admin_credentials[username].encode('utf-8')):
        messagebox.showinfo("Login", "Admin login successful!")
    else:
        messagebox.showerror("Login", "Invalid credentials")

# Simulated user and admin credentials with hashed passwords
user_credentials = {
    "Azhar": bcrypt.hashpw("password1".encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
    "Ainee": bcrypt.hashpw("password2".encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
    "Masyii": bcrypt.hashpw("password3".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
}

admin_credentials = {
    "lc Amir": bcrypt.hashpw("adminpassword".encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
    "Lc Jason": bcrypt.hashpw("adminpassword2".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
}

# Icon Image
image_Icon = tk.PhotoImage(file="loginIcon.png")
mac.iconphoto(False, image_Icon)

# Background Image
frame = tk.Frame(mac, bg=framebg)
frame.pack(fill="both", expand=True)

backgroundImage = Image.open("login.jpg")
backgroundImage = ImageTk.PhotoImage(backgroundImage)
tk.Label(frame, image=backgroundImage).pack()

# User Entry
def user_enter(e):
    user.delete(0, 'end')

def user_leave(e):
    name = user.get()
    if name == 'Username':
        user.delete(0, 'end')
        user.insert(0, 'Username')

user = tk.Entry(frame, width=18, fg="black", border=0, bg="#fff", font=('Arial Bold', 24))
user.insert(0, 'Username')
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=500, y=315)

usernameImage=Image.open('username.png')
usernameLabel=tk.Label(tk.loginFrame,image=usernameImage,text='Username',compound='left'
                   ,font=('times new roman' ,20,'bold' ))
usernameLabel.grid(row=1,column=0,pady=10)

# Password Entry
def password_enter(e):
    password.delete(0, 'end')

def password_leave(e):
    name = password.get()
    if name == '':
        password.delete(0, 'end')
        password.insert(0, 'Password')

password =tk.Entry(frame, width=18, fg="black", border=0, bg="#fff", font=('Arial Bold', 24))
password.insert(0, 'Password')
password.bind("<FocusIn>", password_enter)
password.bind("<FocusOut>", password_leave)
password.place(x=500, y=360)

passwordImage=Image.open('password.png')
passwordLabel=tk.Label(tk.loginFrame,image=passwordImage,text='password',compound='left'
                   ,font=('times new roman',20,'bold'))
passwordLabel.grid(row=2,column=0,pady=10)

# Hide And Show Button (to be added)
button_mode=True

def hide():
    global button_mode

    if button_mode:
        eyeButton.config(image=closeeye,activebackground="white")
        code=tk.Entry(frame, show="*")
        button_mode=False
    else:
        eyeButton.config(image=openeye,activebackground="white")
        code.config(show="")
        button_mode=True

openeye=Image.open("eye.png")
closeeye=Image.open("closeEye.png")
eyeButton=tk.Button(frame,image=openeye,bg="#fff",bd=0,command=hide)
eyeButton.place(x=780,y=410)

#Login Button
loginButton=tk.Button(mac,text="LOGIN",bg="#A9A9A9",fg="white",width=10,height=1,font=("arial ",16,"bold"),bd=0)
loginButton.place(x=570,y=500)

mac.mainloop()
