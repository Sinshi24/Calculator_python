from tkinter import * 
root = Tk()

display=Entry(root)
display.get()

def butt_click(num):
    current=display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(num))

def butt_clr():
    display.delete(0, END)

def butt_add():
    return

def butt_sus():
    return

def butt_mul():
    return

b0 = Button(root, text='0', command=lambda: butt_click(0))

b1 = Button(root, text='1', command=lambda: butt_click(1))
b2 = Button(root, text='2', command=lambda: butt_click(2))
b3 = Button(root, text='3', command=lambda: butt_click(3))

b4 = Button(root, text='4', command=lambda: butt_click(4))
b5 = Button(root, text='5', command=lambda: butt_click(5))
b6 = Button(root, text='6', command=lambda: butt_click(6))

b7 = Button(root, text='7', command=lambda: butt_click(7))
b8 = Button(root, text='8', command=lambda: butt_click(8))
b9 = Button(root, text='9', command=lambda: butt_click(9))

bp=Button(root, text=".", bg="#000000", fg="#FFFFFF")
badd=Button(root, text="+", command=lambda:butt_add, bg="#00FFF2")
bsus=Button(root, text="-", command=lambda:butt_sus, bg="#00FFF2")
bmul=Button(root, text="x", command=lambda:butt_mul, bg="#00FFF2")
breslt=Button(root, text="=", bg="#00FFF2",command=lambda:butt_click())
bclr=Button(root, text="Clear", bg="#F52727",command=butt_clr)

display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

b7.grid(row=1, column=0, padx=2, pady=2)
b8.grid(row=1, column=1, padx=2, pady=2)
b9.grid(row=1, column=2, padx=2, pady=2)
badd.grid(row=1, column=3, padx=2, pady=2)

b4.grid(row=2, column=0, padx=2, pady=2)
b5.grid(row=2, column=1, padx=2, pady=2)
b6.grid(row=2, column=2, padx=2, pady=2)
bsus.grid(row=2, column=3, padx=2, pady=2)

b1.grid(row=3, column=0, padx=2, pady=2)
b2.grid(row=3, column=1, padx=2, pady=2)
b3.grid(row=3, column=2, padx=2, pady=2)
bmul.grid(row=3, column=3, padx=2, pady=2)

b0.grid(row=4, column=1, padx=2, pady=2)
bp.grid(row=4, column=0, padx=2, pady=2)
breslt.grid(row=4, column=2, padx=2, pady=2)
bclr.grid(row=4, column=3, padx=2, pady=2)

root.mainloop()

