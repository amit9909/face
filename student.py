from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("Face Recognition System")



        # Variables*******************************
        self.var_department=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_division=StringVar()
        self.var_roll_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



         #first image
        img=Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\collge_images\student1.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\collge_images\student2.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=130)

        #third image
        img2=Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\collge_images\student3.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

           #background image
        img3=Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\collge_images\bg.jpg")
        img3=img3.resize((1230,650),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)
  
        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=0,y=10,width=700,height=580)

        img_left=Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\collge_images\student4.jpg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=700,height=130)






        # current course
        current_course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=0,y=135,width=720,height=115)
        
        #department 
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)   
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_department,font=("times new roman",12,"bold"),state="read only")
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-2021","2021-22","2022-23","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","semester-1","semester-2","semester-3","semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

         # class student information
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=220,width=720,height=320)
         

         #student id
        studentId_label=Label(class_Student_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.va_std_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

            #student name
        studentName_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_Student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

       
        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_division,font=("times new roman",13,"bold"),state="readonly",width=17)
        div_combo["values"]=("Select","A","B","C","D","E","FAIL")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

            #roll no.
        roll_no_label=Label(class_Student_frame,text="Roll Number:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll_no,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=17)
        gender_combo["values"]=("Select","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)

          #DOB
        dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

          #EMAIL
        email_label=Label(class_Student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

         #PHONE NUMBER
        phone_label=Label(class_Student_frame,text="Phone Number:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

         #ADDRESS
        address_label=Label(class_Student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

         #TEACHER NAME
        teacher_label=Label(class_Student_frame,text="TeacherName:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)

        # buttons frame
        btn_frame=Frame(class_Student_frame,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=700,height=35)

        save_btn=Button(btn_frame,text="save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

         # buttons frame
        btn_frame1=Frame(class_Student_frame,relief=RIDGE)
        btn_frame1.place(x=0,y=235,width=700,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

      # Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=660,height=580)

        img_right=Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\collge_images\student5.jpg")
        img_right=img_right.resize((700,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=700,height=130)


      # search system ***********************************
       
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Serach System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="readonly",width=11)
        search_combo["values"]=("Select ","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=11,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=9,font=("times new roman",11,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=3)

        showAll_btn=Button(search_frame,text="Show All",width=9,font=("times new roman",11,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=3)

       #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=200,width=700,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("Department","Course","Year","Semester","id","Name","Division","Roll_No","Gender","DOB","Email","Gender","Phone","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Division",text="Divison")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"



        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Division",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        
     #**********************function
    def add_data(self):
        if self.var_department.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required!",parent=self.root)
        else:
            try:
                # print("wroking")
                conn=mysql.connector.connect(host="127.0.0.1", port=3306, username="root", password="@Amit9909", database="face_recognizer")
                my_cursor=conn.cursor()
                # print("working2")
                my_cursor.execute("INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (


                    self.var_department.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.va_std_id.get(),
                    self.var_std_name.get(),
                    self.var_division.get(),
                    self.var_roll_no.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
            ))
                self.fetch_data()
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Students details has been added Successfully ",parent=self.root)
            except Exception as es:
              print(f"Error: {str(es)}")  # Add this line to print the error to the console
              messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


    def fetch_data(self):
       conn=mysql.connector.connect(host="127.0.0.1", port=3306, username="root", password="@Amit9909", database="face_recognizer")
       my_cursor=conn.cursor()
       my_cursor.execute("Select * from student")
       data=my_cursor.fetchall()

       if len(data)!=0:
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
          self.student_table.insert("",END,values=i)
        conn.commit()
       conn.close()


        #========================get cursor======================
    def get_cursor(self,event=""):
      cursor_focus=self.student_table.focus()
      content=self.student_table.item(cursor_focus)
      Data=content["values"]

      self.var_department.set(Data[0]),
      self.var_course.set(Data[1]),
      self.var_year.set(Data[2]),
      self.var_semester.set(Data[3]),
      self.va_std_id.set(Data[4]),
      self.var_std_name.set(Data[5]),
      self.var_division.set(Data[6]),
      self.var_roll_no.set(Data[7]),
      self.var_gender.set(Data[8]),
      self.var_dob.set(Data[9]),
      self.var_email.set(Data[10]),
      self.var_phone.set(Data[11]),
      self.var_address.set(Data[12]),
      self.var_teacher.set(Data[13]),
      self.var_radio1.set(Data[14])

      ##########******************update function
    def update_data(self):
      if self.var_department.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required!",parent=self.root)
      else:
        try:
          update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
          if update>0:
              conn=mysql.connector.connect(host="127.0.0.1", port=3306, username="root", password="@Amit9909", database="face_recognizer")
              my_cursor=conn.cursor()
              my_cursor.execute("UPDATE student SET Department=%s, Course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s", (
                                                                      self.var_department.get(),
                                                                      self.var_course.get(),
                                                                      self.var_year.get(),
                                                                      self.var_semester.get(),
                                                                      self.var_division.get(),
                                                                      self.var_roll_no.get(),
                                                                      self.var_gender.get(),
                                                                      self.var_dob.get(),
                                                                      self.var_email.get(),
                                                                      self.var_phone.get(),
                                                                      self.var_address.get(),
                                                                      self.var_teacher.get(),
                                                                      self.var_radio1.get(),
                                                                      self.va_std_id.get()  # Corrected variable name here
                                                                                                                  ))
          else:
            if not update:
              return
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Success","Students details updated Successfully ",parent=self.root)
              # self.fetch_data()
              # conn.commit()
              # conn.close()
              # messagebox.showinfo("Success","Students details has been added Successfully ",parent=self.root)
        except Exception as es:
              print(f"Error: {str(es)}")  # Add this line to print the error to the console
              messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
        



#delete function
    def delete_data(self):
      if self.va_std_id.get()=="":
        messagebox.showerror("Error","Student id must be required",parent=self.root)
      else:
        try:
          delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
          if delete>0:
            conn=mysql.connector.connect(host="127.0.0.1", port=3306, username="root", password="@Amit9909", database="face_recognizer")
            my_cursor=conn.cursor()
            sql="delete from student where Student_id=%s"
            val=(self.va_std_id.get(),)
            my_cursor.execute(sql,val)
          else:
            if not delete:
              return

          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
        except Exception as es:
             print(f"Error: {str(es)}")  # Add this line to print the error to the console
             messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


   #reset
    def reset_data(self):
      self.var_department.set("Select Department")
      self.var_course.set("Select Course")
      self.var_year.set("Select Year")
      self.var_semester.set("Select Semester")
      self.va_std_id.set("")
      self.var_std_name.set("")
      self.var_division.set("Select Division")
      self.var_roll_no.set("")
      self.var_gender.set("Male")
      self.var_dob.set("")
      self.var_email.set("")
      self.var_phone.set("")
      self.var_address.set("")
      self.var_teacher.set("")
      self.var_radio1.set("")
      

              
#*******************************generate dataset or take photo sample****************
    def generate_dataset(self):
      if self.var_department.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
       messagebox.showerror("Error","All Fields are required!",parent=self.root)
      else:
        try:
          conn=mysql.connector.connect(host="127.0.0.1", port=3306, username="root", password="@Amit9909", database="face_recognizer")
          my_cursor=conn.cursor()
          my_cursor.execute("select * from student")
          myresult=my_cursor.fetchall()
          id=0
          for x in myresult:
            id+=1
          my_cursor.execute("UPDATE student SET Department=%s, Course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s", (
                                                                      self.var_department.get(),
                                                                      self.var_course.get(),
                                                                      self.var_year.get(),
                                                                      self.var_semester.get(),
                                                                      self.var_division.get(),
                                                                      self.var_roll_no.get(),
                                                                      self.var_gender.get(),
                                                                      self.var_dob.get(),
                                                                      self.var_email.get(),
                                                                      self.var_phone.get(),
                                                                      self.var_address.get(),
                                                                      self.var_teacher.get(),
                                                                      self.var_radio1.get(),
                                                                      self.va_std_id.get()==id+1  # Corrected variable name here
                                                                 ))
          conn.commit()
          self.fetch_data()
          self.reset_data()
          conn.close()

          # load predefined data on face frontals from open cv**********
          face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

          def face_cropped(img):
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=face_classifier.detectMultiScale(gray,1.3,5)
            #scaling factor 1.3
            #minimum neighbor=5

            for (x,y,w,h) in faces:
              face_cropped=img[y:y+h,x:x+w]
              return face_cropped

          cap=cv2.VideoCapture(0)
          img_id=0
          while True:
            ret, my_frame = cap.read()
            if face_cropped(my_frame) is not None:
                img_id += 1
                face = cv2.resize(face_cropped(my_frame), (450, 450))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                file_name_path = f"data/user.{id}.{img_id}.jpg"
                cv2.imwrite(file_name_path, face)

                # Define the position for the text
                text_position = (10, 30)  # Adjust as needed

                # Use putText with the defined position
                cv2.putText(face, str(img_id), text_position, cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                cv2.imshow("Cropped Face", face)

                if cv2.waitKey(1) == 13 or int(img_id) == 15:
                 break

          cap.release()
          cv2.destroyAllWindows()
          messagebox.showinfo("Result","Generating data sets completed !!!!!")
        except Exception as es:
             print(f"Error: {str(es)}")  # Add this line to print the error to the console
             messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)     

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()