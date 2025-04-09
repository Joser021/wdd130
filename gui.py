from math import pi
import tkinter as tk
from tkinter import Frame, Label, Button

def main():
    root = tk.Tk()

    root.title("Area of a Circle")
    root_text = Label(root, text="Find the area of a Circle")
    root_text.grid(column=0, row=0)

    root_text = Label(root, text="Insert the radius")
    root_text.grid(column=0, row=1)

    root_button = Button(root, text="Calculate", command=calculate_circle_area)
    root_button.grid(column=0, row=2)

    area = Label(root, text="Area: ")
    area.grid(column=0, row=3)

    calculate_circle_area(area)
    root.mainloop()




def calculate_circle_area(area):
    area_circle = pi * 5 ** 2

    text = f"{area_circle:.2f}"

    area["text"] = text









if __name__ == "__main__":
    main()
