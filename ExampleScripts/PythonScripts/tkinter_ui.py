import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import font
from tkinter import filedialog
from tkinter import commondialog
from tkinter import colorchooser
from tkinter import tix
import turtle
import time
import datetime
import random

# This program depends on certain modules and images that need to be accessible by the python interpreter and program for the program to run properly

time_var = datetime.datetime.now()
time_var_str = str(time_var.year)
time_var_str_2 = str(time_var.month)
time_var_str_3 = str(time_var.day)

time_var_str_4 = str(time_var.hour)
time_var_str_5 = str(time_var.minute)

Launcher = Tk()


Launcher.title('Basic Program Launcher')
Launcher.geometry('1099x652')

# padding tells tkinter how many Pixels the content is from the window's edge

Points = 0

frm = ttk.Frame(Launcher, padding=140)
frm.grid()

Launcher.configure(bg='blue')

style = ttk.Style(Launcher)

variable1 = style.theme_names()

style.theme_use('winnative')
global style_1
style_1 = 'winnative'

def default():
    global style_1
    if style_1 == 'winnative':
        style.theme_use('default')
        style_1 = 'default'
    else:
        style.theme_use('winnative')
        style_1 = 'winnative'


ttk.Button(frm, text="Change The Theme", command=default).grid(column=0, row=10)


logo2 = tkinter.PhotoImage(file='Basic_Logo.png')
window_Logo = tkinter.PhotoImage(file='start_button.png')
Launcher.iconphoto(False, window_Logo)

ttk.Label(frm, image=logo2, text="Basic Program", foreground="blue", font=("Helvetica", 60)).grid(column=0, row=0)

ttk.Label(frm, text="   ").grid(column=0, row=1)

ttk.Label(frm, text="   ").grid(column=0, row=2)

Start_Button = tkinter.PhotoImage(file='run_logo.png')

Main_Button = ttk.Button(frm, text="Start Main Program", image=Start_Button, command=Launcher.destroy, width=30).grid(
    column=0, row=1)

ttk.Label(frm, text="Made by Abdullojon Pardakulov", font=("Courier New", 15)).grid(column=0, row=9)

ttk.Label(frm, font=("Ubuntu", 12),
          text="It is currently " + time_var_str_2 + "-" + time_var_str_3 + "-" + time_var_str + " " + time_var_str_4 + ":" + time_var_str_5).grid(
    column=0, row=6)

logo = tkinter.PhotoImage(file='Python-Symbol.png')

ttk.Label(frm, image=logo).grid(column=2, row=9)

Launcher.mainloop()

print(variable1)

time.sleep(0.1)

Menu = Tk()

window_Logo = tkinter.PhotoImage(file='start_button.png')
Menu.iconphoto(False, window_Logo)

