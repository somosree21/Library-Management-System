from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk
from datetime import date
def book_issue():
    pass
def fine():
    st.destroy()
    import fine
def renew_book():
    st.destroy()
    import rw_rew
def show_book():
    st.destroy()
    import Show_Update_add
def book_issue_submit():
    if b_id.get() == '' or s_id_e.get() == '':
        messagebox.showerror('Error', 'All fields are required!')
    elif len(b_id.get()) < 4 or len(s_id_e.get()) < 4:
        messagebox.showerror("Error", "Enter Valid Details")
    else:
        bookid = b_id.get()
        studid = s_id_e.get()
        lib_database = mysql.connector.connect(
            host='localhost', user='root', password='', database='lms_t'
        )
        cursor = lib_database.cursor()
        cursor.execute('select stu_id,fine from book_details where isbn= %s', (bookid,))
        row = cursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid book id')
        elif row[0] != 0:
            messagebox.showerror('Error', 'Book already issued. Not available')
        elif row[1] != 0:
            messagebox.showerror('FINE DUE', 'Book cannot be issued. You need to pay the fine first')
        else:
            tod = date.today()
            query = ('UPDATE book_details SET stu_id = %s , issue_dt=%s WHERE isbn=%s')
            val = (studid, tod, bookid)
            cursor.execute(query, val)
            lib_database.commit()
            lib_database.rollback()
            lib_database.close()
            messagebox.showinfo('Success', 'Book issued successfully')

    b_id.delete(0, END)
    s_id_e.delete(0, END)
    b_id.focus_set()

def exit():
    MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                    icon='warning')
    if MsgBox == 'yes':
        st.destroy()
st=Tk()
st.title("Issue Book")
st.geometry("1600x800+0+0")
to_im=ImageTk.PhotoImage(file="top_frame.jpg")
top_frame=Frame(st,bd=10,relief=GROOVE)
top_frame.place(x=0,y=0,width=1590,height=200)
to_i_l=Label(top_frame,image=to_im)
to_i_l.place(x=0,y=0,relwidth=1,relheight=1)
front_text=Label(top_frame,relief=RAISED,bd=10,text="SMBST Library Management system",font=("Comic Sans MS",30,"bold"),fg="white",bg="black")
front_text.place(x=390,y=60,width=800)
s_frame=Frame(st,bd=4,relief=RIDGE)
s_frame.place(x=0,y=200,width=400,height=800)
sf_im=ImageTk.PhotoImage(file="s_pic.jpg")
sf_i_l=Label(s_frame,image=sf_im)
sf_i_l.place(x=0,y=0,relwidth=1,relheight=1)
#s_title=Label(s_frame,text="Actions",font=("Times New Roman",25,"bold"),fg="white",bg="black")
#s_title.place(x=140,y=30,width=110)
bki_bt=Button(s_frame,text="Issue Book",relief=GROOVE,font=("Arial Black",13),fg="black",bg="white",command=book_issue,width=18).place(x=120,y=100,width=150)
ren_bt=Button(s_frame,text="Renew/Return",relief=GROOVE,font=("Arial Black",13),fg="white",bg="black",command=renew_book,width=18).place(x=120,y=190,width=150)
show_bt=Button(s_frame,text="Show",relief=GROOVE,font=("Arial Black",13),fg="white",bg="black",command=show_book,width=18).place(x=120,y=280,width=150)
fines_bt=Button(s_frame,text="Fines",relief=GROOVE,font=("Arial Black",13),fg="white",bg="black",command=fine,width=18).place(x=120,y=370,width=150)
exit_bt=Button(s_frame,text="Exit",relief=GROOVE,font=("Arial Black",13),fg="white",bg="black",command=exit,width=18).place(x=120,y=450,width=150)
m_frame=Frame(st,bd=2,relief=GROOVE)
m_frame.place(x=400,y=202,width=1125,height=560)
bg=ImageTk.PhotoImage(file="issue1.jpg")
bglb=Label(m_frame,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)
b_isbn=Label(m_frame,text="Book ISBN No",font=("Times New Roman",15,"bold"),bg="black",fg="white")
b_isbn.place(x=250,y=150)
b_id=ttk.Entry(m_frame,font=("Times New Roman",15,"bold"))
b_id.place(x=400,y=150,width=250)
s_id=Label(m_frame,text="Student Id",font=("Times New Roman",16,"bold"),bg="black",fg="white")
s_id.place(x=280,y=220)
s_id_e=ttk.Entry(m_frame,font=("Times New Roman",15,"bold"))
s_id_e.place(x=400,y=220,width=250)
isu_bt=Button(m_frame,text="Submit",font=("imes New Roman",13,"bold"),fg="white",bg="black",command=book_issue_submit,width=5).place(x=550,y=290,width=100)


st.mainloop()