from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk
def update_dt():
    pass
ab=Tk()
ab.title("Update Book")
ab.geometry("600x400+600+300")
bok_frame=Frame(ab,bg="light blue")
bok_frame.place(x=5,y=5,width=600,height=400)
bok_title=Label(bok_frame,text="Update Book Details",font=("Comic Sans MS",20,"bold","underline"),fg="black",bg="light blue")
bok_title.grid(row=0,columnspan=4,padx=200)
bk_n=Label(bok_frame,text="Book Name",font=("Times New Roman",15,"bold"),bg="light blue")
bk_n.grid(row=1,column=0,pady=10)
bk_au=Label(bok_frame,text="Author Name",font=("Times New Roman",15,"bold"),bg="light blue")
bk_au.grid(row=2,column=0,pady=10)
bk_publi=Label(bok_frame,text="Publisher",font=("Times New Roman",15,"bold"),bg="light blue")
bk_publi.grid(row=3,column=0,pady=10)
bk_isbn=Label(bok_frame,text="ISBN Number",font=("Times New Roman",15,"bold"),bg="light blue")
bk_isbn.grid(row=4,column=0,pady=10)
bk_qu=Label(bok_frame,text="Quantity",font=("Times New Roman",15,"bold"),bg="light blue")
bk_qu.grid(row=5,column=0,pady=10)
bk_n=Entry(bok_frame,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
bk_n.grid(row=1,column=1,pady=10,padx=10)
bk_au=Entry(bok_frame,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
bk_au.grid(row=2,column=1,pady=10)
bk_publi=Entry(bok_frame,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
bk_publi.grid(row=3,column=1,pady=10)
bk_isbn=Entry(bok_frame,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
bk_isbn.grid(row=4,column=1,pady=10)
bk_qu=Entry(bok_frame,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
bk_qu.grid(row=5,column=1,pady=10)
add_bk_bt=Button(bok_frame,text="Update Detail",command=update_dt,width=10).place(x=360,y=330)
ab.mainloop()