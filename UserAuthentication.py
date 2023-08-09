import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk

# Create the main window
mac = tk.Tk()
mac.title("Login")

# Simulated user and admin credentials
user_credentials = {"Azhar": "password1", "Ainee": "password2", "Masyii":"password3"}
admin_credentials = {"lc Amir": "adminpassword" , "Lc Jason": "adminpassword2"}

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in user_credentials and user_credentials[username] == password:
        messagebox.showinfo("Login", "Student login successful!")
    elif username in admin_credentials and admin_credentials[username] == password:
        messagebox.showinfo("Login", "Admin login successful!")
    else:
        messagebox.showerror("Login", "Invalid credentials")

# Create background size when pop out
mac.geometry('1280x700+0+0')

mac.resizable(False,False)

#background color
mac.title("Login")
background_color = "lightblue"
mac.configure(bg=background_color)
#background_color.place(x=0, y=0)

#Place the username and password 
loginFrame=tk.Frame(mac,bg='lightblue')
loginFrame.place(x=400,y=150)


# Create the loginFrame
#loginFrame = tk.Frame(mac, width=300, height=200, bg="lightgray")  # Adjust width, height, and background color
#loginFrame.place(x=400, y=150)


# Create and place widgets
username_label = tk.Label(mac, text="Username:")
username_label.pack()

username_entry = tk.Entry(mac)
username_entry.pack()

password_label = tk.Label(mac, text="Password:")
password_label.pack()

password_entry = tk.Entry(mac, show="*")
password_entry.pack()

login_button = tk.Button(mac, text="Login", command=login)
login_button.pack()

# Start the main loop
mac.mainloop()
