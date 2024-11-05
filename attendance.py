from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("Face Recognition System")


        img=Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\collge_images\att1.jpg")
        img=img.resize((700,150),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        #second image
        img1=Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\collge_images\att2.jpg")
        img1=img1.resize((800,150),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)






















if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()