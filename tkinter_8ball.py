# MAGIC 8-BALL (25pts)
# Create a tkinter app which acts as a "Magic 8-ball" fortune teller
# The user asks a yes/no question that they want an answer to.
# Then the user clicks a button, and your program displays
# the "magic" random answer to their question.
# Your program will have the following properties:
# - Use an App class to create the tkinter app
# - Add a proper title (appears in the window tab)
# - Add a Label widget at the top to give the user instructions/intro.
# - Add an Entry widget so the user can enter their question.
# - Add a Button widget which will trigger the answer.
# - Add a Label widget to display the answer (set to a initial value of "Your Fortune Here" or "--" or similar)
# - Get your random answer message from a list of at least 10 possible strings. (e.g. ["Yes", "No", "Most Likely", "Definitely", etc...])
# - Add THREE or more other style modifications to make your app unique (font family, font size, color, padding,
# image, borders, justification, whatever you can find in tkinter library etc.)
# Make a comment at the top or bottom of your code to tell me your 3 things you did. (Just to help me out in checking your assignment)

#I changed the font size and color, along with the border on the question.

from tkinter import *
import random
from tkinter import font

class App():
    def __init__(self,master):
        #TITLE
        self.title_font = font.Font(family = "Fixedsys", size = 30, weight = font.BOLD)
        self.title_label = Label(master,text="Magic 8 Ball",fg="sky blue", font = self.title_font)
        self.title_label.grid(column=0, row=0)

        #INSTRUCTIONS
        self.instructions_font = font.Font(family = "Fixedsys", size = 15, weight = font.BOLD)
        self.instructions = Label(master, fg = "dark blue", text = "Below, enter a yes or no question and prepare for infinite wisdom.", font = self.instructions_font)
        self.instructions.grid(column =0,row=1)

        #QUESTION
        self.question = DoubleVar()
        self.question.set("")
        self.question_space = Entry(master, textvariable = self.question, relief = RAISED)
        self.question_space.grid(column=0,row=2)

        #RESULT
        self.result = DoubleVar()
        self.result.set(" ")
        self.result_button = Button(master, text = "Answer me wise Goddess of Everything", command = lambda: self.button_click())
        self.result_button.grid(column=0,row=3)

        self.result_list = ["Try again", "You did NOT just ask me that","Yas queen!", "No way Jose!", "I guess so...", "You never know...", "Truly, seriously", "Always", "Pfft, yeah right", "Anything is possible"]
        self.result_label = Label(master, textvariable = self.result)
        self.result_label.grid(column=0, row = 4)

    def button_click(self):
        self.result.set(self.result_list[random.randrange(len(self.result_list))])


if __name__ == "__main__":
    root = Tk()
    root.title("Magic 8-Ball")
    my_app = App(root)
    root.mainloop()