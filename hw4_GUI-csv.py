from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
import pandas as pd

#####csv######
import csv

def writecsv(datalist):
    with open('data.csv', 'a', encoding='utf-8', newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) #datalist = ['pen','pencil','eraser']

def readcsv():
    with open('data.csv', encoding='utf-8', newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data
###########

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('1000x450')

L1 = Label(GUI, text='โปรแกรมบันทึกความรู้', font=('Angsana New', 30), fg='green')
L1.place(x=30, y=20)


###### Right Section ######
LF1 = ttk.LabelFrame(GUI, text='กรอกข้อมูลที่ต้องการเข้าไป')
LF1.place(x=50, y=90)

v_data = StringVar()    #ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E1 = ttk.Entry(LF1, textvariable=v_data, font=('Angsana New',25))
E1.pack(pady=10, padx=10)

from datetime import datetime

def SaveData() :
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t,data] #[เวลา, ข้อมูลที่กรอก]
    writecsv(text)  #บันทึกข้อมูล csv
    v_data.set('')  #เคลียร์ข้อมูลทีอยู่ในช่องกรอก

B4 = ttk.Button(LF1, text='บันทึก', command=SaveData)
B4.pack(ipady=20,ipadx=20)

#B5 = ttk.Button(LF1, text='แสดงข้อมูล', command=ShowData)
#B5.pack(ipady=20,ipadx=20)

###### Report Section ######
LF2 = ttk.LabelFrame(GUI, text='Report')
LF2.place(x=350, y=90)

def Button5():
    #text = readcsv()
    #messagebox.showinfo('report', text)

    # อ่านไฟล์ CSV
    df = pd.read_csv('data.csv')

    # สร้างตาราง GUI ด้วย Pandas
    table = ttk.Treeview(LF2)
    table["columns"] = tuple(df.columns)
    for column in table["columns"]:
        table.heading(column, text=column)
    for index, row in df.iterrows():
        table.insert("", index, text=index, values=tuple(row))
    table.pack(fill="both", expand=True)

B5 = ttk.Button(LF2,text='แสดงข้อมูล', command=Button5)
B5.pack(ipadx=20,ipady=20)   #จัดตำแหน่งปุ่มให้อยู่บน+กลาง



GUI.mainloop()




