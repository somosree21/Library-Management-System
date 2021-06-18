from tkinter import *
import mysql.connector
from tkinter import ttk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from datetime import  date


def book_issue():
    qt.destroy()
    import issuebook
def fine():
    qt.destroy()
    import fine

def fetch_fine():
    try:
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
                    mycursor.execute("select * from book_details")
                    rows = mycursor.fetchall()
                    if len(rows) != 0:
                        medtab.delete(*medtab.get_children())
                    for row in rows:
                        y = list(row)
                        if y[1] == 0:
                            y[6] = "Available"
                        elif y[1] != 0:
                            y[6] = "Not Available"
                        row = tuple(y)
                        medtab.insert('', END, values=row)

        db.commit()
        db.close()
    except:
        messagebox.showerror("Error","No connection to Server")


def renew_book():
    qt.destroy()
    import rw_rew


def show_book():
    pass


def exit():
    MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                    icon='warning')
    if MsgBox == 'yes':
        qt.destroy()


def fetch():
    ser = combo_ser.get()
    ser_name = search_l.get()
    if ser == "ISBN No":
        if len(ser_name) < 4:
            messagebox.showerror("Error", "Isbn Number must br 4 digit")
            return
        ser = "isbn"
    elif ser == "Book Name":
        ser = "b_name"
    elif ser == "Author":
        ser = "auth"
    elif ser == "Student Id":
        if len(ser_name) < 4:
            messagebox.showerror("Error", "Student Id must br 4 digit")
            return
        ser = "stu_id"
    if ser_name == None:
        messagebox.showerror("Error", "Enter value in searchbox")
    else:
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="lms_t")
            mycursor = db.cursor()
            mycursor.execute("select * from book_details where " + str(ser) + " LIKE '%" + str(ser_name) + "%'")
            rows = mycursor.fetchall()
            if len(rows) == 0:
                messagebox.showerror("Not found", "No matching database found")
            if len(rows) != 0:
                medtab.delete(*medtab.get_children())
            for row in rows:
                y = list(row)
                if y[1] == 0:
                    y[6] = "Available"
                elif y[1] != 0:
                    y[6] = "Not Available"
                row = tuple(y)
                medtab.insert('', END, values=row)
            db.commit()
            db.close()


        except:
            messagebox.showerror("Error", "No Connection to Server")


def fetchall():
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", database="lms_t")
        mycursor = db.cursor()
        mycursor.execute("select * from book_details")
        rows = mycursor.fetchall()
        if len(rows) != 0:
            medtab.delete(*medtab.get_children())
        for row in rows:
            y = list(row)
            if y[1] == 0:
                y[6] = "Available"
            elif y[1] != 0:
                y[6] = "Not Available"
            row = tuple(y)
            medtab.insert('', END, values=row)
        db.commit()
        db.close()
    except:
        messagebox.showerror("Error", "No Connection to Server")


def add_book():
    import add_book


