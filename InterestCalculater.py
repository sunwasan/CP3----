import math
from tkinter import *

main = Tk()

def LeftClick (event):
    moneyinput = int(textbox_money.get())  # เงินต้น
    year = int(textbox_year.get())  # จำนวนปี
    dokbia = int(textbox_dokbia.get())  # ดอกเบี้ย
    monthfigure = int(textbox_month.get())  # ทุกกี่เดือน

    x = year *(12/monthfigure)
    y = dokbia *(monthfigure/12)
    z = 1+(y/100)
    result = moneyinput*pow(z,x)
    labelresult.configure(text = result )


labelmoney = Label(main,text="เงินต้น",font=('Chonburi',13))
labelmoney.grid(row=0,column=0)

labelyear= Label(main,text="จำนวนปี",font=('Chonburi',13))
labelyear.grid(row=1,column=0)

labeldokbia = Label(main,text="ดอกเบี้ยต่อปี(%)",font=('Chonburi',13))
labeldokbia.grid(row=2,column=0)

labelmonth = Label(main,text="ทบต้นทุกกี่เดือน",font=('Chonburi',13))
labelmonth.grid(row=3,column=0)

labelresult = Label(main,text="ผลลัพธ์",font=('Chonburi',13))
labelresult.grid(row=4,column=1)

labelthb= Label(main,text="บาท",font=('Chonburi',9))
labelthb.grid(row=4,column=3)

labelcredit= Label(main,text="พัฒนาโดย นาย วสันต์ อารัมภ์สกุล",font=('Chonburi',7))
labelcredit.grid(row=5,column=0)


textbox_money = Entry(main)
textbox_money.grid(row=0,column=1)

textbox_year = Entry(main)
textbox_year.grid(row=1,column=1)

textbox_dokbia = Entry(main)
textbox_dokbia.grid(row=2,column=1)

textbox_month = Entry(main)
textbox_month.grid(row=3,column=1)


buttoncal = Button(main,text = "คำนวณ",font=('Chonburi',10))
buttoncal.grid(row = 4,column=0)

buttoncal.bind('<Button-1>',LeftClick)



main.mainloop()

