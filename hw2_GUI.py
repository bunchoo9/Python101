from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมคำนวณ BMI')
GUI.geometry('500x400')

L1 = Label(GUI, text='โปรแกรมคำนวณ BMI', font=('Angsana New', 30), fg='green')
L1.place(x=30, y=20)

L2 = Label(GUI, text = 'น้ำหนัก (กิโลกรัม) :', font=('Angsana New', 16), fg='black')
L2.place(x=40, y=90)

L2 = Label(GUI, text = 'ส่วนสูง (เมตร) :', font=('Angsana New', 16), fg='black')
L2.place(x=40, y=120)

weight = StringVar()
height = StringVar()

E1 = Entry(GUI, textvariable=weight)
E1.place(x=170, y=95)
E2 = Entry(GUI, textvariable=height)
E2.place(x=170, y=125)

def Calc (event=None) :
    print('กำลังคำนวณ...')
    #weight = float(weight.get())
    #height = float(height.get())
    #print(weight)
    bmi = float(weight.get()) / (float(height.get()) ** 2)
    messagebox.showinfo('bmi', 'BMI = {:,.2f}'.format(bmi))

FB1 = Frame(GUI)
FB1.place(x=170, y=170)
B1 = ttk.Button(FB1,text='คำนวณ bmi', command=Calc)
B1.pack(ipadx=20,ipady=20)   #จัดตำแหน่งปุ่มให้อยู่บน+กลาง

E1.bind ('<Return>', Calc)

GUI.mainloop()




