from tkinter import *
root= Tk()


root.configure(background="light pink")
e1=Entry(root,width=30,borderwidth=5)
e1.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):

    current=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(current)+str(number))

def Button_del():
    e=e1.get()
    e1.delete(len(e)-1)


def Button_clear():
    e1.delete(0,END)

def Button_add():
    first_number=e1.get()
    global f_num
    global math
    math='addition'
    f_num=int(first_number)
    e1.delete(0,END)

def Button_equal():
    second_number = e1.get()
    e1.delete(0,END)
    if math=="addition":
        e1.insert(0, f_num + int(second_number))

    if math=="subtraction":
        e1.insert(0, f_num - int(second_number))

    if math=="division":
        e1.insert(0, f_num / int(second_number))

    if math=="multiplication":
        e1.insert(0, f_num * int(second_number))




def Button_sub():
    first_number = e1.get()
    global f_num
    global math
    math='subtraction'
    f_num = int(first_number)
    e1.delete(0, END)


def Button_div():
    first_number = e1.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e1.delete(0, END)


def Button_mul():
    first_number = e1.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e1.delete(0, END)




button1 = Button(root,text="1",activebackground='gray',padx=40,pady=20,command=lambda:button_click(1))
button2=Button(root,text="2",activebackground='gray',padx=40,pady=20,command=lambda:button_click(2))
button3=Button(root,text="3",activebackground='gray',padx=40,pady=20,command=lambda:button_click(3))

button4=Button(root,text="4",activebackground='gray',padx=40,pady=20,command=lambda:button_click(4))
button5=Button(root,text="5",activebackground='gray',padx=40,pady=20,command=lambda:button_click(5))
button6=Button(root,text="6",activebackground='gray',padx=40,pady=20,command=lambda:button_click(6))

button7=Button(root,text="7",activebackground='gray',padx=40,pady=20,command=lambda:button_click(7))
button8=Button(root,text="8",activebackground='gray',padx=40,pady=20,command=lambda:button_click(8))
button9=Button(root,text="9",activebackground='gray',padx=40,pady=20,command=lambda:button_click(9))

button0=Button(root,text="0",activebackground='gray',padx=40,pady=20,command=lambda:button_click(0))
button00=Button(root,text="00",activebackground='gray',padx=37,pady=20,command=lambda:button_click("00"))
button_clear=Button(root,text="Clear",activebackground='light green',padx=77,pady=20,command=Button_clear)

button_add=Button(root,text="+",activebackground='gray',padx=40,pady=20,command=Button_add)
button_sub=Button(root,text="-",activebackground='gray',padx=40,pady=20,command=Button_sub)
button_equal=Button(root,text="=",activebackground='gray',padx=89,pady=20,command=Button_equal)

button_mul=Button(root,text="*",activebackground='gray',padx=39,pady=20,command=Button_mul)
button_div=Button(root,text="/",activebackground='gray',padx=40,pady=20,command=Button_div)
button_del=Button(root,text="del",activebackground='gray',padx=35,pady=20,command=Button_del)



#put the buttons on the screen

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button_div.grid(row=3,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button_del.grid(row=2,column=3)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button_mul.grid(row=1,column=3)

button0.grid(row=4,column=0)
button00.grid(row=4,column=1)
button_clear.grid(row=4,column=2,columnspan=3)


button_add.grid(row=5,column=0)
button_sub.grid(row=5,column=1)
button_equal.grid(row=5,column=2,columnspan=3)




















root.mainloop()