import tkinter as tk

# Logical code
firstNum = ""
secondNum = ""
operator = ""
equation = ""
equalClicked = False

def setText(textbox, text):
    textbox.config(state='normal')
    textbox.delete(1.0, tk.END)
    textbox.insert(tk.END, text)

def onClearBtnClicked(textbox):
    global firstNum, secondNum, operator, equalClicked, equation
    firstNum = ""
    secondNum = ""
    operator = ""
    equation = ""
    equalClicked = False
    setText(textbox, equation)

def numBtnClicked(num, textbox):
    global firstNum, secondNum, operator, equalClicked
    if equalClicked:
        onClearBtnClicked(textbox)
        firstNum += num
        equation = firstNum
    elif operator == "":
        firstNum += num
        equation = firstNum
    else:
        secondNum += num
        equation = firstNum + " " + operator + " " + secondNum
    setText(textbox, equation)

def operatorBtnClicked(op, textbox):
    global firstNum, secondNum, operator, equalClicked
    if firstNum != "":
        operator = op
        equation = firstNum + " " + operator
        setText(textbox, equation)

def equalBtnClicked(textbox):
    global firstNum, secondNum, operator, equalClicked, equation
    if firstNum != "" and secondNum != "" and operator != "":
        if operator == "+":
            equation = firstNum + " + " + secondNum + " = " + str(float(firstNum) + float(secondNum))
        elif operator == "-":
            equation = firstNum + " - " + secondNum + " = " + str(float(firstNum) - float(secondNum))
        elif operator == "*":
            equation = firstNum + " * " + secondNum + " = " + str(float(firstNum) * float(secondNum))
        elif operator == "/":
            if secondNum == "0":
                equation = "ERROR: Cannot divide by 0"
            else:
                equation = firstNum + " / " + secondNum + " = " + str(float(firstNum) / float(secondNum))
        print(equation)
        setText(textbox, equation)
        equalClicked = True

# UI code
root = tk.Tk()
root.configure(background='light blue')

root.geometry("800x500")
root.title("Calculator")

label = tk.Label(root, text= "Calculator", font=('Arial', 22, 'bold'), bg='light blue')
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=1, font=('Arial', 40, 'bold'), state='disabled')
textbox.pack(padx=30, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.configure(background='light blue')

btn1 = tk.Button(buttonframe, text="1", command=lambda : numBtnClicked("1", textbox),  font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", command=lambda : numBtnClicked("2", textbox), font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", command=lambda : numBtnClicked("3", textbox), font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", command=lambda : numBtnClicked("4", textbox), font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", command=lambda : numBtnClicked("5", textbox), font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", command=lambda : numBtnClicked("6", textbox), font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btn7 = tk.Button(buttonframe, text="7", command=lambda : numBtnClicked("7", textbox), font=('Arial', 18))
btn7.grid(row=2, column=0, sticky=tk.W+tk.E)

btn8 = tk.Button(buttonframe, text="8", command=lambda : numBtnClicked("8", textbox), font=('Arial', 18))
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)

btn9 = tk.Button(buttonframe, text="9", command=lambda : numBtnClicked("9", textbox), font=('Arial', 18))
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)

btn0 = tk.Button(buttonframe, text="0", command=lambda : numBtnClicked("0", textbox), font=('Arial', 18))
btn0.grid(row=3, column=1, sticky=tk.W+tk.E)


buttonframe.pack(fill='x', padx=30, pady=10)

buttonframe2 = tk.Frame(root)
buttonframe2.columnconfigure(0, weight=1)
buttonframe2.columnconfigure(1, weight=1)
buttonframe2.columnconfigure(2, weight=1)
buttonframe2.columnconfigure(3, weight=1)
buttonframe2.configure(background='light blue')

btn_plus = tk.Button(buttonframe2, text="+", command=lambda : operatorBtnClicked("+", textbox), font=('Arial', 18))
btn_plus.grid(row=0, column=0, padx=15, sticky=tk.W+tk.E)

btn_minus = tk.Button(buttonframe2, text="-", command=lambda : operatorBtnClicked("-", textbox), font=('Arial', 18))
btn_minus.grid(row=0, column=1, padx=15, sticky=tk.W+tk.E)

btn_multiply = tk.Button(buttonframe2, text="*", command=lambda : operatorBtnClicked("*", textbox), font=('Arial', 18))
btn_multiply.grid(row=0, column=2, padx=15, sticky=tk.W+tk.E)

btn_divide = tk.Button(buttonframe2, text="/", command=lambda : operatorBtnClicked("/", textbox), font=('Arial', 18))
btn_divide.grid(row=0, column=3, padx=15, sticky=tk.W+tk.E)

btn_equal = tk.Button(buttonframe2, text="=", command=lambda : equalBtnClicked(textbox), font=('Arial', 18))
btn_equal.grid(row=1, column=1, padx=15, pady=10, sticky=tk.W+tk.E)

btn_clear = tk.Button(buttonframe2, text="CE", command=lambda : onClearBtnClicked(textbox), font=('Arial', 18))
btn_clear.grid(row=1, column=2, padx=15, pady=10, sticky=tk.W+tk.E)

buttonframe2.pack(fill='x', padx=30, pady=10)

root.mainloop()
