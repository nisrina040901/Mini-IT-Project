from tkinter import * 
from tkinter.ttk import *

root = Tk()
root.geometry("1920x1080")

def timetable():
    global ttwindow
    ttwindow = Toplevel()
    ttwindow.geometry("1920x1080")
    ttwindow.title("Timetable")
    root.iconify()
    
    ttframe = Frame(ttwindow)
    ttframe.grid(row = 0, column = 0)
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    for i in range(len(days)):
        label = Label(ttframe, text = days[i], borderwidth = 1)
        label.grid(row = i+1, column = 0, padx = 10, pady = 10)

    times = ["08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00"]
    for j in range(len(times)):
        label = Label(ttframe, text = times[j], borderwidth = 1, width = 20)
        label.grid(row = 0, column = j+1, padx = 10, pady = 10)

    ttwindow.protocol("WM_DELETE_WINDOW",ttclose)
    ttwindow.mainloop

courseData = [
    {"name": "PMT0301 - Mathematics 3", "time": "10:00", "place": "CNMX1002", "day": "Thursday", "group": "TC1L"},
    {"name": "PSP0201 - Mini IT Project", "time": "14:00", "place": "FCICQAR3006", "day": "Monday", "group": "TC1L"},
    {"name": "PEN0065 - Academic English", "time": "12:00", "place": "FOECQCR2045", "day": "Tuesday", "group": "FCI1"}
]

def updateInfo(course_index):
    courseInfo = courseData[course_index]
    info_label.config(text = f"Time: {courseInfo['time']}\nPlace: {courseInfo['place']}\nDay: {courseInfo['day']}\nGroup: {courseInfo['group']}")

def select(event):
    selected = Courses.curselection()
    if selected:
        updateInfo(selected[0])

def view_courses():
    global vcwindow, Courses, Info, info_label
    vcwindow = Toplevel()
    vcwindow.geometry("1920x1080")
    vcwindow.title("Course Registration")
    root.iconify

    Courses = Listbox(vcwindow, width = 100)
    Courses.grid(row = 0, column = 0)

    for course in courseData:
        Courses.insert(END, course["name"])
    Courses.bind("<<ListboxSelect>>", select)
    
    Info = Frame(vcwindow)
    Info.grid(row = 1, column = 0)

    info_label = Label(Info, text = "Select a Course from the list.")
    info_label.pack()

    vcwindow.protocol("WM_DELETE_WINDOW", ttclose)
    vcwindow.mainloop()

def ttclose():
    root.deiconify()
    ttwindow.destroy()

def vcclose():
    root.deiconify
    vcwindow.destroy

def student():
    frame1 = Frame(root)
    frame1.place(relx = 0.5, rely = 0.3, anchor = CENTER)
    option1 = Button(frame1, text="View and Register Courses", width = 100, command = view_courses)
    option1.grid(row = 0, column = 0, padx = 5, pady = 5)
    
    option2 = Button(frame1, text="View Timetable", width = 100, command = timetable)
    option2.grid(row = 1, column = 0, padx = 5, pady = 5)
       
    root.mainloop()

student()