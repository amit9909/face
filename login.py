from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Load the image
        original_image = Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\login\image\bg.jpg")
        
        # Resize the image (for example, 1600x900)
        resized_image = original_image.resize((1530, 720), Image.LANCZOS)  # Using Image.LANCZOS instead of Image.ANTIALIAS

        # Convert the resized image to a Tkinter-compatible photo image
        self.bg = ImageTk.PhotoImage(resized_image)

        # Create a Label widget with the background image
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="white")
        frame.place(x=510, y=170, width=340, height=450)

        img1 = Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\login\image\icon2.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        # Define the label to display the image
        lblimg1 = Label(self.root, image=self.photoimage1, bg="white")
        lblimg1.place(x=650, y=175, width=80, height=80)

        get_str = Label(frame, text="Get Started", font=("times ner roman", 20, "bold"), fg="green", bg="white")
        get_str.place(x=95, y=100)

        ############ label
        username = Label(frame, text="Username", font=("times ner roman", 20, "bold"), fg="black", bg="white")
        username.place(x=70, y=145)

        self.txtuser = ttk.Entry(frame, font=("times ner roman", 20, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text="Password", font=("times ner roman", 20, "bold"), fg="black", bg="white")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times ner roman", 20, "bold"))
        self.txtpass.place(x=40, y=260, width=270)

        ##################### icon images
        img2 = Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\login\image\icon2.png")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimage2)
        lblimg2.place(x=540, y=315, width=35, height=35)

        img3 = Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\login\image\icon3.jpeg")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(self.root, image=self.photoimage3)
        lblimg3.place(x=540, y=395, width=35, height=35)

        ################ login button
        loginbtn = Button(frame, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="black", bg="white", activeforeground="black", activebackground="light green", command=self.login)
        loginbtn.place(x=110, y=315, width=120, height=30)

        regbtn = Button(frame, text="New User Register",command=self.register_window, font=("times new roman", 15, "bold"), borderwidth=0, fg="black", bg="white", activeforeground="black", activebackground="light green")
        regbtn.place(x=20, y=350, width=160)

        frgtbtn = Button(frame, text="Forget Password",command=self.forgot_password_window, font=("times new roman", 15, "bold"), borderwidth=0, bg="white", activeforeground="black", activebackground="light green")
        frgtbtn.place(x=20, y=378, width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    # Define the login method
    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All Fields Required")
        elif self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu":
            messagebox.showinfo("Success", "Welcome..................")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="@Amit9909",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                      self.txtuser.get(),
                                                                                      self.txtpass.get()

                                                                                     ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            self.clear()
            conn.close()

            ##############################################reset password###########
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter the new Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="@Amit9909",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset , please enter the new password",parent=self.root2)
                self.root2.destroy()



        #################################################forget password

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email Address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="@Amit9909",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("My Eror","Please Enter ther Valid Email or username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"), fg="black", bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2,  font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Girlfriend Name", "Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), fg="black", bg="white")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2,  font=("times new roman", 15, "bold"))
                self.txt_security.place(x=50, y=180, width=250)






                new_password= Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2,  font=("times new roman", 15, "bold"))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",font=("times new roman",15,"bold"),fg="white",bg="black")
                btn.place(x=100,y=270)



            






class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        ##################################variables#############################
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # Load the image
        original_image = Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\login\image\reg2.jpeg")
        resized_image = original_image.resize((1530, 720), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(resized_image)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        ###########################left image
        original_image = Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\login\image\reg4.jpeg")
        resized_image = original_image.resize((1530, 720), Image.LANCZOS)
        self.bg1 = ImageTk.PhotoImage(resized_image)
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        frame = Frame(self.root, bg="white")
        frame.place(x=510, y=100, width=600, height=550)

        register_lbl = Label(frame, text="REGISTER HERE..", font=("times new roman", 20, "bold"), fg="green", bg="white")
        register_lbl.place(x=20, y=20)

        #####################label AND entry
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), fg="black", bg="white")
        fname.place(x=50, y=100)

        self.txt_fname = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.txt_fname.place(x=50, y=130, width=250)

        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), fg="black", bg="white")
        lname.place(x=330, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=330, y=130, width=250)

        ##########################2row
        contact = Label(frame, text="Contact", font=("times new roman", 15, "bold"), fg="black", bg="white")
        contact.place(x=50, y=170)
        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), fg="black", bg="white")
        email.place(x=330, y=170)
        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=330, y=200, width=250)

        ###############row 3
        security_Q = Label(frame, text="Security Question", font=("times new roman", 15, "bold"), fg="black", bg="white")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Girlfriend Name", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), fg="black", bg="white")
        security_A.place(x=330, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_SecurityA, font=("times new roman", 15, "bold"))
        self.txt_security.place(x=330, y=270, width=250)

        ##############################4th row
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        password.place(x=50, y=310)

        self.txt_password = ttk.Entry(frame, textvariable=self.var_pass, show="*", font=("times new roman", 15, "bold"))
        self.txt_password.place(x=50, y=340, width=250)

        confirm_password = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        confirm_password.place(x=330, y=310)

        self.txt_confirm_password = ttk.Entry(frame, textvariable=self.var_confpass, show="*", font=("times new roman", 15, "bold"))
        self.txt_confirm_password.place(x=330, y=340, width=250)

        ##################### check button
        self.var_check = IntVar()
        Checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", font=("times new roman", 13, "bold"), onvalue=1, offvalue=0)
        Checkbtn.place(x=50, y=390)

        ##################buttons
        img = Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\login\image\btn 1.png")
        img = img.resize((200, 50), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        b1.place(x=10, y=440, width=200)

        img1 = Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\login\image\login.jpegg")
        img1 = img1.resize((200, 50), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame, image=self.photoimage1,command=self.return_login, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        b2.place(x=300, y=440, width=200)

    ################################function
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "password and confirm password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please Agree Our Terms & Conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="@Amit9909",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row =my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already exist , please try another email...")
            else:
                my_cursor.execute("insert into register values (%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),               
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_SecurityA.get(),
                                                                                        self.var_pass.get()


                                                                                                       ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully!")

        def return_login(self):
            self.root.destroy()


if __name__ == "__main__":
    main()