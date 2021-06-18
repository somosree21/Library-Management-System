from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk, Image
from mysql.connector import connect

def doregister():
     if one.get() == "" or two.get() == "" or three.get() == "" or four.get() == "" or five.get()== "":
        messagebox.showerror("Error", "Given fields are required")
        return
     elif check.get() ==0:
         messagebox.showerror('Error','You need to agree to our terms and conditions')
         return
     passs= four.get()
     conf = con.get()
     if passs != conf:
         messagebox.showerror('Error','Passwords do not match!')
     else:
         empid= emid.get()
         conf = con.get()
         lib_database = connect(
             host='localhost',user='root',password= '', database='lms_t'
         )
         cursor= lib_database.cursor()
         sql = "insert into employee_details (EMPLOYEE_ID, PASSWORD) values (%s,%s)"
         val= (empid,conf)
         cursor.execute(sql,val)
         lib_database.commit()
         lib_database.rollback()
         lib_database.close()
         messagebox.showinfo('Success', 'You have registered succesfully!')
def dologin():
    reg.destroy()
    import Login.py

reg= Tk()
reg.geometry('1366x800')
reg.title('Registration Page')
reg.configure(background = 'cyan')
top= Frame(bd=6, relief = RIDGE)
top.place(x=5,y=5,width=1360,height=200)
head= Label(text="Welcome to registration page",font=("Montoype Corsiva",20,'bold','italic'),fg='white', bg='darkblue')
head.place(x=30,y=85,width=1300)
i= Image.open('register 2.jpeg')
im= i.resize((1360,200),Image.ANTIALIAS)
img = ImageTk.PhotoImage(im)
x= Label(top,image = img)
x.place(x=0,y=0,relwidth=1,relheight=1)
frm = Frame(reg,bd=5,relief = GROOVE,bg ='white')
frm.place(x=200,y=220,width=1020,height= 500)
txt = Label(frm,text = 'REGISTER HERE!', font= 'MonotypeCorsiva 15 bold', bg= 'yellow',fg='black',bd=8, relief = RAISED)
txt.place(x=50,y=5, width=900 )
fname= Label(frm,text= 'First Name:', font=("Copperplate Gothic",15,'bold'),bg ='white')
fname.place(x=50,y=100)
one= StringVar()
two= StringVar()
three= StringVar()
four= StringVar()
five= StringVar()
first= Entry(frm, bd=5,relief= SUNKEN,font=("Cooper", 14,"bold"),textvariable = one)
first.place(x=180,y=100,width=300)
lname= Label(frm,text= 'Last Name:', font=("Copperplate Gothic",15,'bold'),bg ='white')
lname.place(x=500,y=100)
last=Entry(frm,bd=5,relief= SUNKEN,font=("Cooper", 14,"bold"),textvariable = two)
last.place(x=630,y=100,width=300)
eid= Label(frm,text= 'Employee I.D:', font=("Copperplate Gothic",15,'bold'),bg ='white')
eid.place(x=45,y=200)
emid= Entry(frm,bd=5,relief= SUNKEN,font=("Cooper", 14,"bold"),textvariable = three)
emid.place(x=180,y=200,width=300)
p= Label(frm,text= 'Password:', font=("Copperplate Gothic",15,'bold'),bg ='white')
p.place(x=500,y=200)
paswd= Entry(frm,bd=5,relief= SUNKEN,font=("Cooper", 14,"bold"),show ='*',textvariable = four)
paswd.place(x=630,y=200,width=300)
c= Label(frm,text= 'Confirm Password:', font=("Copperplate Gothic",15,'bold'),bg ='white')
c.place(x=200,y=300)
con= Entry(frm,bd=5,relief= SUNKEN,font=("Cooper", 14,"bold"),show = "*",textvariable = five)
con.place(x=400,y=295,width=300)
check =IntVar()
c1 = Checkbutton(frm,variable = check, offvalue= 0,onvalue=1,text="I agree to the library terms and conditions", bg='white')
c1.place(x=400,y=350)
register = Button(bg='red',fg='black',font = ("Lucida Bright", 18, 'bold'), text='REGISTER',activebackground='blue',command= doregister)
register.place(x=530, y= 650)
login = Button(bg='red',fg='black',font = ("Lucida Bright", 18, 'bold'), text='LOGIN',activebackground='blue',command= dologin)
login.place(x=700, y= 650)

reg.mainloop()