q1 = 0
q2 = 0
q3 = 0
q4 = 0
def OpenQuizWindow():

    Points = 0

    def q1_choice1():
        global q1
        q1 = 1

    def q1_choice2():
         global q1
         q1 = 2

    def q1_choice3():
        global q1
        q1 = 3

    def q1_choice4():
        global q1
        q1 = 4

    def q2_choice1():
        global q2
        q2 = 1

    def q2_choice2():
        global q2
        q2 = 2

    def q2_choice3():
        global q2
        q2 = 3

    def q2_choice4():
        global q2
        q2 = 4

    def q3_choice1():
        global q3
        q3 = 1

    def q3_choice2():
        global q3
        q3 = 2

    def q3_choice3():
        global q3
        q3 = 3

    def q3_choice4():
        global q3
        q3 = 4

    def q4_choice1():
        global q4
        q4 = 1

    def q4_choice2():
        global q4
        q4 = 2

    def q4_choice3():
        global q4
        q4 = 3

    def q4_choice4():
        global q4
        q4 = 4


    Correct_Answers = [2, 1, 3, 4]
    QuizWindow = Toplevel(Menu)

    QuizWindow.title("Quiz")

    QuizWindow.geometry("630x750")

    Label(QuizWindow, text="Quiz:", font=("Arial", 20)).place(x=275, y=0)

    Label(QuizWindow, text="Question #1:", font=("Arial", 15)).place(x=30, y=30)
    Label(QuizWindow, text="Question #2:", font=("Arial", 15)).place(x=30, y=190)
    Label(QuizWindow, text="Question #3:", font=("Arial", 15)).place(x=30, y=350)
    Label(QuizWindow, text="Question #4:", font=("Arial", 15)).place(x=30, y=510)

    window_Logo = tkinter.PhotoImage(file='start_button.png')
    QuizWindow.iconphoto(False, window_Logo)
    global Points_str2

    def Submit():
        print(q1)
        global Points
        global Points_str
        global Points_str2
       
        Points = 0
        if q1 == 2:
            Points = Points + 1
        if q2 == 1:
            Points = Points + 1
        if q3 == 3:
            Points = Points + 1
        if q4 == 4:
            Points = Points + 1

        Points_str = str(Points)
        Points_str2 = str(Points*25)
        Label(QuizWindow, font=("Arial", 20), text= "You have earned " + Points_str + " out of 4 points.").place(x=10, y=680)
        Label(QuizWindow, font=("Arial", 20), fg="Green", text= Points_str2 + "%").place(x=525, y=0)


    question1 = Label(QuizWindow, text="What is the boiling point of water in Celsius?").place(x=30, y=63)
    question2 = Label(QuizWindow, text="What is 3^3?").place(x=30, y=225)
    question3 = Label(QuizWindow, text="What is the longest word in this list?").place(x=30, y=385)
    question4 = Label(QuizWindow, text="How many questions are on this Quiz?").place(x=30, y=540)

    Label(QuizWindow, text="1: 76 C").place(x=30, y=88)
    ttk.Button(QuizWindow, command=q1_choice1, text="Choice 1").place(x=80, y=88)

    Label(QuizWindow, text="2: 100 C").place(x=30, y=113)
    ttk.Button(QuizWindow, command=q1_choice2, text="Choice 2").place(x=80, y=113)

    Label(QuizWindow, text="3: 0 C").place(x=30, y=138)
    ttk.Button(QuizWindow, command=q1_choice3, text="Choice 3").place(x=80, y=138)

    Label(QuizWindow, text="4: 98.6 C").place(x=30, y=163)
    ttk.Button(QuizWindow, command=q1_choice4, text="Choice 4").place(x=80, y=163)

    Label(QuizWindow, text="1: 27").place(x=30, y=250)
    ttk.Button(QuizWindow, command=q2_choice1, text="Choice 1").place(x=80, y=250)

    Label(QuizWindow, text="2: 9 ").place(x=30, y=275)
    ttk.Button(QuizWindow, command=q2_choice2, text="Choice 2").place(x=80, y=275)

    Label(QuizWindow, text="3: 6 ").place(x=30, y=300)
    ttk.Button(QuizWindow, command=q2_choice3, text="Choice 3").place(x=80, y=300)

    Label(QuizWindow, text="4: 30").place(x=30, y=325)
    ttk.Button(QuizWindow, command=q2_choice4, text="Choice 4").place(x=80, y=325)

    Label(QuizWindow, text="1: Hello").place(x=30, y=410)
    ttk.Button(QuizWindow, command=q3_choice1, text="Choice 1").place(x=80, y=410)

    Label(QuizWindow, text="2: Chips").place(x=30, y=435)
    ttk.Button(QuizWindow, command=q3_choice2, text="Choice 2").place(x=80, y=435)

    Label(QuizWindow, text="3: Programming").place(x=30, y=460)
    ttk.Button(QuizWindow, command=q3_choice3, text="Choice 3").place(x=120, y=460)

    Label(QuizWindow, text="4: If").place(x=30, y=485)
    ttk.Button(QuizWindow, command=q3_choice4, text="Choice 4").place(x=80, y=485)

    Label(QuizWindow, text="1: 1 ").place(x=30, y=565)
    ttk.Button(QuizWindow, command=q4_choice1, text="Choice 1").place(x=80, y=565)

    Label(QuizWindow, text="2: 2").place(x=30, y=590)
    ttk.Button(QuizWindow, command=q4_choice2, text="Choice 2").place(x=80, y=590)

    Label(QuizWindow, text="3: 3").place(x=30, y=615)
    ttk.Button(QuizWindow, command=q4_choice3, text="Choice 3").place(x=80, y=615)

    Label(QuizWindow, text="4: 4").place(x=30, y=640)
    ttk.Button(QuizWindow, command=q4_choice4, text="Choice 4").place(x=80, y=640)

    Button(QuizWindow, text="Submit Quiz?", font=("Arial", 13), fg="green", bg="black", command=Submit).place(
        x=486, y=680)


