# Universal Gravity Calculator (30pts)
# In physics, the force of gravity between two objects
# can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters

# Make a tkinter app with the following attributes:
# - use an App class
# - Add a title.
# - Make a label and entry widget for m1, m2, and r
# - Make a "Calculate" button widget to trigger a lambda function
# - Add a calculate label widget to display the answer
# - Make exceptions for division by zero and type conversion errors.
# - When "Calculate" is pushed, the result is displayed.  Yay!
# - Add an exception for the possible entry of zero radius (ZeroDivisionError Exception)
# - Make your app unique by changing 3 or more DIFFERENT style attributes or kwargs for your app.  Perhaps consider: fonts, color, padding, widths, etc).  Put a comment in your code to tell me what you changed. If you change the font for all the widgets, that is ONE thing.  If you add padx to all your app widgets, that is ONE thing.  If you change the color of all your blocks, that is ONE thing.

from tkinter import *
from tkinter import font

class Gravity():
    def __init__(self,master):
        #VARIABLES
        self.m1 = DoubleVar()
        self.m2 = DoubleVar()
        self.x = DoubleVar()
        self.calculate = DoubleVar()

        #TITLE
        self.title_font = font.Font(family = "Courier New", size = 20, weight = font.BOLD)
        self.title = Label(master, text = "Universal Gravity Calculator", fg = "blueviolet",font = self.title_font)
        self.title.grid(column=0, row =0)

        #ENTRY LABELS/WIDGETS
        self.entry_font = font.Font(family = "Courier New", size = 13, weight = font.BOLD)
        self.m1_label = Label(master, text = "First Object Mass (kg)", fg = "dark blue", relief = FLAT, font = self.entry_font)
        self.m1_label.grid(column=0,row=1)
        self.m1_entry = Entry(master, textvariable = self.m1)
        self.m1_entry.grid(column = 0, row = 2)

        self.m2_label = Label(master, text = "Second Object Mass (kg)", fg = "dark blue", relief = FLAT, font = self.entry_font)
        self.m2_label.grid(column=0,row=3)
        self.m2_entry = Entry(master, textvariable = self.m2)
        self.m2_entry.grid(column = 0, row =4)

        self.x_label = Label(master, text = "Distance (m)", fg = "dark blue", relief = FLAT, font = self.entry_font)
        self.x_label.grid(column=0,row=5)
        self.x_entry = Entry(master, textvariable = self.x)
        self.x_entry.grid(column = 0, row = 6)

        #CALCULATE
        self.calculate_button = Button(master, text = "Calculate Force (N)", command = lambda: self.button_click(master))
        self.calculate_button.grid(column = 0, row = 7)

    def button_click(self,master):
        try:
            self.calculate.set((6.67 * (10 ** -11)) * (self.m1.get() * self.m2.get())/ (self.x.get() ** 2))
            self.calculate_font = font.Font(family="Courier New", size = 40, weight=font.BOLD)
            self.calculate_label = Label(master, textvariable=self.calculate, fg="dark blue", bg="sky blue",
                                         font=self.calculate_font, relief=RAISED)
            self.calculate_label.grid(column=0, row=8)
        except:
            x = 0


if __name__ == "__main__":
    root = Tk()
    root.title("Gravity Calculator")
    my_app = Gravity(root)
    root.mainloop()