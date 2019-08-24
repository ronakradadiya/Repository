from tkinter import *
from tkinter import messagebox
import sqlite3
import os

db_filename = 'Employee.db'
db_exists = not os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

if (db_exists):
    cursor.execute("create table Employee(Emp_pid int primary key, Emp_username varchar(50), Emp_name varchar(50), Emp_gender varchar(20), Emp_dept varchar(20), Emp_email varchar(50), cgpi int, placement varchar(20), company varchar(20), currentstatus varchar(20), salary int)")
    cursor.execute("insert into Employee values(113,'Rajverma','Raj', 'Male', 'IT', 'rajverma@gmail.com', 9, 'Yes', 'TATA', 'HR', 10000)")
    print('table created')
    cursor.execute("delete from Employee where Emp_pid=''")
    
cursor.execute('select * from Employee')
conn.commit()
data=cursor.fetchall()
print(data)


list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
list8=[]
list9=[]
list10=[]
list11=[]

for row in data:
    list1.append(row[0])
    list2.append(row[1])
    list3.append(row[2])
    list4.append(row[3])
    list5.append(row[4])
    list6.append(row[5])
    list7.append(row[6])
    list8.append(row[7])
    list9.append(row[8])
    list10.append(row[9])
    list11.append(row[10])
    

class Login_window:
    
    def log_window1(self):
        
        try:
            self.master2.destroy()
            
        except:
            pass
            
        self.master = Tk()
        self.master.title("Employee details")
        self.master.configure(background='#1A2B41')
        
        self.login_frame = Frame(self.master, height=1000, width=1000, bg='#2F4158')
        self.login_frame.pack_propagate(0)
        self.login_frame.pack(expand=1)
    

        self.im = PhotoImage(file = 'logoo.png')
        self.im = self.im.subsample(5,5)
        self.label_img = Label(self.login_frame , image = self.im)
        self.label_img.grid(row=0, columnspan=2, pady=10)


        self.var = IntVar()
        self.admin = Radiobutton(self.login_frame, text='Admin', variable=self.var, value=1, bg='#2F4158', padx=40, pady=20, fg='white')
        self.student = Radiobutton(self.login_frame, text='Student', variable=self.var, value=2, bg='#2F4158', padx=40, pady=20, fg='white')
        self.admin.grid(row=1)
        self.student.grid(row=1, column=1)
        
        

        self.label1 = Label(self.login_frame, text='Name', bg='#2F4158', fg='white')
        self.label1.grid(row=2, column=0, pady=20)
        self.label2= Label(self.login_frame, text='Password', bg='#2F4158', fg='white')
        self.label2.grid(row=4, column=0, pady=20)

        self.entry1= Entry(self.login_frame, bd=3, justify=LEFT, width=30)
        self.entry2= Entry(self.login_frame, bd=3, show='*', justify=LEFT, width=30)
        self.entry1.grid(row=3, column=0, pady=10, columnspan=2)
        self.entry2.grid(row=5, column=0, pady=10, columnspan=2)
    
        
        self.button1= Button(self.login_frame, text='Login', bg='#39DAF7', fg='black', command=self.new_window, width=5)
        self.button1.grid(row=6, pady=20, columnspan=2)
        
        self.button2 = Button(self.login_frame, text='Forgot Password', bg='#39DAF7', fg='black', command = self.forgot_password)
        self.button2.grid(row=7, columnspan=2 , pady=20 )
        
        self.master.mainloop()
        
        
    
    def new_window(self):
        
        if self.var.get() == 2:
            i=0
            flag=0
            flag1=0
            length = len(list2)
            print(length)
            userid = str(self.entry1.get())
            password = str(self.entry2.get())
            print('userid is',userid)
            print('password is', password)
        
            while i<length:
            
                flag=0
                userid1=str(list3[i])
                password1=str(list1[i])
                username = str(list2[i])
                gender = str(list4[i])
                dept = str(list5[i])
                email = str(list6[i])
                cgpi = str(list7[i])
                placement = str(list8[i])
                company = str(list9[i])
                crs = str(list10[i])
                salary = str(list11[i])
                print("userid1:",userid,"password1:",password)
                print("list id:",userid1,"list password:",password1)
            
                if self.var.get() == 2:    
                
                    if userid == userid1:
                        flag = flag+1
                        flag1 = flag1 +1

                    if password == password1:
                        flag = flag+1
                        flag1 = flag1+1
            
            
        
                    if flag==2:
                
                        print('Done')
                        messagebox.showinfo("Thank you", "You are logged in\nClick on the button below to view your details")
                        top = Toplevel()
                        top.title("Welcome")
                        self.emp_topframe = Frame(top, height=200, width=1600, bg='black')
                        self.emp_topframe.pack_propagate(0)
                        self.emp_topframe.pack( anchor='n')
                        self.emp_frame = Frame(top, height=600, width=600, bg='light blue')
                        self.emp_frame2 = Frame(top, height=600, width=600, bg='white')
                        self.emp_image = PhotoImage(file = 'student.png')
                        self.emp_image = self.emp_image.subsample(2,2)
                        self.labemp_image = Label(self.emp_topframe , image = self.emp_image)
                        self.labemp_image.pack(side=LEFT)
                        self.emplabel_1 = Label(self.emp_topframe, text='Student Details', bg='black', fg='white', font=('Verdana',25,'bold'))
                        self.emplabel_1.pack(expand=1, pady=50)
                        self.l1=Label(self.emp_frame, text='Your PID is: '+password1,font=('Verdana',15,'bold'),fg='black', bg='light blue')
                        self.l2=Label(self.emp_frame, text='Your Username is: '+username,font=('Verdana',15,'bold'),fg='black', bg='light blue')
                        self.l3=Label(self.emp_frame, text='Your Name is: '+userid1,font=('Verdana',15,'bold'),fg='black', bg='light blue')
                        self.l4=Label(self.emp_frame, text='Your Gender is: '+gender,font=('Verdana',15,'bold'),fg='black', bg='light blue')
                        self.l5=Label(self.emp_frame, text='Your Department is: '+dept,font=('Verdana',15,'bold'),fg='black', bg='light blue')
                        self.l6=Label(self.emp_frame, text='Your Email: '+email,font=('Verdana',15,'bold'),fg='black', bg='light blue')
                        self.l7=Label(self.emp_frame2, text='Your Average CGPI: '+cgpi,font=('Verdana',15,'bold'),fg='black', bg='white')
                        self.l8=Label(self.emp_frame2, text='Placement: '+placement,font=('Verdana',15,'bold'),fg='black', bg='white')
                        self.l9=Label(self.emp_frame2, text='Your Company is: '+company,font=('Verdana',15,'bold'),fg='black', bg='white')
                        self.l10=Label(self.emp_frame2, text='Your Current status is: '+crs,font=('Verdana',15,'bold'),fg='black', bg='white')
                        self.l11=Label(self.emp_frame2, text='Your Salary is: '+salary,font=('Verdana',15,'bold'),fg='black', bg='white')
                        
                        
                        self.l1.grid(row=0, pady=20, sticky=W)
                        self.l2.grid(row=1, pady=20, sticky=W)
                        self.l3.grid(row=2, pady=20, sticky=W)
                        self.l4.grid(row=3, pady=20, sticky=W)
                        self.l5.grid(row=4, pady=20, sticky=W)
                        self.l6.grid(row=5, pady=20, sticky=W)
                        self.l7.grid(row=6, pady=20, sticky=W)
                        self.l8.grid(row=7, pady=20, sticky=W)
                        self.l9.grid(row=8, pady=20, sticky=W)
                        self.l10.grid(row=9, pady=20, sticky=W)
                        self.l11.grid(row=10, pady=20, sticky=W)
                        self.emp_frame.place(x=55, y=250)
                        self.emp_frame2.place(x=950, y=250)
                        top.mainloop()
                        break
                
            
                i+=1
        
        
                
            if (flag==0 or flag1 == 1) and (self.entry1.get() != '' or self.entry2.get() != ''):
                messagebox.showinfo("Sorry","Please enter correct details")
        
            if ((self.entry1.get() == '') and (self.entry2.get() == '')):
                messagebox.showinfo("Hey", "Please fill in the username and password")
                
                
        else:
                c.admin_window()
                #print('done')
        
    def forgot_password(self):
        
        self.master.destroy()
        
        self.master6 = Tk()
        self.master6.title("Forgot Password")
        self.master6.configure(background='#1A2B41')
        
        self.password_frame = Frame(self.master6, height=1000, width=1000, bg='#2F4158')
        self.password_frame.pack_propagate(0)
        self.password_frame.pack(expand=1)
        
        self.password_label = Label(self.password_frame, text='Enter your Email', bg='#2F4158', fg='white')
        self.password_label.grid(row=1, pady=20)
        self.password_label= Label(self.password_frame, text='Enter your username', bg='#2F4158', fg='white')
        self.password_label.grid(row=3, pady=20)
        
        self.password_entry1= Entry(self.password_frame, bd=3, justify=LEFT)
        self.password_entry2= Entry(self.password_frame, bd=3, justify=LEFT)
        self.password_entry1.grid(row=2, pady=15, padx=30)
        self.password_entry2.grid(row=4, pady=15, padx=30)
        
        self.password_button1= Button(self.password_frame, text='Set Password', bg='#39DAF7', fg='black', command=self.password_window)
        self.password_button1.grid(row=5, padx=30, pady=15)
        
        self.master6.mainloop()
        
            
    
    def password_window(self):
        
        
        
        gmail_1 = str(self.password_entry1.get()) 
        username_1 = str(self.password_entry2.get())
        
        
        flag = 0
        length = len(list2)
        i=0
        
        while i<length:
            
            gm = str(list6[i])
            ud = str(list2[i])
            
            if gmail_1 == gm:
                flag+=1
                
            if username_1 == ud:
                flag+=1
                
            if flag==2:
                
                try:
                    self.password_frame.forget()
                    messagebox.showinfo('Hey', 'Your details are successfully matched')
                    
                except:
                    pass
                
                self.password_frame1 = Frame(self.master6, height=1000, width=1000, bg='#2F4158')
                self.password_frame1.pack_propagate(0)
                self.password_frame1.pack(expand=1)
                
                self.password_label1 = Label(self.password_frame1, text='Enter new password', bg='#2F4158', fg='white')
                self.password_label1.grid(row=1, pady=20)
        
        
                self.password_entry3= Entry(self.password_frame1, bd=3, justify=LEFT, show="*")
                self.password_entry3.grid(row=2, pady=15, padx=30)
                
                
                self.password_button1= Button(self.password_frame1, text='Submit', bg='#39DAF7', fg='black', command = self.set_password)
                self.password_button1.grid(row=3, padx=30, pady=15)
                
                break
            
            i+=1
                
        
    def set_password(self):
        
        
        cursor.execute("update Employee set Emp_pid = ? where Emp_email=? and Emp_username=?", (self.password_entry3.get(), self.password_entry1.get(), self.password_entry2.get()))
        conn.commit()
        
        messagebox.showinfo('Hey', 'You have successfully changed your password')
        self.master6.destroy()
        
        
        cursor.execute('select * from Employee')
        data2 = cursor.fetchall()
        print(data2)
        
            

    def admin_window(self):
        
        if self.var.get() == 1:
            print(self.var.get())
            
            if self.entry1.get() == 'Ronak' and self.entry2.get() == '1234':
                
                print('done')
                messagebox.showinfo('Hey Admin', 'You are logged in')
                self.top = Toplevel()
                self.top.title("Welcome Admin")
                self.c = Canvas(self.top, bg='white')
                self.c.pack(fill=BOTH, expand=YES)
                
                self.i = PhotoImage(file='bg1.png')
                self.c.create_image( 750, 300, image = self.i, anchor=CENTER)
                
                self.admin_frame = Frame(self.c)
                self.admin_frame.place(relx= 0.5, rely=0.5, anchor="c")
                self.lab1 = Label(self.admin_frame, image = self.i, padx=20, pady=20)
                self.lab1.pack(fill=BOTH, expand=YES)
                self.admin_frame.pack_propagate(0)
                self.admin_frame.pack(expand=1)
                
                self.emp_pid = Label(self.admin_frame, text='PID', bg='#011017', fg='white', font=('Verdana',15,'bold'))
                self.emp_pid.grid(row=0, column=0, pady=20, padx=20, sticky=W)
                self.emp_name = Label(self.admin_frame, text='Name', bg='#011017', fg='white', font=('Verdana',15,'bold'))
                self.emp_name.grid(row=2, column=0, pady=20, padx=20, sticky=W)
                self.emp_username = Label(self.admin_frame, text='Username', bg='#011017', fg='white', font=('Verdana',15,'bold'))
                self.emp_username.grid(row=1, column=0, pady=20, padx=20, sticky=W)
                self.emp_gender = Label(self.admin_frame, text='Gender', bg='#011017', fg='white', font=('Verdana',15,'bold'))
                self.emp_gender.grid(row=3, column=0, pady=20, padx=20, sticky=W)
                self.emp_dept = Label(self.admin_frame, text='Department', bg='#011017', fg='white', font=('Verdana',15,'bold'))
                self.emp_dept.grid(row=4, column=0, pady=20, padx=20, sticky=W)
                self.emp_email = Label(self.admin_frame, text='Email ', bg='#011017', fg='white', font=('Verdana',15,'bold'))
                self.emp_email.grid(row=5, column=0, pady=20, padx=20, sticky=W)

                self.emp_pid1= Entry(self.admin_frame, bd=3)
                self.emp_pid1.grid(row=0, column=1, pady=20, padx=40)
                
                self.emp_username1= Entry(self.admin_frame, bd=3)
                self.emp_username1.grid(row=1, column=1, pady=20, padx=40)
                
                self.emp_name1= Entry(self.admin_frame, bd=3)
                self.emp_name1.grid(row=2, column=1, pady=10, padx=40)
                
                self.emp_gender1= Entry(self.admin_frame, bd=3)
                self.emp_gender1.grid(row=3, column=1, pady=10, padx=40)
                
                self.emp_dept1= Entry(self.admin_frame, bd=3)
                self.emp_dept1.grid(row=4, column=1, pady=10, padx=40)
                
                self.emp_email1 = Entry(self.admin_frame, bd=3)
                self.emp_email1.grid(row=5, column=1, pady=10, padx=40)

                
                self.ctr=0
                
                self.addmore_details = Button(self.c, text='For more details', bg='light blue', font=('Verdana',12,'bold'), command = self.details_addmore)
                self.addmore_details.place(x=680, y=650)
                 
                self.top.mainloop()
                
                
            elif ((self.entry1.get() == '') and (self.entry2.get() == '')):
                messagebox.showinfo("Hey Admin", "Please fill in the username and password") 
                
            elif ((self.entry1.get() == 'Ronak' and self.entry2.get() == '')):
                messagebox.showinfo('Hey Admin', 'Please enter password')
                
            elif ((self.entry1.get() == '' and self.entry2.get() == '1234')):  
                messagebox.showerror('Hey Admin', 'Please enter username')
                
            else:
                messagebox.showinfo('Hey Admin', 'Please enter correct details')
    
    def details_addmore(self):
        
        self.ctr+=1
        
        
        if self.ctr == 1:
            
            
            self.admin_frame.forget()
            self.addmore_details.destroy()
            
            self.admin_frame1 = Frame(self.c)
            self.admin_frame1.place(relx= 0.5, rely=0.5, anchor="c")
            self.lab11 = Label(self.admin_frame1, image = self.i, padx=20, pady=20)
            self.lab11.pack(fill=BOTH, expand=YES)
            self.admin_frame1.pack_propagate(0)
            self.admin_frame1.pack(expand=1)

            self.emp_cgpi = Label(self.admin_frame1, text='Average CGPI', bg='#011017', fg='white', font=('Verdana',15,'bold'))
            self.emp_cgpi.grid(row=1, column=0, pady=20, padx=20, sticky=W)
            self.emp_placement = Label(self.admin_frame1, text='Placement', bg='#011017', fg='white', font=('Verdana',15,'bold'))
            self.emp_placement.grid(row=2, column=0, pady=20, padx=20, sticky=W)
            self.emp_company = Label(self.admin_frame1, text='Company', bg='#011017', fg='white', font=('Verdana',15,'bold'))
            self.emp_company.grid(row=3, column=0, pady=20, padx=20, sticky=W)
            self.emp_cr = Label(self.admin_frame1, text='Current Status', bg='#011017', fg='white', font=('Verdana',15,'bold'))
            self.emp_cr.grid(row=4, column=0, pady=20, padx=20, sticky=W)
            self.emp_salary = Label(self.admin_frame1, text='Salary ', bg='#011017', fg='white', font=('Verdana',15,'bold'))
            self.emp_salary.grid(row=5, column=0, pady=20, padx=20, sticky=W)

            self.emp_cgpi1= Entry(self.admin_frame1, bd=3)
            self.emp_cgpi1.grid(row=1, column=1, pady=20, padx=40)
             
            self.emp_placement1= Entry(self.admin_frame1, bd=3)
            self.emp_placement1.grid(row=2, column=1, pady=10, padx=40)
            
            self.emp_company1= Entry(self.admin_frame1, bd=3)
            self.emp_company1.grid(row=3, column=1, pady=10, padx=40)
            
            self.emp_cr1= Entry(self.admin_frame1, bd=3)
            self.emp_cr1.grid(row=4, column=1, pady=10, padx=40)
            
            self.emp_salary1 = Entry(self.admin_frame1, bd=3)
            self.emp_salary1.grid(row=5, column=1, pady=10, padx=40)

            self.add_details1 = Button(self.admin_frame1, text='Add', bg='light blue', font=('Verdana',12,'bold'), command = self.details_add)
            self.add_details1.grid(columnspan=2, pady=20)
                
            self.top.mainloop()
      
    
                
    def details_add(self):
        
        
        if self.emp_pid1.get() == '' or self.emp_username1.get() == '' or self.emp_name1.get() == '' or self.emp_gender1.get() == '' or self.emp_dept1.get() == ''  or self.emp_email1.get() == '' or self.emp_cgpi1.get() == '' or self.emp_placement1.get() == '' or self.emp_company1.get()=='' or self.emp_cr1.get()=='' or self.emp_salary1.get()=='':
            
            messagebox.showinfo('Hey', 'Please fill in the details')
        
        else:
            
            listdb = [(self.emp_pid1.get(), self.emp_username1.get(), self.emp_name1.get(), self.emp_gender1.get(), self.emp_dept1.get(), self.emp_email1.get(), self.emp_cgpi1.get(), self.emp_placement1.get(), self.emp_company1.get(), self.emp_cr1.get(), self.emp_salary1.get())]
        
            for element in listdb:
                cursor.execute("insert into Employee values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", element)
                print('done')
                conn.commit()
                messagebox.showinfo('Admin', 'You have successfully details')
                self.master.destroy()
                cursor.execute('select * from Employee')
                data2 = cursor.fetchall()
                print(data2)
            
        
    def log_window(self):
        
        self.master2 = Tk()
        self.master2.title('Welcome to Alumni')


        self.frame_log = Frame(self.master2, height=200, width=1600, bg='black')
        self.frame_log.pack_propagate(0)
        self.frame_log.pack(expand=1, side=TOP, anchor='n')

        self.image_1 = PhotoImage(file = 'student1.png')
        self.image_1 = self.image_1.subsample(2,2)
        self.label_image1 = Label(self.frame_log , image = self.image_1)
        self.label_image1.pack(side=LEFT)

        self.label_1 = Label(self.frame_log, text='Repository and Search Engine for Alumni', bg='black', fg='white', font=('Verdana',25,'bold'))
        self.label_1.pack(expand=1, pady=50)


        self.label_2 = Button(self.frame_log, text='Home', bg='black', fg='white', font=('Verdana',15,'bold'))
        self.label_2.pack(side=LEFT, padx=50)


        self.button_3 = Button(self.frame_log, text='Login', bg='black', fg='white', font=('Verdana',15,'bold'), command = self.log_window1)
        self.button_3.pack(side=LEFT, padx=50)

        self.label_4 = Button(self.frame_log, text='About Us', bg='black', fg='white', font=('Verdana',15,'bold'), command = self.about_window)
        self.label_4.pack(side=LEFT, padx=50)

        self.label_5 = Button(self.frame_log, text='Help', bg='black', fg='white', font=('Verdana',15,'bold'), command=self.help_window)
        self.label_5.pack(side=LEFT, padx=50)

        self.frame1_log = Frame(self.master2, height=510, width=600, bg='light blue')
        self.frame1_log.place(x=80, y=250)

        self.details_label = Label(self.frame1_log, text='Welcome to Repository and Search engine for Alumni', fg='black', bg='light blue', font=('Verdana',12,'bold'))
        self.details_label.place(x=10, y=10)
        
        self.details_label1 = Label(self.frame1_log, text='PROJECTS DONE BY OUR ALUMNI', fg='black', bg='light blue', font=('Verdana',12,'bold'))
        self.details_label1.place(x=10, y=50)
        
        self.details_label2 = Label(self.frame1_log, text='1: Online bookshop based on web service', fg='black', bg='light blue', font=('Verdana',12,'bold'))
        self.details_label2.place(x=10, y=90)
        
        self.details_label2 = Label(self.frame1_log, text='2: Web based Student Staff Interaction system ', fg='black', bg='light blue', font=('Verdana',12,'bold'))
        self.details_label2.place(x=10, y=130)
        
        self.details_label3 = Label(self.frame1_log, text='3: Web based income tax calculation', fg='black', bg='light blue', font=('Verdana',12,'bold'))
        self.details_label3.place(x=10, y=170)
        
        self.details_label3 = Label(self.frame1_log, text='4: Web based healthcare system', fg='black', bg='light blue', font=('Verdana',12,'bold'))
        self.details_label3.place(x=10, y=210)
        
        self.details_label3 = Label(self.frame1_log, text='5: Stock in Management System', fg='black', bg='light blue', font=('Verdana',12,'bold'))
        self.details_label3.place(x=10, y=250)
        
        self.details_label3 = Label(self.frame1_log, text='6: Private Banking Network', fg='black', bg='light blue', font=('Verdana',12,'bold'))
        self.details_label3.place(x=10, y=290)
        
        self.details_label3 = Label(self.frame1_log, text='7: Telecom Management System', fg='black', bg='light blue', font=('Verdana',12,'bold'))
        self.details_label3.place(x=10, y=330)
        
        self.details_label3 = Label(self.frame1_log, text='8: Network Banking System', fg='black', bg='light blue', font=('Verdana',12,'bold'))
        self.details_label3.place(x=10, y=370)
        
        self.details_label3 = Label(self.frame1_log, text='9: Energy Billing System', fg='black', bg='light blue', font=('Verdana',12,'bold'))
        self.details_label3.place(x=10, y=410)
        
        self.details_label3 = Label(self.frame1_log, text='10: Job Portal', fg='black', bg='light blue', font=('Verdana',12,'bold'))
        self.details_label3.place(x=10, y=450)
        
        

        self.frame_2 = Frame(self.master2, height=500, width=500, bg='white')
        self.frame_2.place(x=950, y=250)
        
        self.log_image_1 = PhotoImage(file = 'stud.png')
        self.log_image_1 = self.log_image_1.subsample(1,1)
        self.label_logimage1 = Label(self.frame_2 , image = self.log_image_1)
        self.label_logimage1.pack(side=LEFT, fill=BOTH, expand=YES)

        self.master2.mainloop()          

    def about_window(self):
        
        top1 = Toplevel()
        top1.title("About us")
        T = Text(top1, height=4, width=30)
        T.pack()
        T.insert(END, "Press Help to know more about us")
        top1.mainloop()

        
    def help_window(self):
        
        top2 = Toplevel()
        top2.title('Help')
        T = Text(top2, height=6, width=30)
        T.pack()
        T.insert(END,  "For any help\nor\nFor more queries\nContact\nRonak Radadiya\n9664869629")
        top2.mainloop()
            
master1= Tk()
master1.image = PhotoImage(file='LOGO.png')
lab1 = Label(master1, image = master1.image, bg='white')
master1.overrideredirect(True)
master1.geometry('+650+250')
master1.lift()
master1.wm_attributes("-topmost", True)
master1.wm_attributes("-disabled", True)
master1.wm_attributes("-transparentcolor", "white")
lab1.pack()
master1.after(3000, lambda: master1.destroy())
master1.mainloop()

c = Login_window()
c.log_window()
