import math
from tkinter import *
main = Tk()
result = 0
def leftClick(event):
    heightcm = int(textBox.get())
    weight = int(textBox02.get())
    heightm = heightcm/100
    result = weight/(heightm*heightm)
    result02 = str(result)[:5]
    if result >= 30:
        print('BMIของคุณคือ :',result02,' คุณอ้วนไป')
        resultext.configure(text='คุณอ้วนไป')
    elif result >= 25:
        print('BMIของคุณคือ :',result02,' คุณอ้วน')
        resultext.configure(text='คุณอ้วน')
    elif result >= 18.6:
        print('BMIของคุณคือ :',result02,' คุณปกติ')
        resultext.configure(text='คุณปกติ')
    elif result <= 18.5:
        print('BMIของคุณคือ :',result02,' คุณผอมไป')
        resultext.configure(text= 'คุณผอมไป')
    else:
        print("ERROR")
labelHeight = Label(main,text='ส่วนสูง (cm)').grid(row=0,column=0)
textBox = Entry(main)
textBox.grid(row=0,column=1)

labelWeight = Label(main,text='น้ำหนัก (kg)').grid(row=1,column=0)
textBox02 = Entry(main)
textBox02.grid(row=1,column=1)

buttonCal = Button(main,text='คำนวณ')
buttonCal.grid(row=3)

resultext = Label(main,text='ผลลัพธ์')
resultext.grid(row=3,column=1)

buttonCal.bind('<Button-1>',leftClick)

main.mainloop()