def OpenClickerWindow():
    ClickerWindow = Toplevel(Menu)

    ClickerWindow.title("Clicker Game")

    ClickerWindow.geometry("1140x640")
    global clicker_score
    global clicker_rate
    global clicker_sleep
    global clicker_sleep_str
    global clicker_rate_str
    clicker_score = 0
    clicker_rate = 1
    clicker_sleep = 2
    clicker_rate_str = ("1")
    clicker_sleep_str = ("2")

    Label(ClickerWindow, font=("arial", 17), fg="blue",
          text="There is a " + clicker_sleep_str + " second cooldown per click.").place(
        x=340, y=430)
    Label(ClickerWindow, font=("arial", 17), fg="green",
          text="You get " + clicker_rate_str + " points per click.").place(
        x=340, y=390)

    def click():
        global clicker_score
        clicker_score = clicker_score + clicker_rate
        print(clicker_score)
        clicker_score_str = str(clicker_score)
        Label(ClickerWindow, font=("arial", 20), fg="red", text="Your current score is " + clicker_score_str + ".").place(x=340, y=350)
        Label(ClickerWindow, font=("arial", 10), fg="purple", text="Poggers").place(x=random.uniform(0, 1050), y=random.uniform(0, 550))
        time.sleep(clicker_sleep)

    def click2():
        global clicker_rate
        global clicker_score
        global clicker_sleep
        global clicker_rate_str
        if clicker_score > 2:
            clicker_score = clicker_score - 3 - clicker_score*0.05

            clicker_rate = clicker_rate*1.05
            clicker_rate_str=str(clicker_rate)
            clicker_score_str=str(clicker_score)
            Label(ClickerWindow, font=("arial", 17), fg="green", text="You get " + clicker_rate_str + " points per click.").place(
                x=340, y=390)
            Label(ClickerWindow, font=("arial", 20), fg="red",
                  text="Your current score is " + clicker_score_str + ".").place(x=340, y=350)
            time.sleep(clicker_sleep)
        print(clicker_rate)

    def click3():
        global clicker_sleep
        global clicker_score
        global clicker_rate
        global clicker_sleep_str
        if clicker_score > 2:
            clicker_score = clicker_score - 3
            clicker_sleep = clicker_sleep/1.5
            clicker_sleep_str=str(clicker_sleep)
            clicker_score_str=str(clicker_score)
            Label(ClickerWindow, font=("arial", 17), fg="blue",
                  text="There is a " + clicker_sleep_str + " second cooldown per click.").place(
                x=340, y=430)
            Label(ClickerWindow, font=("arial", 20), fg="red",
                  text="Your current score is " + clicker_score_str + ".").place(x=340, y=350)
            time.sleep(clicker_sleep)

        print (clicker_sleep)

    Label(ClickerWindow, text="Clicker Game", font=("Arial", 30)).place(x=10, y=0)

    Clicker_Button = Button(ClickerWindow, command=click,text="Click Me!", font=("Arial", 40), fg="red").place(x=300, y=210)

    Clicker_Button2 = Button(ClickerWindow, command=click2, text="Rate of Score increase - Worth 3 or more points", font=("Arial", 10), fg="blue").place(x=660, y=220)

    Clicker_Button3 = Button(ClickerWindow, command=click3, text="Rate of Cooldown decrease - Worth 3 points", font=("Arial", 10), fg="green").place(x=660, y=260)

