from tkinter import * 
import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
from tkcalendar import Calendar

backgrounds = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

admin = tk.Tk()


#Styling
admin.title("Admin Page")
admin.geometry("535x300")
bg = tk.PhotoImage(file = "login.png")
bglabel = tk.Label(admin, image=bg)
bglabel.grid()

image_Icon = tk.PhotoImage(file="AdminIcon.png")
admin.iconphoto(False, image_Icon)

# Create a database
studDBcon = sqlite3.connect("studentInfo.db")
studDB = studDBcon.cursor()

#create table
'''
studDB.execute("""CREATE TABLE studentdb(
                name text,
                studentId integer,
                effectiveDate text,
                academicProgram string,
                subjectTaking text,
                status text
                )""")
'''

def subAddStud():
    studDBcon = sqlite3.connect("studentInfo.db")
    studDB = studDBcon.cursor()
    if len(studentId.get()) == 10:
        try:
            int(studentId.get())
            studDB.execute("INSERT INTO studentdb VALUES (:name, :studentId, :effectiveDate, :academicProgram, :subjectTaking, :status)",
                            {
                                "name" : name.get(),
                                "studentId" : studentId.get(),
                                "effectiveDate" : selectedD,
                                "academicProgram" : clicked.get(),
                                "subjectTaking" : subjectTaking.get(),
                                "status" : status.get(),
                            })
            name.delete(0, END)
            studentId.delete(0, END)
            dateL.config(text="")
            clicked.set(opt[0])
            subjectTaking.delete(0, END)
            status.delete(0, END)
        except ValueError:
            msg.config(text="Invalid format for \"Student ID\", please check again.")
    else:
        msg.config(text="Invalid input for \"Student ID\", please check again.")

    studDBcon.commit()
    studDBcon.close()

def selectDate():
    global selectedD
    selectedD = effectiveDate.get_date()
    dateL.config(text="Successfully selected " + selectedD + " as \"Effective Date\"")
    # print(selectedD)

def addStudent():
    global name
    global studentId
    global effectiveDate
    global academicProgram
    global subjectTaking
    global status

    global dateL
    global clicked
    global opt

    global msg

    addStudentW = Toplevel()
    addStudentW.title("Add Student")
    image_Icon = tk.PhotoImage(file="AdminIcon.png")
    addStudentW.iconphoto(False, image_Icon)

    name = tk.Entry(addStudentW, width=30)
    name.grid(row=0, column=1, padx=20, pady=(10, 0))
    studentId = tk.Entry(addStudentW, width=30)
    studentId.grid(row=1, column=1, padx=20)
    effectiveDate = Calendar(addStudentW, selectmode = "day", date_pattern="yyyy-mm-dd")
    effectiveDate.grid(row=2, column=1, padx=20)
    selectBtn = Button(addStudentW, text="Select Date", command=selectDate) 
    selectBtn.grid(row=3, column=0, columnspan=2, pady=10)
    opt = ["Foundation in IT", "Degree in Software Engineering"]
    clicked = StringVar()
    clicked.set(opt[0])
    academicProgram = OptionMenu(addStudentW, clicked, *opt)
    academicProgram.grid(row=5, column=1, padx=20)
    subjectTaking = Checkbutton(addStudentW, width=30)
    subjectTaking.grid(row=6, column=1, padx=20)
    # subjectTaking = tk.Entry(addStudentW, width=30)
    # subjectTaking.grid(row=6, column=1, padx=20)
    status = tk.Entry(addStudentW, width=30)
    status.grid(row=7, column=1, padx=20)

    #create text box label
    nameL = tk.Label(addStudentW, text="Name")
    nameL.grid(row=0, column=0, pady=(10, 0))
    studentIdL = tk.Label(addStudentW, text="Student ID")
    studentIdL.grid(row=1, column=0)
    effectiveDateL = tk.Label(addStudentW, text="Effective Date")
    effectiveDateL.grid(row=2, column=0)
    dateL = tk.Label(addStudentW, text="")
    dateL.grid(row=4, column=0, columnspan=2)
    academicProgramL = tk.Label(addStudentW, text="Academic Program")
    academicProgramL.grid(row=5, column=0)
    subjectTakingL = tk.Label(addStudentW, text="Subject Taking")
    subjectTakingL.grid(row=6, column=0)
    statusL = tk.Label(addStudentW, text="Status")
    statusL.grid(row=7, column=0)

    subAddStudBtn = Button(addStudentW, text="Submit", command=subAddStud)
    subAddStudBtn.grid(row=8, column=0, columnspan=2, pady=10)

    msg = Label(addStudentW, text="")
    msg.grid(row=9, column=0, columnspan=2, pady=10)

studDBcon.commit()
studDBcon.close()

studentsFrame = tk.LabelFrame(admin, text="Students", padx=15, pady=50, bg="#06283D", fg="white")
studentsFrame.place(x=20, y=20)

addSBtn = tk.Button(studentsFrame, text="Add Student", command=addStudent)
addSBtn.grid(row=0, padx=20, pady=10)
removeSBtn = tk.Button(studentsFrame, text="Remove Student")
removeSBtn.grid(row=1, padx=20, pady=10)
updateSBtn = tk.Button(studentsFrame, text="Update Student's Status")
updateSBtn.grid(row=2, padx=20, pady=10)

courseFrame = tk.LabelFrame(admin, text="Course", padx=15, pady=50, bg="#06283D", fg="white")
courseFrame.place(x=280, y=20)

addCBtn = tk.Button(courseFrame, text="Add Course")
addCBtn.grid(row=0, padx=20, pady=10)
removeCBtn = tk.Button(courseFrame, text="Remove Course")
removeCBtn.grid(row=1, padx=20, pady=10)
updateCBtn = tk.Button(courseFrame, text="Update Course's Information")
updateCBtn.grid(row=2, padx=20, pady=10)

admin.mainloop()
