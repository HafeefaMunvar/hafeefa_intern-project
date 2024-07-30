# # # # import cv2
# # # # import os
# # # # import csv
# # # # import numpy as np
# # # # from PIL import Image
# # # # import pandas as pd
# # # # import datetime
# # # # import time
# # # # import pymysql

# # # # from main import assure_path_exists, check_haarcascadefile

# # # # # Function to store attendance data in MySQL
# # # # def store_attendance_in_mysql(attendance_data):
# # # #     try:
# # # #         mydb = pymysql.connect(
# # # #             host="localhost",
# # # #             user="root",
# # # #             password="root",
# # # #             database="your_database"
# # # #         )
# # # #         cursor = mydb.cursor()
        
# # # #         # Insert attendance data into MySQL database
# # # #         for record in attendance_data:
# # # #             cursor.execute("INSERT INTO attendance_table (ID, Name, Date, Time) VALUES (%s, %s, %s, %s)", record)
        
# # # #         mydb.commit()
# # # #         print("Attendance data stored in MySQL successfully!")
        
# # # #     except Exception as e:
# # # #         print("Error storing attendance data in MySQL:", e)
    
# # # #     finally:
# # # #         # Close the database connection
# # # #         mydb.close()

# # # # def TrackImages():
# # # #     check_haarcascadefile()
# # # #     assure_path_exists("Attendance/")
# # # #     assure_path_exists("StudentDetails/")
# # # #     recognizer = cv2.face.LBPHFaceRecognizer_create()
# # # #     exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
# # # #     if exists3:
# # # #         recognizer.read("TrainingImageLabel\Trainner.yml")
# # # #     else:
# # # #         mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!') # type: ignore
# # # #         return
# # # #     harcascadePath = "haarcascade_frontalface_default.xml"
# # # #     faceCascade = cv2.CascadeClassifier(harcascadePath)

# # # #     # Initialize list to store attendance records
# # # #     attendance_data = []

# # # #     cam = cv2.VideoCapture(0)
# # # #     font = cv2.FONT_HERSHEY_SIMPLEX

# # # #     while True:
# # # #         ret, im = cam.read()
# # # #         gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# # # #         faces = faceCascade.detectMultiScale(gray, 1.2, 5)

# # # #         for (x, y, w, h) in faces:
# # # #             cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
# # # #             serial, conf = recognizer.predict(gray[y:y + h, x:x + w])

# # # #             if conf < 50:
# # # #                 ts = time.time()
# # # #                 date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
# # # #                 timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
# # # #                 name = df.loc[df['SERIAL NO.'] == serial]['NAME'].values[0] # type: ignore
# # # #                 ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values[0] # type: ignore
# # # #                 attendance = (ID, name, date, timeStamp)

# # # #                 # Append attendance record to the list
# # # #                 attendance_data.append(attendance)

# # # #             else:
# # # #                 name = 'Unknown'

# # # #             cv2.putText(im, str(name), (x, y + h), font, 1, (255, 255, 255), 2)

# # # #         cv2.imshow('Taking Attendance', im)
# # # #         if cv2.waitKey(1) == ord('q'):
# # # #             break

# # # #     cam.release()
# # # #     cv2.destroyAllWindows()

# # # #     # Store attendance data in MySQL
# # # #     store_attendance_in_mysql(attendance_data)

# # # #     # Update GUI or perform any other necessary actions

# # # #     # Display attendance data in table (optional)
# # # #     # display_attendance(attendance_data)



# # # # import sqlite3

# # # # # database = sqlite3.connect('users.db')



# # # # def insertData(name,date,time):
# # # #     database = sqlite3.connect('users.db')
# # # #     cursor = database.cursor()
# # # #     qry = "insert into users (NAME,DATE,TIME) Values(?,?,?);"
# # # #     cursor.execute(qry,(name,date,time))
# # # #     database.commit()
# # # #     database.close()
# # # #     print("added")

# # # # insertData("govi", "2023-05-08", "12:00")

# # # # import sqlite3
# # # # class database:
# # # #     def __init__(self,db):
# # # #         self.con = sqlite3.connect(db)
# # # #         self.cur = self.con.cursor()
# # # #         sql ="""
# # # #         CREATE TABLE IF NOT EXISTS attendance(
# # # #         id Integer Primary Key,
# # # #         name text,
# # # #         date text,
# # # #         time text,
# # # #         )

# # # #         """
# # # #         self.cur.execute(sql)
# # # #         self.con.commit()
# # # # o = database("details")        


# # # # import mysql.connector
# # # # import cv2
# # # # import os
# # # # import pandas as pd
# # # # import numpy as np
# # # # import csv
# # # # import time
# # # # import datetime

# # # # # Establish connection to the database
# # # # database = mysql.connector.connect(host='localhost', password='Govi@123', user='root', database='attendance_sheet')

# # # # if database.is_connected:
# # # #     print("Connection successful")
# # # # else:
# # # #     print("Connection failed")


