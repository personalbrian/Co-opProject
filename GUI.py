import tkinter as tk
from tkinter import messagebox, NW, CENTER, BOTH
from Player import Player
from PIL import ImageTk, Image


def instructions(event):
    messagebox.showinfo("Instructions", "There are 2 players needed to play Battleships. Each player\n"
                        + "starts with 5 different ships which are plotted on a 10 x 10 grid\n"
                        + "Once all the ships have been plotted, each player calls coordinates\n"
                        + "to try to hit the opposing player's battleships. If the player\n"
                        + "fails to hit his opponent, then the coordinate will be recorded on the player's map\n"
                        + "If a player was successful and hits a boat, then the screen will print that a\n"
                        + "boat has been hit. If a boat sinks, then the screen will print:\n"
                        + "'You Sunk My Battleship'. Once a player sinks all of the opposing ships\n"
                        + "the game ends and the player that sunk all the ships is the winner.")


def set_up(event):
    start_frame.destroy()
    root.geometry("800x700")
    player_1_frame = tk.Frame(root, width=800, height=700)
    player_1_frame.pack()
    player_1_frame.config(bg="black")
    y_axis_board = tk.Canvas(player_1_frame, width=30, height=285, bg="white")
    y_axis_board.place(x=10, y=390)
    img = Image.open("/Users/brian/Desktop/y-axis.png")
    img = img.resize((35,290), Image.ANTIALIAS)
    y_axis_board.image = ImageTk.PhotoImage(img)
    y_axis_board.create_image(0, 0, image=y_axis_board.image, anchor="nw")
    


root = tk.Tk()
player_1 = Player()
player_2 = Player()
root.title("BATTLESHIPS")
root.geometry("600x500")
start_frame = tk.Frame(root, width=600, height=500)
start_frame.pack()
start_frame.config(background="black")
root.config(background="black")
title_screen = tk.Label(start_frame, text="BATTLESHIPS", font=("Times", 35), fg="green", bg="black")
title_screen.place(x=180, y=60)
instructions_button = tk.Button(start_frame, text="INSTRUCTIONS")
instructions_button.bind("<Button-1>", instructions)
instructions_button.place(x=100, y=400)
instructions_button.config(fg="green")
boat_part_1 = tk.Canvas(start_frame, bg="green", width=400, height=25)
boat_part_1.place(x=100, y=270)
boat_part_2 = tk.Canvas(start_frame, bg="green", width=320, height=15)
boat_part_2.place(x=140, y=299)
boat_part_3 = tk.Canvas(start_frame, bg="green", width=500, height=25)
boat_part_3.place(x=50, y=240)
boat_part_4 = tk.Canvas(start_frame, bg="green", width=200, height=60)
boat_part_4.place(x=205, y=175)
boat_part_5 = tk.Canvas(start_frame, bg="black", width=20, height=30)
boat_part_5.place(x=240, y=190)
boat_part_6 = tk.Canvas(start_frame, bg="black", width=20, height=30)
boat_part_6.place(x=275, y=190)
boat_part_7 = tk.Canvas(start_frame, bg="black", width=20, height=30)
boat_part_7.place(x=310, y=190)
boat_part_7 = tk.Canvas(start_frame, bg="black", width=20, height=30)
boat_part_7.place(x=345, y=190)
start_button = tk.Button(start_frame, text="START")
start_button.bind("<Button-1>", set_up)
start_button.place(x=450, y=400)
start_button.config(fg="green")
root.mainloop()
