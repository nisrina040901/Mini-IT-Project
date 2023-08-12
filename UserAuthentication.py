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

#Password Encryption
def login():
    username = user.get()
    entered_password = password.get()

    # Check if the username exists
    if username in user_credentials:
        # Hash the entered password and compare it to the stored hash
        if bcrypt.checkpw(entered_password.encode('utf-8'), user_credentials[username].encode('utf-8')):
            messagebox.showinfo("Login", "Student login successful!")
            return

    # Check if the username exists in admin_credentials
    if username in admin_credentials:
        # Hash the entered password and compare it to the stored hash
        if bcrypt.checkpw(entered_password.encode('utf-8'), admin_credentials[username].encode('utf-8')):
            messagebox.showinfo("Login", "Admin login successful!")
            return

    # Invalid credentials
    messagebox.showerror("Login", "Invalid credentials")

# Simulated user and admin credentials with hashed passwords
user_credentials = {
    "Azhar": bcrypt.hashpw("password1".encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
    "Ainee": bcrypt.hashpw("password2".encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
    "Masyii": bcrypt.hashpw("password3".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
}

admin_credentials = {
    "Lc Amir": bcrypt.hashpw("adminpassword".encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
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

#Students Icon
studentIcon=Image.open("graduated.png")
studentIcon= ImageTk.PhotoImage(studentIcon)
studentIconLabel = tk.Label(frame, image=studentIcon)
studentIconLabel.place(x=555, y=155)

# User Entry
def user_enter(e):
    user.delete(0, 'end')

def user_leave(e):
    name = user.get()
    if name == 'Username' or name == '':
        user.delete(0, 'end')
        user.insert(0, 'Username')

user = tk.Entry(frame, width=18, fg="black", border=0, bg="#fff", font=('Arial Bold', 24))
user.insert(0, 'Username')
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=500, y=315)

usernameImage = Image.open('username.png')
usernamePhotoImage = ImageTk.PhotoImage(usernameImage)
usernameLabel = tk.Label(frame, image=usernamePhotoImage, text='password', compound='left', font=('times new roman', 20, 'bold'))
usernameImage = Image.open('username.png')
usernamePhotoImage = ImageTk.PhotoImage(usernameImage)
usernameLabel = tk.Label(frame, image=usernamePhotoImage)
usernameLabel.image = usernamePhotoImage  # Store a reference to the image to prevent it from being garbage collected
usernameLabel.place(x=450, y=315)  # Place the label on the frame

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

passwordImage = Image.open('password.png')
passwordPhotoImage = ImageTk.PhotoImage(passwordImage)
passwordLabel = tk.Label(frame, image=passwordPhotoImage, text='password', compound='left', font=('times new roman', 20, 'bold'))
passwordImage = Image.open('password.png')
passwordPhotoImage = ImageTk.PhotoImage(passwordImage)
passwordLabel = tk.Label(frame, image=passwordPhotoImage)
passwordLabel.image = passwordPhotoImage  # Store a reference to the image to prevent it from being garbage collected
passwordLabel.place(x=450, y=360)  # Place the label on the frame

# Hide And Show Button (to be added)
button_mode=True

def hide():
    global button_mode

    if button_mode:
        eyeButton.config(image=closeeye, activebackground="white")
        password.config(show="*")
        button_mode = False
    else:
        eyeButton.config(image=openeye, activebackground="white")
        password.config(show="")
        button_mode = True


openeye=Image.open("OpenEye.png")
openeye = ImageTk.PhotoImage(openeye)
openeyeLabel = tk.Label(frame, image=openeye)

closeeye=Image.open("CloseEye.png")
closeeye= ImageTk.PhotoImage(closeeye)
passwordLabel = tk.Label(frame, image=closeeye)

eyeButton=tk.Button(frame,image=openeye,bg="#fff",bd=0,command=hide)
eyeButton.place(x=724,y=360)

#Login Button
loginButton = tk.Button(mac, text="LOGIN", bg="#A9A9A9", fg="black", width=10, height=1, font=("arial", 16, "bold"), bd=0, command=login)
loginButton.place(x=550, y=450)

mac.mainloop()
