from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk
def book_issue():
    rt.destroy()
    import issuebook
def renew_book():
    rt.destroy()
    import rw_rew
def fine():
    rt.destroy()
    import fine
def show_book():
    rt.destroy()
    import Show_Update_add
def exit():
    MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                       icon='warning')
    if MsgBox == 'yes':
        rt.quit()

rt=Tk()
rt.title("HOME PAGE")
rt.geometry("1600x800+0+0")
to_im=ImageTk.PhotoImage(file="top_frame.jpg")
top_frame=Frame(rt,bd=10,relief=GROOVE)
top_frame.place(x=0,y=0,width=1590,height=200)
to_i_l=Label(top_frame,image=to_im)
to_i_l.place(x=0,y=0,relwidth=1,relheight=1)
front_text=Label(top_frame,relief=RAISED,bd=10,text="SMBST Library Management system",font=("Comic Sans MS",30,"bold"),fg="white",bg="black")
front_text.place(x=390,y=60,width=800)
s_frame=Frame(rt,bd=4,relief=RIDGE,bg="light blue")
s_frame.place(x=0,y=200,width=400,height=800)
sf_im=ImageTk.PhotoImage(file="s_pic.jpg")
sf_i_l=Label(s_frame,image=sf_im)
sf_i_l.place(x=0,y=0,relwidth=1,relheight=1)
#s_title=Label(s_frame,text="Actions",font=("Arial Black",20,"bold","underline"),fg="green",bg="light blue")
#s_title.place(x=70,y=20,width=200)
m_frame=Frame(rt,bd=2,relief=GROOVE)
m_frame.place(x=400,y=202,width=1125,height=560)
m_f_im=ImageTk.PhotoImage(file="fr_pic.jpg")
m_f_Im=Label(m_frame,image=m_f_im)
m_f_Im.place(x=0,y=0,relwidth=1,relheight=1)
bki_bt=Button(s_frame,text="Issue Book",relief=GROOVE,font=("Arial Black",13),fg="white",bg="black",command=book_issue,width=18).place(x=120,y=100,width=150)
#bki_bt.pack()
ren_bt=Button(s_frame,text="Renew/Return",relief=GROOVE,font=("Arial Black",13),fg="white",bg="black",command=renew_book,width=18).place(x=120,y=190,width=150)
#Button.pack()
show_bt=Button(s_frame,text="Show",relief=GROOVE,font=("Arial Black",13),fg="white",bg="black",command=show_book,width=18).place(x=120,y=280,width=150)
#Button.pack()
fines_bt=Button(s_frame,text="Fines",relief=GROOVE,font=("Arial Black",13),fg="white",bg="black",command=fine,width=18).place(x=120,y=370,width=150)
#Button.pack()
exit_bt=Button(s_frame,text="Exit",relief=GROOVE,font=("Arial Black",13),fg="white",bg="black",command=exit,width=18).place(x=120,y=450,width=150)
#Button.pack()
rt.mainloop()