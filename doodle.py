from tkinter import * 
from tkinter.ttk import *

root = Tk()
root.geometry("1920x1080")

def CoursesList():
        vc = Toplevel()
        vc.geometry("1920x1080")
        
        
        Courses = Listbox(vc, width = 100)  
        Courses.insert(1, "PSP0201 - MINI IT PROJECT")
        Courses.insert(2, "PMT0301 - MATHEMATICS III")
        Courses.insert(3, "PEN0065 - ACADEMIC ENGLISH")

        Courses.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        vc.mainloop
        root.iconify()

def StudentsList():
        vs = Toplevel()
        vs.geometry("1920x1080")
        Students = Listbox(vs,width = 100)
        
        while False:
                with open("Students.txt") as SFile:
                        SData = SFile.read()
                        SList = SData.split("\n")
                Students = Listbox(vs)
                i = 0
                j = 1
                while True: 
                        Students.insert(j,SList[i])
                        i = i + 1
                        j = j + 1
                        if i == len(SList):
                                break
        
        vs.mainloop
        root.iconify()

def admin():
    option1 = Button(root, text="View Courses", width = 100, command = CoursesList)
    option1.place(relx = 0.5, rely = 0.1, anchor = CENTER)
    
    option2 = Button(root, text="View Students", width = 100, command = StudentsList)
    option2.place(relx = 0.5, rely = 0.13, anchor = CENTER)
    
    
    
    
    root.mainloop()
    

admin()