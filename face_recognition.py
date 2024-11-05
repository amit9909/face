from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x710+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 25, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1350, height=40)

        # Left image
        img_top = Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\collge_images\face recognition.jpg")
        img_top = img_top.resize((550, 600), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=70, width=550, height=600)

        # Right image
        img_bot = Image.open(r"C:\Users\hp\OneDrive\Desktop\khushiii\collge_images\face2.jpg")
        img_bot = img_bot.resize((800, 600), Image.LANCZOS)
        self.photoimg_bot = ImageTk.PhotoImage(img_bot)

        f_lbl = Label(self.root, image=self.photoimg_bot)
        f_lbl.place(x=550, y=70, width=800, height=600)

        # Button
        b1_1 = Button(f_lbl, text="Face Recognition", command=self.face_recog, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=340, y=550, width=200, height=40)

    # Attendance marking function
    def mark_attendance(self, i, r, n, d):
        with open("khushi.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{d1},{dtString},Present")

    # Face recognition function
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100 * (1 - predict / 300))

                conn = mysql.connector.connect(host="127.0.0.1", port=3306, username="root", password="@Amit9909", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = n[0] if n else "Unknown"  # Handle if no data is returned

                my_cursor.execute("SELECT Roll FROM student WHERE Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = r[0] if r else "Unknown"  # Handle if no data is returned

                my_cursor.execute("SELECT Department FROM student WHERE Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = d[0] if d else "Unknown"  # Handle if no data is returned

                my_cursor.execute("SELECT Student_id FROM student WHERE Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = i[0] if i else "Unknown"  # Handle if no data is returned

                if confidence > 77:
                    cv2.putText(img, f"Student_id: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        try:
            # Try using the face recognizer from contrib module
            clf = cv2.face.LBPHFaceRecognizer_create()
        except AttributeError:
            # Handle the case where contrib module is not available
            messagebox.showerror("Error", "LBPH Face Recognizer not found. Please ensure opencv-contrib-python is installed.")
            return

        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Failed to capture image")
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Enter key to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
