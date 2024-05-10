## Tkinter 基本使用

参考教学[网站](https://www.pythonguis.com/tutorials), [视频](https://www.youtube.com/watch?v=mop6g-c5HEY)

## 居中显示

```python title="center.py"
from tkinter import *
from tkinter import ttk

window_width = 300
window_height = 150
# create the root window
root = Tk()
root.title("Tkinter MessageBox")
root.resizable(False, False)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))

root.geometry(
    "{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate)
)

# run the app
root.mainloop()

```

## base.py

```python title="base.py"
from tkinter import *
from tkinter import ttk


# 设置主窗口
root = Tk()
# 设置标题
root.title("ToolBox")

# 背景色
# root.configure(background="yellow")
root.minsize(200, 200)
root.maxsize(500, 500)
# 设置宽x高+坐标偏移
root.geometry("300x300+50+50")


root.mainloop()
```

## button.py

```python title="button.py"
from tkinter import *
from tkinter import ttk

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

root = Tk()  # create parent window


def volumeUp():
    """output message to terminal to tell that the button is working"""
    print("Volume Increase +1")


def volumeDown():
    """output message to terminal to tell that the button is working"""
    print("Volume Decrease -1")


# use Button and Label widgets to create a simple TV remote
def turnOnTV():
    """callback method used for turn_on button"""
    # use a Toplevel widget to display an image in a new window
    window = Toplevel(root)
    window.title("TV")
    image = PhotoImage(file=os.path.join(dir_path, "1.jpg"))

    original_image = Label(window, image=image)
    original_image.image = image
    original_image.pack()


turn_on = Button(root, text="ON", command=turnOnTV)
turn_on.pack()

turn_off = Button(root, text="OFF", command=root.quit)
turn_off.pack()

volume = Label(root, text="VOLUME")
volume.pack()

vol_up = Button(root, text="+", command=volumeUp)
vol_up.pack()

vol_down = Button(root, text="-", command=volumeDown)
vol_down.pack()

root.mainloop()
```

## demo.py

```python title="demo.py"
from tkinter import *
from tkinter import ttk


# 按钮点击
def convert():
    output_string.set(entry_int.get() * 1.61)


# 设置主窗口
root = Tk()
# 设置标题
root.title("ToolBox")
# 设置宽x高
root.geometry("300x200")

title_label = ttk.Label(master=root, text="Miles to kilometers", font="Calibri 24 bold")
title_label.pack()

input_frame = ttk.Frame(master=root)

entry_int = IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
entry.pack(side="left", padx=10)

button = ttk.Button(master=input_frame, text="Convert", command=convert)
button.pack(side="left")

input_frame.pack(pady=10)

# 输出
output_string = StringVar()
output_label = ttk.Label(
    master=root, text="Output", font="Calibri 24", textvariable=output_string
)
output_label.pack(pady=5)

# 启动主窗口
root.mainloop()
```

## frame-demo.py

```python title="frame-demo.py"
from tkinter import *
from tkinter import ttk


root = Tk()  # create root window
root.title("Basic GUI Layout")  # title of the GUI window
root.maxsize(900, 600)  # specify the max size the window can expand to
root.config(bg="skyblue")  # specify background color

# Create left and right frames
left_frame = Frame(root, width=200, height=400, bg="grey")
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(root, width=650, height=400, bg="grey")
right_frame.grid(row=0, column=1, padx=10, pady=5)

# Create frames and labels in left_frame
Label(left_frame, text="Original Image").grid(row=0, column=0, padx=5, pady=5)

# load image to be "edited"
image = PhotoImage(file="1.jpg")
original_image = image.subsample(3, 3)  # resize image using subsample
Label(left_frame, image=original_image).grid(row=1, column=0, padx=5, pady=5)

# Display image in right_frame
Label(right_frame, image=image).grid(row=0, column=0, padx=5, pady=5)

# Create tool bar frame
tool_bar = Frame(left_frame, width=180, height=185)
tool_bar.grid(row=2, column=0, padx=5, pady=5)

# Example labels that serve as placeholders for other widgets
Label(tool_bar, text="Tools", relief=RAISED).grid(
    row=0, column=0, padx=5, pady=3, ipadx=10
)  # ipadx is padding inside the Label widget
Label(tool_bar, text="Filters", relief=RAISED).grid(
    row=0, column=1, padx=5, pady=3, ipadx=10
)

# Example labels that could be displayed under the "Tool" menu
Label(tool_bar, text="Select").grid(row=1, column=0, padx=5, pady=5)
Label(tool_bar, text="Crop").grid(row=2, column=0, padx=5, pady=5)
Label(tool_bar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
Label(tool_bar, text="Resize").grid(row=4, column=0, padx=5, pady=5)
Label(tool_bar, text="Exposure").grid(row=5, column=0, padx=5, pady=5)
root.mainloop()
```

## frame-in-frame.py

```python title="frame-in-frame.py"
from tkinter import *
from tkinter import ttk


# 设置主窗口
root = Tk()
# 设置标题
root.title("ToolBox")
root.config(bg="skyblue")

left_frame = ttk.Frame(root, width=200, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)

tool_bar_style = ttk.Style()
tool_bar_style.configure("tool_bar.TFrame", background="purple")
tool_bar = ttk.Frame(left_frame, width=100, height=185, style="tool_bar.TFrame")
tool_bar.grid(row=2, column=0, padx=5, pady=5)


root.mainloop()
```

## frame.py

```python title="frame.py"
from tkinter import *
from tkinter import ttk


# 设置主窗口
root = Tk()
# 设置标题
root.title("ToolBox")
root.config(bg="skyblue")

left_frame = ttk.Frame(root, width=200, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)


root.mainloop()
```

## grid-demo.py

```python title="grid-demo.py"
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Profile Entry using Grid")
root.geometry("500x300")  # set starting size of window
root.maxsize(500, 300)  # width x height
root.config(bg="lightgrey")

# Profile picture
image = PhotoImage(file="1.jpg")
small_img = image.subsample(4, 4)

img = Label(root, image=small_img)
img.grid(row=0, column=0, rowspan=6, padx=5, pady=5)

# Enter specific information for your profile into the following widgets
enter_info = Label(root, text="Please enter your information: ", bg="lightgrey")
enter_info.grid(row=0, column=1, columnspan=4, padx=5, pady=5)

# Name label and entry widgets
Label(root, text="Name", bg="lightgrey").grid(row=1, column=1, padx=5, pady=5, sticky=E)

name = Entry(root, bd=3)
name.grid(row=1, column=2, padx=5, pady=5)

# Gender label and dropdown widgets
gender = Menubutton(root, text="Gender")
gender.grid(row=2, column=2, padx=5, pady=5, sticky=W)
gender.menu = Menu(gender, tearoff=0)
gender["menu"] = gender.menu

# choices in gender dropdown menu
gender.menu.add_cascade(label="Male")
gender.menu.add_cascade(label="Female")
gender.menu.add_cascade(label="Other")
gender.grid()

# Eyecolor label and entry widgets
Label(root, text="Eye Color", bg="lightgrey").grid(
    row=3, column=1, padx=5, pady=5, sticky=E
)
eyes = Entry(root, bd=3)
eyes.grid(row=3, column=2, padx=5, pady=5)

# Height and Weight labels and entry widgets
Label(root, text="Height", bg="lightgrey").grid(
    row=4, column=1, padx=5, pady=5, sticky=E
)
Label(root, text="inches", bg="lightgrey").grid(row=4, column=3, sticky=W)

height = Entry(root, bd=3)
height.grid(row=4, column=2, padx=5, pady=5)

Label(root, text="Weight", bg="lightgrey").grid(
    row=5, column=1, padx=5, pady=5, sticky=E
)
Label(root, text="lbs", bg="lightgrey").grid(row=5, column=3, sticky=W)

weight = Entry(root, bd=3)
weight.grid(row=5, column=2, padx=5, pady=5)

root.mainloop()
```

## grid.py

```python title="grid.py"
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Practice with Grid")
root.geometry("210x180")  # set starting size of window


def display_checked():
    """check if the checkbuttons have been toggled, and display
    a value of '1' if they are checked, '0' if not checked"""
    red = red_var.get()
    yellow = yellow_var.get()
    green = green_var.get()
    blue = blue_var.get()

    print("red: {}\nyellow:{}\ngreen: {}\nblue: {}".format(red, yellow, green, blue))


# Create label
label = Label(root, text="Which colors do you like below?")
label.grid(row=0)

# Create variables and checkbuttons
red_var = IntVar()
Checkbutton(root, width=10, text="red", variable=red_var, bg="red").grid(row=1)

yellow_var = IntVar()
Checkbutton(root, width=10, text="yellow", variable=yellow_var, bg="yellow").grid(row=2)

green_var = IntVar()
Checkbutton(root, width=10, text="green", variable=green_var, bg="green").grid(row=3)

blue_var = IntVar()
Checkbutton(root, width=10, text="blue", variable=blue_var, bg="blue").grid(row=4)

# Create Buttons, one to check which colors are checked,
# and another to close the window.
Button(root, text="Tally", command=display_checked).grid(row=5)
Button(root, text="End", command=root.quit).grid(row=6)

root.mainloop()
```

## login.py

```python title="login.py"
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Login UI using Pack")
root.geometry("400x320")  # set starting size of window
root.maxsize(400, 320)  # width x height
root.config(bg="#6FAFE7")  # set background color of root window

login = Label(root, text="Login", bg="#2176C1", fg="white", relief=RAISED)
login.pack(ipady=5, fill="x")
login.config(font=("Font", 30))  # change font and size of label

# login image
image = PhotoImage(file="1.jpg")
img_resize = image.subsample(5, 5)
Label(root, image=img_resize, bg="white", relief=SUNKEN).pack(pady=5)


def checkInput():
    """check that the username and password match"""
    usernm = "Username301"
    pswrd = "Passw0rd"
    entered_usernm = username_entry.get()  # get username from Entry widget
    entered_pswrd = password_entry.get()  # get password from Entry widget

    if (usernm == entered_usernm) and (pswrd == entered_pswrd):
        print("Hello!")
        root.destroy()

    else:
        print("Login failed: Invalid username or password.")


def toggled():
    """display a message to the terminal every time the check button
    is clicked"""
    print("The check button works.")


# Username Entry
username_frame = Frame(root, bg="#6FAFE7")
username_frame.pack()

Label(username_frame, text="Username", bg="#6FAFE7").pack(side="left", padx=5)

username_entry = Entry(username_frame, bd=3)
username_entry.pack(side="right")

# Password entry
password_frame = Frame(root, bg="#6FAFE7")
password_frame.pack()

Label(password_frame, text="Password", bg="#6FAFE7").pack(side="left", padx=7)

password_entry = Entry(password_frame, bd=3)
password_entry.pack(side="right")

# Create Go! Button

go_button = Button(root, text="GO!", command=checkInput, bg="#6FAFE7", width=15)

go_button.pack(pady=5)

# Remember me and forgot password
bottom_frame = Frame(root, bg="#6FAFE7")
bottom_frame.pack()

var = IntVar()

remember_me = Checkbutton(
    bottom_frame, text="Remember me", bg="#6FAFE7", command=toggled, variable=var
)
remember_me.pack(side="left", padx=19)

# The forgot password Label is just a placeholder, has no function currently
forgot_pswrd = Label(bottom_frame, text="Forgot password?", bg="#6FAFE7")
forgot_pswrd.pack(side="right", padx=19)

root.mainloop()
```

## messageBox.py

```python title="messageBox.py"
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

# create the root window
root = Tk()
root.title("Tkinter MessageBox")
root.resizable(False, False)
root.geometry("300x150")

#
options = {"fill": "both", "padx": 10, "pady": 10, "ipadx": 5}

ttk.Button(
    root,
    text="Show an error message",
    command=lambda: showerror(title="Error", message="This is an error message."),
).pack(**options)

ttk.Button(
    root,
    text="Show an information message",
    command=lambda: showinfo(
        title="Information", message="This is an information message."
    ),
).pack(**options)


ttk.Button(
    root,
    text="Show an warning message",
    command=lambda: showwarning(title="Warning", message="This is a warning message."),
).pack(**options)


# run the app
root.mainloop()
```