def OpenFactWindow():
    FactWindow = Toplevel(Menu)
    FactWindow.configure(bg='Black')
    FactWindow.title("Fact Calculator")
    FactWindow.geometry("1150x650")
    logo = tkinter.PhotoImage(file='cat.png')
    fact_logo = Label(FactWindow, text="Peng", font=("Arial", 30), fg="white", bg='black').place(x=15, y=0)
    


def OpenSettingsWindow():
    SettingsWindow = Toplevel(Menu)

    SettingsWindow.title("Condition of Program")

    SettingsWindow.geometry("460x460")

    Label(SettingsWindow, text="Condition of Program").place(x=140, y=0)

    Label(SettingsWindow, text="Background Color of Menu: Black").place(x=10, y=30)
    Label(SettingsWindow, text="Current State of Program: Currently Running").place(x=10, y=50)
    Label(SettingsWindow, text="Sub_Application Currently Selected: Settings ").place(x=10, y=70)
    Label(SettingsWindow, text="Available Options:").place(x=10, y=90)
    Label(SettingsWindow, text="- Quiz").place(x=10, y=110)
    Label(SettingsWindow, text="- Clicker").place(x=10, y=130)
    Label(SettingsWindow, text="- Fact Calculator (Work in Progress)").place(x=10, y=150)

def OpenAboutWindow():
    AboutWindow = Toplevel(Menu)

    AboutWindow.title("About Program")

    AboutWindow.geometry("720x240")

    Label(AboutWindow, text="About Program:", font=("Times", 15)).place(x=7, y=0)

    About_Program = Label(AboutWindow,
                          text="REDACTED").place(
        x=10, y=30)
    About_Program2 = Label(AboutWindow,
                           text="There are three options to choose from, a quiz, a clicker game, and a fact calculator.").place(
        x=10, y=50)
    About_Program3 = Label(AboutWindow,
                           text="REDACTED").place(
        x=10, y=70)
    About_Program4 = Label(AboutWindow, text="Made by Abdullojon Pardakulov").place(x=415, y=180)


Menu.title('Basic Program Menu!')

Menu.configure(bg='black')

style.theme_use('default')

Menu.geometry('1320x760')

button1 = tkinter.PhotoImage(file='settings.png')
Settings_Button = ttk.Button(Menu, text="Settings", image=button1, command=OpenSettingsWindow).place(x=1200, y=650)

Menu_Logo_image = tkinter.PhotoImage(file='Menu_logo.png')
Menu_Logo = Label(Menu, text="Pick one of the following below:", image=Menu_Logo_image, bg="Black").place(x=400, y=0)

Question_Logo = tkinter.PhotoImage(file='question.png')
About = ttk.Button(Menu, text="About", image=Question_Logo, command=OpenAboutWindow).place(x=1125, y=650)

Option1 = tkinter.PhotoImage(file='Option1.png')
Option2 = tkinter.PhotoImage(file='Option2.png')
Option3 = tkinter.PhotoImage(file='Option3.png')

o1l = Label(Menu, text='option1', image=Option1, bg="Black").place(x=200, y=200)
o2l = Label(Menu, text='option2', image=Option2, bg="Black").place(x=200, y=350)
o3l = Label(Menu, text='option3', image=Option3, bg="Black").place(x=200, y=500)

quiz_logo = tkinter.PhotoImage(file='quiz.png')
optionbutton1 = ttk.Button(Menu, text='Quiz', image=quiz_logo, command=OpenQuizWindow).place(x=510, y=210)

clicker_logo = tkinter.PhotoImage(file='clicker.png')
optionbutton2 = ttk.Button(Menu, text='clicker', image=clicker_logo, command=OpenClickerWindow).place(x=510, y=360)

fact_cal_logo = tkinter.PhotoImage(file='fact_cat.png')
optionbutton3 = ttk.Button(Menu, text='fact_cal.', image=fact_cal_logo, command=OpenFactWindow).place(x=510, y=510)

Menu.mainloop()