# # # # def check_haarcascadefile():
# # # #     exists = os.path.isfile("haarcascade_frontalface_default.xml")
# # # #     if exists:
# # # #         # TrackImages()
# # # #         pass
# # # #     else:
# # # #         mess._show(title='Some file missing', message='Please contact us for help')
# # # #         window.destroy()



# # # import mysql.connector
# # # import cv2
# # # import os
# # # import pandas as pd
# # # import numpy as np
# # # import csv
# # # import time
# # # import datetime

# # # # Establish connection to the database
# # # database = mysql.connector.connect(host='localhost', password='Govi@123', user='root', database='attendance_sheet')

# # # if database.is_connected:
# # #     print("Connection successful")
# # # else:
# # #     print("Connection failed")



# # # def check_haarcascadefile():
# # #     exists = os.path.isfile("haarcascade_frontalface_default.xml")
# # #     if exists:
# # #         # TrackImages()
# # #         pass
# # #     else:
# # #         mess._show(title='Some file missing', message='Please contact us for help')
# # #         window.destroy()






# # # def TrackImages():
# # #     attendance_records = [] 
    
# # #     check_haarcascadefile()
# # #     # assure_path_exists("Attendance/")
# # #     # assure_path_exists("StudentDetails/")
# # #     # for k in tv.get_children():
# # #     #     tv.delete(k)
# # #     msg = ''
# # #     i = 0
# # #     j = 0
# # #     recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
# # #     exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
# # #     if exists3:
# # #         recognizer.read("TrainingImageLabel\Trainner.yml")
# # #     else:
# # #         mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
# # #         return
# # #     harcascadePath = "haarcascade_frontalface_default.xml"
# # #     faceCascade = cv2.CascadeClassifier(harcascadePath);

# # #     cam = cv2.VideoCapture(0)
# # #     font = cv2.FONT_HERSHEY_SIMPLEX
# # #     col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
# # #     exists1 = os.path.isfile("StudentDetails\StudentDetails.csv")
# # #     if exists1:
# # #         df = pd.read_csv("StudentDetails\StudentDetails.csv")
# # #     else:
# # #         mess._show(title='Details Missing', message='Students details are missing, please check!')
# # #         cam.release()
# # #         cv2.destroyAllWindows()
# # #         window.destroy()
# # #         return
    
# # #     while True:
# # #         ret, im = cam.read()
# # #         gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# # #         faces = faceCascade.detectMultiScale(gray,1.2,5)
# # #         for (x, y, w, h) in faces:
# # #             cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
# # #             serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
# # #             if (conf < 50):
# # #                 ts = time.time()
# # #                 date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
# # #                 timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
# # #                 aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
# # #                 ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
# # #                 ID = str(ID)
# # #                 ID = ID[1:-1]
# # #                 bb = str(aa)
# # #                 bb = bb[2:-2]
# # #                 attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]
# # #                 attendance_records.append(attendance)  # Append attendance record to list

# # #             else:
# # #                 Id = 'Unknown'
# # #                 bb = str(Id)
# # #             cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
# # #         cv2.imshow('Taking Attendance', im)
# # #         if (cv2.waitKey(1) == ord('q')):
# # #             break
    
# # #     # Release the camera
# # #     cam.release()
# # #     cv2.destroyAllWindows()

# # #     # Insert attendance data into MySQL database
# # #     cursor = database.cursor()
# # #     for attendance_record in attendance_records:
# # #         try:
# # #             cursor.execute("INSERT INTO attendance_table (ID, Name, Date, Time) VALUES (%s, %s, %s, %s)", 
# # #                            (attendance_record[0], attendance_record[2], attendance_record[4], attendance_record[6]))
# # #             database.commit()
# # #         except mysql.connector.Error as err:
# # #             print("Error inserting record:", err)
# # #             database.rollback()

# # #     cursor.close()

# # #     # Your existing code for displaying attendance

# # #     database.close()  # Close the database connection

# # # # Call the TrackImages function to start tracking attendance
# # # TrackImages()


# # import tkinter
# # from tkinter import PhotoImage

# # root = tkinter.Tk()
# # root.title("Hello")
# # root.geometry("1250x720")
# # image_path = PhotoImage(file="C:\\Users\\HP\\Downloads\\download.png")
# # add = tkinter.Label(root,image=image_path)
# # add.place(relheight=1,relwidth=1)
# # root.mainloop()

# import tkinter
# from PIL import Image, ImageTk

# root = tkinter.Tk()
# root.title("hello")
# root.geometry('1000x750')

# # Open the image using PIL
# pic = Image.open("images\\facial_recognition.png")

# # Resize the image
# resized_image = pic.resize((1000, 800), Image.ANTIALIAS)

# # Convert the resized image to PhotoImage
# new_pic = ImageTk.PhotoImage(resized_image)

# # Create a label to display the image
# my_label = tkinter.Label(root, image=new_pic)
# my_label.pack(pady=20)

# root.mainloop()

c = 0
while c != 0:
    c = c-1
    print(c)
