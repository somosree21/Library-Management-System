from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from mysql.connector import connect
def loginfunc():
    x= id.get()
    y= pas.get()
    if x=='' or y=='':
        messagebox.showerror('Error','All fields are required')
    lib_database = connect(
        host='localhost', user='root', passwd='', database='lms_t'
    )
    cursor = lib_database.cursor()
    cursor.execute('select * from employee_details where EMPLOYEE_ID=%s and PASSWORD=%s',(x,y))
    data = cursor.fetchone()
    if data == None:
        messagebox.showerror('Error','Invalid details')
    else:
        messagebox.showinfo('success','you are logged in')
        root.destroy()
        import DEMO
    lib_database.commit()
    lib_database.rollback()
    lib_database.close()
def regfunc():
    root.destroy()
    import regi
root = Tk()
root.geometry('1366x800')
root.title('LIBRARY MANAGEMENT SYSTEM')
img = Image.open('library_new.jpeg')
photo = ImageTk.PhotoImage(img)
lab= Label(root,image = photo)
lab.place(x=0,y=0,relwidth=1,relheight=1)
Label(root,text='Employee I.D:',font='Times 15 bold', bg='black',fg='white').place(x=500,y=500)
Label(root,text='Password:',font='Times 15 bold', bg='black',fg='white').place(x=500,y=560)
id = StringVar()
pas = StringVar()
Entry(textvariable=id).place(x= 650, y=510)
Entry( textvariable=pas,show='*').place(x=650, y= 565)
Button(text= 'Login',activebackground= 'blue',activeforeground='white',fg='black',command= loginfunc).place(x=600,y=630)
Button(text= 'Register',activebackground= 'blue',activeforeground='white',fg='black', command = regfunc).place(x=660,y=630)
root.mainloop( )