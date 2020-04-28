from tkinter import *
import language_check

#run spell check
def run():
	text = namestr.get()
	tool1 = language_check.LanguageTool('en-US')
	matches1 = tool1.check(text)
	len(matches1)
	for i in range(len(matches1)):
		#get output in window instead of terminal
		new_text = Label(screen , text = matches1[i] , fg = "yellow" , bg = "black")
		new_text.pack()
		
		
screen = Tk()
screen.title("Spell Checker Wizard")
screen.configure(bg = "black")
screen.geometry("666x666")

#Display Intro Text
welcome_text = Label(screen , text = "Coded by : Who Killed DB ?" , font = ("Courier",24) ,fg = "white" , bg = "black")
welcome_text.pack()

#Getting String From User
namestr=StringVar()
name = Entry( textvariable = namestr )

#Creating Button
click_me = Button (text = "Run Check" , fg = "black" , bg = "green" , command = run )

name.pack()
click_me.pack()


screen.mainloop()