def update_book():
    def update_dt():
        bkn = bk_n.get()
        bka = bk_au.get()
        bkisb = bk_isbn.get()
        bkdt = cal.get()
        stud = bk_qu.get()
        print(type(bka))
        if stud != 0:
            st = 1
        elif stud == 0:
            st = 0
        # print(stud,bkdt)
        if (stud == "" and bkdt != ""):
            messagebox.showerror("Error", "Fill both student id and Issue")
            ab.destroy()
            return
        if (stud != "" and bkdt == ""):
            messagebox.showerror("Error", "Fill both student id and Issue")
            ab.destroy()
            return
        try:
            if (type(int(bka))==int):
                messagebox.showerror("Error", "Please enter valid author name")
                ab.destroy()
                return
        except:
            try:
                db = mysql.connector.connect(host="localhost", user="root", password="", database="lms_t")
                mycursor = db.cursor()
                sql = "UPDATE `book_details` SET `stu_id`=%s,`b_name`=%s,`auth`=%s,`issue_dt`=%s WHERE isbn=%s"
                val = (stud, bkn, bka, bkdt, bkisb)
                mycursor.execute(sql, val)
                db.commit()
                db.close()
                messagebox.showinfo("Success", "Updated Success fully")
                ab.destroy()

            except:
                messagebox.showerror("Error", "No Connection")
                ab.destroy()

    ab = Tk()
    ab.title("Update Book Details")
    ab.geometry("600x400+600+200")
    bok_frame = Frame(ab, bg="light blue")
    bok_frame.place(x=5, y=5, width=600, height=400)
    bok_title = Label(bok_frame, text="Update Book Details", font=("Comic Sans MS", 20, "bold", "underline"),
                      fg="black",
                      bg="light blue")
    bok_title.grid(row=0, columnspan=4, padx=200)
    bk_n = Label(bok_frame, text="Book Name", font=("Times New Roman", 15, "bold"), bg="light blue")
    bk_n.grid(row=1, column=0, pady=10)
    bk_au = Label(bok_frame, text="Author Name", font=("Times New Roman", 15, "bold"), bg="light blue")
    bk_au.grid(row=2, column=0, pady=10)
    # bk_publi = Label(bok_frame, text="Publisher", font=("Times New Roman", 15, "bold"), bg="light blue")
    # bk_publi.grid(row=3, column=0, pady=10)
    bk_isbn = Label(bok_frame, text="ISBN Number", font=("Times New Roman", 15, "bold"), bg="light blue")
    bk_isbn.grid(row=3, column=0, pady=10)
    bk_qu = Label(bok_frame, text="Student Id", font=("Times New Roman", 15, "bold"), bg="light blue")
    bk_qu.grid(row=4, column=0, pady=10)
    bk_isu = Label(bok_frame, text="Issue Date", font=("Times New Roman", 15, "bold"), bg="light blue")
    bk_isu.grid(row=5, column=0, pady=10)
    cal = DateEntry(bok_frame, date_pattern='yyyy/mm/dd', font=("Times New Roman", 15, "bold"), background='gray',
                    foreground='white', borderwidth=1)
    cal.grid(row=5, column=1, pady=10, padx=10)
    cal.delete(0, END)
    bk_n = Entry(bok_frame, font=("Times New Roman", 15, "bold"), bd=5, relief=GROOVE)
    bk_n.grid(row=1, column=1, pady=10, padx=10)
    bk_au = Entry(bok_frame, font=("Times New Roman", 15, "bold"), bd=5, relief=GROOVE)
    bk_au.grid(row=2, column=1, pady=10)
    # bk_publi = Entry(bok_frame, font=("Times New Roman", 15, "bold"), bd=5, relief=GROOVE)
    # bk_publi.grid(row=3, column=1, pady=10)
    bk_isbn = Entry(bok_frame, font=("Times New Roman", 15, "bold"), bd=5, relief=GROOVE)
    bk_isbn.grid(row=3, column=1, pady=10)
    bk_qu = Entry(bok_frame, font=("Times New Roman", 15, "bold"), bd=5, relief=GROOVE)
    bk_qu.grid(row=4, column=1, pady=10)
    try:
        currow = medtab.focus()
        contents = medtab.item(currow)
        row = contents['values']
        if row == None:
            messagebox.showerror("Error", "please select a row to update")
        else:
            bk_n.insert(0, row[2])
            bk_au.insert(0, row[3])
            bk_isbn.insert(0, row[0])
            bk_isbn.configure(state='disabled')
            if row[1]!=str(0):
                bk_qu.insert(0, row[1])
                cal.insert(0, row[5])
            else:
                bk_qu.delete(0,END)
                cal.delete(0,END)
            add_bk_bt = Button(bok_frame, text="Update Detail", command=update_dt, width=10).place(x=380, y=330)
            ab.mainloop()
    except:
        messagebox.showerror("Error","Select a row to update")
        ab.destroy()


def delete_book():
    try:
        currow = medtab.focus()
        contents = medtab.item(currow)
        row = contents['values']
        db = mysql.connector.connect(host="localhost", user="root", password="", database="lms_t")
        mycursor = db.cursor()
        try:
            sql = "delete from book_details where isbn=%s"
            val = (row[0],)
            mycursor.execute(sql, val)
            db.commit()
            x = medtab.selection()[0]
            medtab.delete(x)
            messagebox.showinfo("information", "Record Deleted successfully")
        except EXCEPTION as e:
            print(e)
            db.rollback()
            db.close()
            messagebox.showerror("Error", "Connection Lost")
    except:
        messagebox.showerror("Error", "Please select a row to delete")


def getdata():
    pass


qt = Tk()
qt.title("HOME PAGE")
qt.geometry("1600x800+0+0")
to_im = ImageTk.PhotoImage(file="top_frame.jpg")
top_frame = Frame(qt, bd=10, relief=GROOVE)
top_frame.place(x=0, y=0, width=1590, height=200)
to_i_l = Label(top_frame, image=to_im)
to_i_l.place(x=0, y=0, relwidth=1, relheight=1)
front_text = Label(top_frame, relief=RAISED, bd=10, text="Library Management system",
                   font=("Comic Sans MS", 30, "bold"), fg="white", bg="black")
