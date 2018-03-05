from tkinter import  *

cal = Tk()
cal.title('Calculator')

try:
    cal.wm_iconbitmap('calc.ico')
except:
    pass

operator = ''
text_Input = StringVar()

def btnClick(numbers):
    global operator
    operator += str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ''
    text_Input.set('')

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ''


txtDislay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=20, insertwidth = 4, bg='orange', justify='right').grid(columnspan=4)


btn7 = Button(cal, padx=20, pady=16, bd=4, fg='black', font=('arial', 15, 'bold'), text='7', bg='orange', command=lambda:btnClick(7)).grid(row=2, column=0)
btn8 = Button(cal, padx=20, pady=16, bd=4, fg='black', font=('arial', 15, 'bold'), text='8', bg='orange', command=lambda:btnClick(8)).grid(row=2, column=1)
btn9 = Button(cal, padx=20, pady=16, bd=4, fg='black', font=('arial', 15, 'bold'), text='9', bg='orange', command=lambda:btnClick(9)).grid(row=2, column=2)

div = Button(cal, padx=20, pady=16, bd=4, fg= 'black', font=('arial', 15, 'bold'), text='/', bg='orange', command=lambda:btnClick('/')).grid(row=2, column=3)

#================================================================================================================

btn4 = Button(cal, padx=20, pady=16, bd=4, fg='black', font=('arial', 15, 'bold'), text='4', bg='orange', command=lambda:btnClick(4)).grid(row=3, column=0)
btn5 = Button(cal, padx=20, pady=16, bd=4, fg='black', font=('arial', 15, 'bold'), text='5', bg='orange', command=lambda:btnClick(5)).grid(row=3, column=1)
btn6 = Button(cal, padx=20, pady=16, bd=4, fg='black', font=('arial', 15, 'bold'), text='6', bg='orange', command=lambda:btnClick(6)).grid(row=3, column=2)

add = Button(cal, padx=20, pady=16, bd=4, fg= 'black', font=('arial', 15, 'bold'), text='+', bg='orange', command=lambda:btnClick('+')).grid(row=3, column=3)

#================================================================================================================

btn1 = Button(cal, padx=20, pady=16, bd=4, fg= 'black', font=('arial', 15, 'bold'), text='1', bg='orange', command=lambda:btnClick(1)).grid(row=4, column=0)
btn2 = Button(cal, padx=20, pady=16, bd=4, fg= 'black', font=('arial', 15, 'bold'), text='2', bg='orange', command=lambda:btnClick(2)).grid(row=4, column=1)
btn3 = Button(cal, padx=20, pady=16, bd=4, fg= 'black', font=('arial', 15, 'bold'), text='3', bg='orange', command=lambda:btnClick(3)).grid(row=4, column=2)

minus= Button(cal, padx=20, pady=16, bd=4, fg= 'black', font=('arial', 15, 'bold'), text='-', bg='orange', command=lambda:btnClick('-')).grid(row=4, column=3)

#================================================================================================================


mult = Button(cal, padx=20, pady=16, bd=4, fg='black', font=('arial', 15, 'bold'), text='*', bg='orange', command=lambda:btnClick('*')).grid(row=1, column=3)
btnL = Button(cal, padx=20, pady=16, bd=4, fg='black', font=('arial', 15, 'bold'), text='L', bg='orange').grid(row=1, column=0)
btnM = Button(cal, padx=20, pady=16, bd=4, fg='black', font=('arial', 15, 'bold'), text='M', bg='orange').grid(row=1, column=1)
btnK = Button(cal, padx=20, pady=16, bd=4, fg='black', font=('arial', 15, 'bold'), text='K', bg='orange').grid(row=1, column=2)

#================================================================================================================

dcml = Button(cal, padx=20, pady=16, bd=4, fg='black', font=('arial', 15, 'bold'), text='.', bg='orange', command=lambda:btnClick('.')).grid(row=5, column=1)
btn0 = Button(cal, padx=20, pady=16, bd=4, fg='black', font=('arial', 15, 'bold'), text='0', bg='orange', command=lambda:btnClick(0)).grid(row=5, column=0)
btnC = Button(cal, padx=20, pady=16, bd=4, fg='black', font=('arial', 15, 'bold'), text='C', bg='orange', command = btnClearDisplay).grid(row=5, column=2)
equals = Button(cal, padx=20, pady=16, bd=4, fg='black', font=('arial', 15, 'bold'), text='=', bg='orange', command =btnEqualsInput).grid(row=5, column=3)


cal.mainloop()
