from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("Face Recognition System")



        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1350,height=40)

        img_top=Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\collge_images\train2.jpg")
        img_top=img_top.resize((1350,325),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=70,width=1350,height=280)

          #button 
        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=350,width=1350,height=40)

        img_bot=Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\collge_images\train4.jpg")
        img_bot=img_bot.resize((1350,325),Image.LANCZOS)
        self.photoimg_bot=ImageTk.PhotoImage(img_bot)

        f_lbl=Label(self.root,image=self.photoimg_bot)
        f_lbl.place(x=0,y=400,width=1350,height=350)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #  gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)




        #########train the classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")    
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset completed")



if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()