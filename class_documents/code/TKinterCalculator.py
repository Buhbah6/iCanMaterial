import tkinter as tk

# Logic Code


# UI Code
root = tk.Tk()

root.geometry("800x500")
root.title("Aesthetic Calculator")
root.configure(bg="light blue")

label = tk.Label(root, text= "Calculator", font=('Arial', 22, 'bold'), bg="light blue")
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=1, font=('Arial', 40, 'bold'), state='disabled')
textbox.pack(padx=30, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.configure(bg="light blue")

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btn7 = tk.Button(buttonframe, text="7", font=('Arial', 18))
btn7.grid(row=2, column=0, sticky=tk.W+tk.E)

btn8 = tk.Button(buttonframe, text="8", font=('Arial', 18))
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)

btn9 = tk.Button(buttonframe, text="9", font=('Arial', 18))
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)

btn0 = tk.Button(buttonframe, text="0", font=('Arial', 18))
btn0.grid(row=3, column=1, sticky=tk.W+tk.E)

buttonframe.pack(fill='x', padx=30, pady=10)

buttonframe2 = tk.Frame(root)
buttonframe2.columnconfigure(0, weight=1)
buttonframe2.columnconfigure(1, weight=1)
buttonframe2.columnconfigure(2, weight=1)
buttonframe2.columnconfigure(3, weight=1)
buttonframe2.configure(bg="light blue")

btn_plus = tk.Button(buttonframe2, text="+", font=('Arial', 18))
btn_plus.grid(row=0, column=0, padx=15, sticky=tk.W+tk.E)

btn_minus = tk.Button(buttonframe2, text="-", font=('Arial', 18))
btn_minus.grid(row=0, column=1, padx=15, sticky=tk.W+tk.E)

btn_multiply = tk.Button(buttonframe2, text="*", font=('Arial', 18))
btn_multiply.grid(row=0, column=2, padx=15, sticky=tk.W+tk.E)

btn_divide = tk.Button(buttonframe2, text="/", font=('Arial', 18))
btn_divide.grid(row=0, column=3, padx=15, sticky=tk.W+tk.E)

btn_equal = tk.Button(buttonframe2, text="=", font=('Arial', 18))
btn_equal.grid(row=1, column=1, padx=15, sticky=tk.W+tk.E)

btn_clear = tk.Button(buttonframe2, text="CE", font=('Arial', 18))
btn_clear.grid(row=1, column=2, padx=15, sticky=tk.W+tk.E)

buttonframe2.pack(fill='x', padx=30, pady=10)

root.mainloop()
