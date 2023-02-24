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
GUI.geometry('650x300')

L1 = Label(GUI, text='โปรแกรมบันทึกความรู้', font=('Angsana New', 30), fg='green')
L1.place(x=30, y=20)


###### Notebook #######
Tab = ttk.Notebook(GUI)

T1 = Frame(Tab)
T2 = Frame(Tab)

Tab.pack(fill=BOTH,expand=1)

Tab.add(T1,text='Insert')
Tab.add(T2,text='ShowData')

# ***************** Tab 1 *******************#
###### Insert #######
LF1 = ttk.LabelFrame(T1, text='กรอกข้อมูลที่ต้องการเข้าไป')
LF1.pack(pady=30)

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

# ***************** Tab 2 *******************#
###### ShowData #######
LF2 = ttk.LabelFrame(T2, text='แสดงข้อมูลที่บันทึก')
LF2.pack(pady=20)

# อ่านไฟล์ CSV
df = pd.read_csv('data.csv')

# สร้างตาราง GUI ด้วย Pandas
table = ttk.Treeview(LF2)
#table.delete(*table.get_children())
table["columns"] = tuple(df.columns)
for column in table["columns"]:
    table.heading(column, text=column)
for index, row in df.iterrows():
    table.insert("", index, text=index, values=tuple(row))
table.pack(fill="both", expand=True)


GUI.mainloop()




