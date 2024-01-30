import tkinter as tk

# Logical code
p1Text = "Welcome to page1"
p2Text = "Welcome to page2"
page = 1

def changePage(root, page1Frame, page2Frame):
    global page
    if page == 1:
        page = 2
        root.title("Page 2")
        page1Frame.pack_forget()
        page2Frame.pack(fill='both', expand=True)
    elif page == 2:
        page = 1
        root.title("Page 1")
        page2Frame.pack_forget()
        page1Frame.pack(fill='both', expand=True)

def onEnter(button):
    global page
    if page == 1:
        button.config(background='light blue')
    elif page == 2:
        button.config(background='red')

def onLeave(button):
    global page
    if page == 1:
        button.config(background='red')
    elif page == 2:
        button.config(background='light blue')

# UI code
root = tk.Tk()
root.geometry("800x500")
root.title("Page 1")

page1Frame = tk.Frame(root, bg='light blue')
page2Frame = tk.Frame(root, bg='red')

# Page 1 Frame
text1 = tk.Label(page1Frame, text=p1Text, bg='light blue', font=('Arial', 22, 'bold'))
text1.pack(fill='both', expand=True)
button1 = tk.Button(page1Frame, text="Change Page", command=lambda: changePage(root, page1Frame, page2Frame), bg='red', font=('Arial', 18))
button1.pack(padx=20, pady=20, fill='both', expand=True)
page1Frame.pack(fill='both', expand=True)

# Page 2 Frame
text2 = tk.Label(page2Frame, text=p2Text, bg='red', font=('Arial', 22, 'bold'))
text2.pack(fill='both', expand=True)
button2 = tk.Button(page2Frame, text="Change Page", command=lambda: changePage(root, page1Frame, page2Frame), bg='light blue', font=('Arial', 18))
button2.pack(padx=20, pady=20, fill='both', expand=True)

button1.bind("<Enter>", lambda event: onEnter(button1))
button1.bind("<Leave>", lambda event: onLeave(button1))

button2.bind("<Enter>", lambda event: onEnter(button2))
button2.bind("<Leave>", lambda event: onLeave(button2))

root.mainloop()
