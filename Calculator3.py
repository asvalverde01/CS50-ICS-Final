# CS50 Final Project
# Created by Alberto Valverde

# Program config

from cmath import log
from tkinter import *

import speech_recognition
import pyttsx3

root = Tk()
root.title("Calculator for CS50")
# Gui
# Result Box
info_box = Entry(root, width=9, borderwidth=20,
                 bg="#34495E", justify="right", fg="White")
log_box = Entry(root, width=9, borderwidth=10,
                bg="#34495E", justify="right", fg="White")
resultListen_box = Entry(root, width=9, borderwidth=10,
                         bg="#34495E", justify="right", fg="White")

# Last result
last_result = Entry(root, width=10, borderwidth=8,
                    justify="center", bg="grey", fg="black")

l_result = Label(root, font=('Consolas', '13'), bg="orange",
                 text="LAST RESULT: ").grid(row=5, column=0, columnspan=2)


def fun(number):
    current = info_box.get()
    info_box.delete(0, END)
    info_box.insert(0, str(current) + str(number))
    return


def fun_clear():
    info_box.delete(0, END)
    log_box.delete(0, END)
    return


def operation1():
    first_number = info_box.get()
    global f_num
    global op
    f_num = int(first_number)
    op = "addition"
    info_box.delete(0, END)
    return


def operation2():
    first_number = info_box.get()
    global f_num
    global op
    f_num = int(first_number)
    op = "subtraction"
    info_box.delete(0, END)
    return


def operation3():
    first_number = info_box.get()
    global f_num
    global op
    f_num = int(first_number)
    op = "multiplication"
    info_box.delete(0, END)
    return


def operation4():
    first_number = info_box.get()
    global f_num
    global op
    f_num = int(first_number)
    op = "division"
    info_box.delete(0, END)
    return


def fun_equal():
    second_number = info_box.get()
    info_box.delete(0, END)
    global result

    if op == "addition":
        info_box.insert(0, f_num + int(second_number))
        last_result.delete(0, END)
        result = info_box.get()
        last_result.insert(0, int(result))

    elif op == "subtraction":
        info_box.insert(0, f_num - int(second_number))
        last_result.delete(0, END)
        result = info_box.get()
        last_result.insert(0, int(result))

    elif op == "multiplication":
        info_box.insert(0, f_num * int(second_number))
        last_result.delete(0, END)
        result = info_box.get()
        last_result.insert(0, int(result))

    elif op == "division":
        info_box.insert(0, f_num / int(second_number))
        last_result.delete(0, END)
        result = info_box.get()
        last_result.insert(0, int(result))

    else:
        last_result.insert(str("Syntax error"))
    return


def colorMode(color):
    root.configure(bg=color)
    for button in buttons:
        button.config(bg=color)
    button_clear.configure(bg=color)
    return


