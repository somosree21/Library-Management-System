from tkinter import *
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk
from datetime import  date
def book_issue():
    st.destroy()
    import issuebook
def renew_book():
    st.destroy()
    import rw_rew
def show_book():
    st.destroy()
    import Show_Update_add
def fine():
    pass
def exit():
    MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                    icon='warning')
    if MsgBox == 'yes':
        st.destroy()
def payment():
    if student_id.get() == '':
        messagebox.showerror('Error','Please enter valid student ID')
    else:
        #try:
        stud = student_id.get()
        tod = date.today()
        db = mysql.connector.connect(host="localhost", user="root", password="", database="lms_t")
        mycursor = db.cursor()
        sql = "UPDATE `book_details` SET `fine`=%s,`issue_dt`=%s  WHERE stu_id=%s"
        val = (0, tod, stud)
        mycursor.execute(sql, val)
        messagebox.showinfo("Sucess","Payment Done")
        db.commit()
        db.close()

        #except:
         #   messagebox.showerror("Error","No connection")


def fetch():
    if student_id.get() == '':
        messagebox.showerror('Error','Please enter valid student ID')
    else:
        try:
            stud = student_id.get()
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lms_t")
            mycursor = db.cursor()
            mycursor.execute("select isbn,issue_dt from book_details")
            rows = mycursor.fetchall()
            dt = date.today()
            for i in rows:
                fine = 0
                if i[1] == None:
                    fine = 0
                else:
                    fine_date = dt - i[1]
                    if fine_date.days > 30:
                        fine = fine_date.days - 29
                        mycursor = db.cursor()
                        sql = "UPDATE `book_details` SET `fine`=%s  WHERE isbn=%s"
                        val = (fine, i[0])
                        mycursor.execute(sql, val)
            mycursor = db.cursor()
            mycursor.execute('select fine from book_details where stu_id=%s', (stud,))
            rows = mycursor.fetchall()
            fn = 0
            for i in rows:
                fn = fn + i[0]
            if fn==0:
                messagebox.showinfo("Info","No Fines")
            amount.configure(state='normal')
            amount.delete(0, END)
            amount.insert(0, fn)
            amount.configure(state='disable')
        except:
            messagebox.showerror("Error","No Connection")


        #print(type(rows[0][0]))
        #print(date.today())
        #print(type(rows[0][0].day))
        '''x = row[0]
        if row == None:
            messagebox.showerror('Error','Invalid Student ID')
        else:
            amt.set(x)'''





st=Tk()
st.title("Fine Collection")
st.geometry("1600x800+0+0")
to_im=ImageTk.PhotoImage(file="top_frame.jpg")
top_frame=Frame(st,bd=10,relief=GROOVE)
top_frame.place(x=0,y=0,width=1590,height=200)
to_i_l=Label(top_frame,image=to_im)
to_i_l.place(x=0,y=0,relwidth=1,relheight=1)
front_text=Label(top_frame,relief=RAISED,bd=10,text="SMBST library Management Sysytem",font=("Comic Sans MS",30,"bold"),fg="white",bg="black")
front_text.place(x=320,y=60,width=800)
s_frame=Frame(st,bd=4,relief=RIDGE)
s_frame.place(x=0,y=200,width=400,height=800)
sf_im=ImageTk.PhotoImage(file="s_pic.jpg")
sf_i_l=Label(s_frame,image=sf_im)
sf_i_l.place(x=0,y=0,relwidth=1,relheight=1)
#s_title=Label(s_frame,text="Actions",font=("Times New Roman",25,"bold"),fg="white",bg="black")
#s_title.place(x=140,y=30,width=110)
bki_bt=Button(s_frame,text="Issue Book",relief=GROOVE,font=("Arial Black",13),fg="white",bg="black",command=book_issue,width=18).place(x=120,y=100,width=150)
ren_bt=Button(s_frame,text="Renew/Return",relief=GROOVE,font=("Arial Black",13),fg="white",bg="black",command=renew_book,width=18).place(x=120,y=190,width=150)
show_bt=Button(s_frame,text="Show",relief=GROOVE,font=("Arial Black",13),fg="white",bg="black",command=show_book,width=18).place(x=120,y=280,width=150)
fines_bt=Button(s_frame,text="Fines",relief=GROOVE,font=("Arial Black",13),fg="black",bg="white",command=fine,width=18).place(x=120,y=370,width=150)
exit_bt=Button(s_frame,text="Exit",relief=GROOVE,font=("Arial Black",13),fg="white",bg="black",command=exit,width=18).place(x=120,y=450,width=150)
m_frame=Frame(st,bd=2,relief=GROOVE)
m_frame.place(x=400,y=202,width=1125,height=560)
b = Image.open('fine.jpg')
bm = b.resize((1125,560), Image.ANTIALIAS)
bg=ImageTk.PhotoImage(bm)
bglb=Label(m_frame,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)
stid=Label(m_frame,text="Student ID:",font=("Times New Roman",15,"bold"),bg="black",fg="white")
stid.place(x=250,y=50)
student_id=ttk.Entry(m_frame,font=("Times New Roman",15,"bold"))
student_id.place(x=400,y=50,width=250)
fine=Button(m_frame,text="FETCH FINE",font=("Times New Roman",13,"bold"),fg="white",bg="black",width=5, command= fetch).place(x=450,y=100,width=120)
Label(m_frame,text="Amount due:",font=("Times New Roman",15,"bold"),fg="white",bg="black").place(x=250,y=200)
amt= IntVar()
amount=ttk.Entry(m_frame,font=("Times New Roman",15,"bold"), textvariable=amt)
amount.place(x=400,y=200,width=250)
pay=Button(m_frame,text="PAY",font=("Times New Roman",13,"bold"),fg="white",bg="black",width=5,command=payment).place(x=450,y=330,width=120)


st.mainloop()