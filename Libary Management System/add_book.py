from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk
from tkinter import simpledialog
def add_dt():
    if bk_n.get() == "" or bk_au.get() == ""  :
        messagebox.showerror("Error", "Given fields are required")
    else:
        bkis = bk_isbn.get()
        bnm = bk_n.get()
        bkau = bk_au.get()
        db = mysql.connector.connect(host="localhost", user="root", password="", database="lms_t")
        mycursor = db.cursor()
        sql = "SELECT b_name,auth FROM book_details"
        mycursor.execute(sql)
        dt = mycursor.fetchall()
        flag=False
        for i in range(len(dt)):
            if dt[i][0]==bnm and dt[i][1]==bkau:
                flag=True
                break
        if flag==True:
            x = simpledialog.askinteger(title="quantity",prompt="Enter the quantity:")
            for lop in range(x):
                mycursor = db.cursor()
                sql = "insert into book_details(b_name,auth,isbn)values(%s,%s,%s)"
                val = (bnm, bkau,bkis)
                mycursor.execute(sql, val)
                db.commit()
                bkis = int(bkis) + 1
            messagebox.showinfo("information", "Record Inserted successfully")
            bk_n.delete(0, END)
            bk_au.delete(0, END)
            bk_publi.delete(0, END)
            bk_n.focus_set()
        else:
            try:
                mycursor = db.cursor()
                sql = "insert into book_details(b_name,auth,isbn)values(%s,%s,%s)"
                val = (bnm,bkau,bkis)
                mycursor.execute(sql,val)
                db.commit()
                messagebox.showinfo("information", "Record Inserted successfully")
                bk_n.delete(0, END)
                bk_au.delete(0, END)
                bk_publi.delete(0,END)
                bk_n.focus_set()
            except EXCEPTION as e:
                print(e)
                messagebox.showerror("No connection","Data can not be inserted")
                db.rollback()
                db.close()
            ab.destroy()
def add_close():
    ab.destroy()

ab=Tk()
ab.title("Add Book")
ab.geometry("600x400+600+300")
bok_frame=Frame(ab,bg="light blue")
bok_frame.place(x=5,y=5,width=600,height=400)
bok_title=Label(bok_frame,text="Add Book Details",font=("Comic Sans MS",20,"bold","underline"),fg="black",bg="light blue")
bok_title.grid(row=0,columnspan=4,padx=200)
bk_n=Label(bok_frame,text="Book Name",font=("Times New Roman",15,"bold"),bg="light blue")
bk_n.grid(row=1,column=0,pady=10)
bk_au=Label(bok_frame,text="Author Name",font=("Times New Roman",15,"bold"),bg="light blue")
bk_au.grid(row=2,column=0,pady=10)
bk_publi=Label(bok_frame,text="Publisher",font=("Times New Roman",15,"bold"),bg="light blue")
bk_publi.grid(row=3,column=0,pady=10)
bk_isbn=Label(bok_frame,text="ISBN Number",font=("Times New Roman",15,"bold"),bg="light blue")
bk_isbn.grid(row=4,column=0,pady=10)
#bk_qu=Label(bok_frame,text="Quantity",font=("Times New Roman",15,"bold"),bg="light blue")
#bk_qu.grid(row=5,column=0,pady=10)
bk_n=Entry(bok_frame,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
bk_n.grid(row=1,column=1,pady=10,padx=10)
bk_au=Entry(bok_frame,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
bk_au.grid(row=2,column=1,pady=10)
bk_publi=Entry(bok_frame,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
bk_publi.grid(row=3,column=1,pady=10)
bk_isbn=Entry(bok_frame,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
bk_isbn.grid(row=4,column=1,pady=10)
#bk_qu=Entry(bok_frame,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
#bk_qu.grid(row=5,column=1,pady=10)
add_bk_bt=Button(bok_frame,text="Add Book",command=add_dt,width=10).place(x=360,y=270)
db = mysql.connector.connect(host="localhost", user="root", password="", database="lms_t")
mycursor = db.cursor()
sql="SELECT * FROM `book_details` ORDER BY `book_details`.`isbn` DESC LIMIT 1"
mycursor.execute(sql)
isp=mycursor.fetchone()
ispu=isp[0]+1
bk_isbn.insert(0,ispu)
bk_isbn.configure(state='disabled')
add_bk_ex=Button(bok_frame,text="Close",command=add_close,width=10).place(x=200,y=270)
ab.mainloop()