def listen():
    recognizer = speech_recognition.Recognizer()
    engine = pyttsx3.init()

    result = ""
    while result != "stop":
        try:
            with speech_recognition.Microphone() as source:
                log_box.insert(0, "Listening...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                engine.say("I am listening...")
                engine.runAndWait()
                audio = recognizer.listen(source)
                if audio is not None:
                    result = recognizer.recognize_google(
                        audio, language="en-in")
                    fun_clear()
                    log_box.insert(0, result)
                    calculateText(result)
                else:
                    log_box.insert(0, "Not listening")
                break
        except Exception as e:
            print(str(e))
    return result


def calculateText(text):
    engine = pyttsx3.init()
    try:
        result = eval(text)
        last_result.delete(0, END)
        resultListen_box.delete(0, END)
        resultListen_box.insert(0, result)
        last_result.insert(0, result)
        info_box.insert(0, result)
        engine.say("The result is: " + str(result))
        engine.runAndWait()
        return result
    except Exception as e:
        engine.say("Error, I only listen to math probems")
        engine.runAndWait()
        print(str(e))
        return "Syntax error"


# Add buttons


button_1 = Button(root, font=('Consolas', '20'), borderwidth=7, text="1", padx=17, pady=10, fg="blue", bg="#808285",
                  command=lambda: fun(1))
button_2 = Button(root, font=('Consolas', '20'), borderwidth=7, text="2", padx=17, pady=10, fg="blue", bg="#808285",
                  command=lambda: fun(2))
button_3 = Button(root, font=('Consolas', '20'), borderwidth=7, text="3", padx=17, pady=10, fg="blue", bg="#808285",
                  command=lambda: fun(3))
button_4 = Button(root, font=('Consolas', '20'), borderwidth=7, text="4", padx=17, pady=10, fg="blue", bg="#808285",
                  command=lambda: fun(4))
button_5 = Button(root, font=('Consolas', '20'), borderwidth=7, text="5", padx=17, pady=10, fg="blue", bg="#808285",
                  command=lambda: fun(5))
button_6 = Button(root, font=('Consolas', '20'), borderwidth=7, text="6", padx=17, pady=10, fg="blue", bg="#808285",
                  command=lambda: fun(6))
button_7 = Button(root, font=('Consolas', '20'), borderwidth=7, text="7", padx=17, pady=10, fg="blue", bg="#808285",
                  command=lambda: fun(7))
button_8 = Button(root, font=('Consolas', '20'), borderwidth=7, text="8", padx=17, pady=10, fg="blue", bg="#808285",
                  command=lambda: fun(8))
button_9 = Button(root, font=('Consolas', '20'), borderwidth=7, text="9", padx=17, pady=10, fg="blue", bg="#808285",
                  command=lambda: fun(9))
button_0 = Button(root, font=('Consolas', '20'), borderwidth=7, text="0", padx=17, pady=10, fg="blue", bg="#808285",
                  command=lambda: fun(0))
# Add buttons to list
buttons = [button_1, button_2, button_3, button_4, button_5,
           button_6, button_7, button_8, button_9, button_0]


button_listen = Button(root, font=('Consolas', '20'), borderwidth=7, text="Listen", padx=17, pady=10, fg="white", bg="#FF0000",
                       command=lambda: listen())


# Operations
button_add = Button(root, font=('Consolas', '20'), borderwidth=10, text="+", padx=20, pady=5, fg="White", bg="#3498DB",
                    command=operation1)
button_sub = Button(root, font=('Consolas', '20'), borderwidth=10, text="-", padx=20, pady=5, fg="White", bg="#3498DB",
                    command=operation2)
button_mul = Button(root, font=('Consolas', '20'), borderwidth=10, text="x", padx=20, pady=5, fg="White", bg="#3498DB",
                    command=operation3)
button_div = Button(root, font=('Consolas', '20'), borderwidth=10, text="/", padx=20, pady=5, fg="White", bg="#3498DB",
                    command=operation4)

button_clear = Button(root, font=('Consolas', '15'), borderwidth=10, text="C", padx=60, pady=15, fg="red", bg="#5F6A6A",
                      command=fun_clear)
button_equal = Button(root, font=('Consolas', '20'), borderwidth=10, text="=", fg="black", bg="#E67E22", padx=15,
                      pady=15,
                      command=fun_equal)

# Extra buttons
button_white = Button(root, font=('Consolas', '15'),
                      borderwidth=2, text="Light mode", comman=lambda: colorMode("white"))
button_black = Button(root, font=('Consolas', '15'), borderwidth=2, text="Dark mode", fg="White", bg="black",
                      command=lambda: colorMode("black"))

# Buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=2)
button_listen.grid(row=0, column=5)

button_add.grid(row=1, column=4)
button_sub.grid(row=2, column=4)
button_mul.grid(row=3, column=4)
button_div.grid(row=4, column=4)

button_clear.grid(row=4, column=0, columnspan=2)
button_equal.grid(row=0, column=4)

button_white.grid(row=6, column=0, columnspan=2)
button_black.grid(row=6, column=2, columnspan=3)

info_box.grid(row=0, column=0, columnspan=3, padx=5, pady=10, ipadx=0, ipady=5)
log_box.grid(row=1, column=5, columnspan=3, padx=5, pady=10, ipadx=0, ipady=5)
resultListen_box.grid(row=2, column=5, columnspan=3,
                      padx=5, pady=10, ipadx=0, ipady=5)

frame_info = LabelFrame(root, text="About the app:", bg="#A41034")

information = Label(frame_info, fg="white", bg="#A41034", text="CS50 2022") \
    .grid(row=6, columnspan=2, )
information1 = Label(frame_info, fg="white", bg="#A41034", text="Calculator created by Sebastian Valverde") \
    .grid(row=7, columnspan=2)

frame_info.grid(row=9, columnspan=5)
info_box.config(font=("Consolas", 30))
log_box.config(font=("Consolas", 20))
resultListen_box.config(font=("Consolas", 20))
last_result.grid(row=5, column=2, columnspan=4)
last_result.config(font=("Consolas", 10))

root.configure(bg="#A41034")
root.resizable(0, 0)
root.mainloop()

# Changelog 1.1
# Window is not resizable anymore
# Gui colors
# Buttons positions
# Button colors

# Changelog 1.2
# Operations Added
# App information Updated
# Quit button Added
# Light mode added
# Dark mode added
# Numbers box justified and size upgraded

# Changelog 1.2
# Size of the buttons has been upgraded
# Last result added
# Changes in the gui
# Quit button Removed

# Changelog 1.3
# Voice recognition added