front_text.place(x=390, y=60, width=800)
s_frame = Frame(qt, bd=4, relief=RIDGE, bg="light blue")
s_frame.place(x=0, y=200, width=400, height=800)
sf_im = ImageTk.PhotoImage(file="s_pic.jpg")
sf_i_l = Label(s_frame, image=sf_im)
sf_i_l.place(x=0, y=0, relwidth=1, relheight=1)
# s_title=Label(s_frame,text="Actions",font=("Arial Black",20,"bold","underline"),fg="green",bg="light blue")
# s_title.place(x=70,y=20,width=200)
bki_bt = Button(s_frame, text="Issue Book", relief=GROOVE, font=("Arial Black", 13), fg="white", bg="black",
                command=book_issue, width=18).place(x=120, y=100, width=150)
ren_bt = Button(s_frame, text="Renew/Return", relief=GROOVE, font=("Arial Black", 13), fg="white", bg="black",
                command=renew_book, width=18).place(x=120, y=190, width=150)
show_bt = Button(s_frame, text="Show", relief=GROOVE, font=("Arial Black", 13), fg="black", bg="white",
                 command=show_book, width=18).place(x=120, y=280, width=150)
fines_bt = Button(s_frame, text="Fines", relief=GROOVE, font=("Arial Black", 13), fg="white", bg="black",
                  command=fine, width=18).place(x=120, y=370, width=150)
exit_bt = Button(s_frame, text="Exit", relief=GROOVE, font=("Arial Black", 13), fg="white", bg="black", command=exit,
                 width=18).place(x=120, y=450, width=150)
m_frame = Frame(qt, bd=2, relief=GROOVE, bg="light green")
m_frame.place(x=400, y=202, width=1125, height=560)
search_l = Label(m_frame, text="Search By", font=("Britannic Bold", 17), fg="black", bg="light green")
# search_l.place(x=50,y=15,width=110)
search_l.grid(row=0, column=0, padx=10, pady=10, sticky="w")
combo_ser = ttk.Combobox(m_frame, font=("Britannic Bold", 14), width=10, state='readonly')
combo_ser['values'] = ("ISBN No", "Student Id", "Book Name", "Author")
combo_ser.grid(row=0, column=1, padx=20, pady=10, sticky="w")
search_l = Entry(m_frame, font=("Times New Roman", 15, "bold"), bd=4, relief=GROOVE)
search_l.grid(row=0, column=2, padx=20, pady=10, sticky="w")
s_bt = Button(m_frame, text="Search", command=fetch, font=("Arial Black", 12), bg="black", fg="white").grid(row=0,
                                                                                                            column=3)
showall_bt = Button(m_frame, text="Show All", command=fetchall, font=("Arial Black", 12), fg="White", bg="black").place(
    x=750, y=6)
# add_bt=Button(m_frame,text="Search",command=fetch,font=("Arial Black",12),bg="black",fg="white").grid(row=0,column=3)
ta_frm = Frame(m_frame, bd=4, relief=RIDGE, bg="white")
ta_frm.place(x=60, y=60, width=1000, height=420)
scrollx = Scrollbar(ta_frm, orient=HORIZONTAL)
scrolly = Scrollbar(ta_frm, orient=VERTICAL)
medtab = ttk.Treeview(ta_frm, columns=("bid", "sId", "bname", "status", "iss_d", "fine", "author"),
                      xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
scrollx.pack(side=BOTTOM, fill=X)
scrolly.pack(side=RIGHT, fill=Y)
scrollx.config(command=medtab.xview)
scrolly.config(command=medtab.yview)
medtab.heading("bid", text="ISBN NO")
medtab.heading("sId", text="Student Id")
medtab.heading("bname", text="Book Name")
medtab.heading("status", text="Author")
medtab.heading("iss_d", text="Fine")
medtab.heading("fine", text="Issue Date")
medtab.heading("author", text="Status")
medtab['show'] = "headings"
medtab.column("bid", width=100)
medtab.column("sId", width=100)
medtab.column("bname", width=100)
medtab.column("status", width=100)
medtab.column("iss_d", width=100)
medtab.column("fine", width=100)
medtab.column("author", width=100)
medtab.pack(fill=BOTH, expand=1)
# medtab.bind("<ButtonRelease-1>",store)
# medtab.bind("<Double-1>",getdata)
add_btn = Button(m_frame, text="Add Book", command=add_book, font=("Arial Black", 12), fg="White", bg="black").place(
    x=450, y=500)
updt_btn = Button(m_frame, text="Update Book", command=update_book, font=("Arial Black", 12), fg="White",
                  bg="black").place(x=600, y=500)
del_bt = Button(m_frame, text="Delete Book", command=delete_book, font=("Arial Black", 12), fg="White",
                bg="black").place(x=770, y=500)
fine_ft = Button(m_frame, text="Update Fine", command=fetch_fine, font=("Arial Black", 12), fg="White",
                 bg="black").place(x=280, y=500)
qt.mainloop()
