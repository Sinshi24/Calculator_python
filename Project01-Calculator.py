from tkinter import * 
root = Tk()

display=Entry(root)
display.get()

b0=Button(root, text="0")
b1=Button(root, text="1")
b2=Button(root, text="2")
b3=Button(root, text="3")
b4=Button(root, text="4")
b5=Button(root, text="5")
b6=Button(root, text="6")
b7=Button(root, text="7")
b8=Button(root, text="8")
b9=Button(root, text="9")
bp=Button(root, text=".")
badd=Button(root, text="+")
bsus=Button(root, text="-")
bmul=Button(root, text="x")
breslt=Button(root, text="=")

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

root.mainloop()
