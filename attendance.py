from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x710+0+0")
        self.root.title("Face Recognition System")


        ############# variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        # First Image
        img = Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\collge_images\att1.jpg")
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # Second Image
        img1 = Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\collge_images\att2.jpg")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

        # Background Image
        img3 = Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\collge_images\atttt_new.jpg")
        img3 = img3.resize((1530, 650), Image.LANCZOS)  # Resize to fit the window size
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=180, width=1530, height=710)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1430, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)

        # Left Label Frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=0, y=10, width=700, height=580)

        img_left = Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\collge_images\student4.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=0, width=700, height=130)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=160, width=680, height=300)

        # Label and entry fields
        # Attendance ID
        attendanceId_label = Label(left_inside_frame, text="AttendanceID:", font=("times new roman", 13, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_id, font=("times new roman", 13, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll
        rollLabel = Label(left_inside_frame, text="Roll:", bg="white", font="comicsansns 11 bold")
        rollLabel.grid(row=0, column=2, padx=4, pady=8)

        atten_roll = ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll, width=22, font="comicsansns 11 bold")
        atten_roll.grid(row=0, column=3, pady=8)

        # Name
        nameLabel = Label(left_inside_frame, text="Name:", bg="white", font="comicsansns 11 bold")
        nameLabel.grid(row=1, column=0)

        atten_name = ttk.Entry(left_inside_frame, textvariable=self.var_atten_name,width=22, font="comicsansns 11 bold")
        atten_name.grid(row=1, column=1, pady=8)

        # Department
        depLabel = Label(left_inside_frame, text="Department:", bg="white", font="comicsansns 11 bold")
        depLabel.grid(row=1, column=2)

        atten_dep = ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep, width=22, font="comicsansns 11 bold")
        atten_dep.grid(row=1, column=3, pady=8)

        # Time
        timeLabel = Label(left_inside_frame, text="Time:", bg="white", font="comicsansns 11 bold")
        timeLabel.grid(row=2, column=0)

        atten_time = ttk.Entry(left_inside_frame,textvariable=self.var_atten_time, width=22, font="comicsansns 11 bold")
        atten_time.grid(row=2, column=1, pady=8)

        # Date
        dateLabel = Label(left_inside_frame, text="Date:", bg="white", font="comicsansns 11 bold")
        dateLabel.grid(row=2, column=2)

        atten_date = ttk.Entry(left_inside_frame,textvariable=self.var_atten_date, width=22, font="comicsansns 11 bold")
        atten_date.grid(row=2, column=3, pady=8)

        # Attendance
        attendanceLabel = Label(left_inside_frame, text="Attendance Status:", bg="white", font="comicsansns 11 bold")
        attendanceLabel.grid(row=3, column=0)

        self.atten_status = ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,width=20, font="comicsansns 11 bold")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # Button Frame
        btn_frame = Frame(left_inside_frame, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=250, width=700, height=35)

        save_btn = Button(btn_frame, text="Import csv",command=self.importcsv,width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export csv",command=self.exportcsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # Right Label Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=660, height=580)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=565, height=420)

        # Scrollbars for the table
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("id", "roll", "name", "department", "time", "date", "attendance"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")



        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<<TreeviewSelect>>", self.get_cursor)





        ###################### fetch data

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)


            #############import csv

    def importcsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


#########################export csv
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",Parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                    messagebox.showinfo("Data Export","Your Data Exported to " +os.path.basename(fln)+"Successfully")
        except Exception as es:
            print(f"Error: {str(es)}")  # Add this line to print the error to the console
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        





if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()