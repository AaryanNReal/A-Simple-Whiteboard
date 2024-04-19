import tkinter as tk
from tkinter import *
import random


def play_game(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result = ""
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
            (player_choice == "Paper" and computer_choice == "Rock") or \
            (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    label34.config(text=result)


def create_widgets(root):
    title_frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
    title_frame.pack(fill=tk.BOTH)

    buttons_frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
    buttons_frame.pack()

    title_label = tk.Label(title_frame, text="Rock Paper Scissors Game", font=("Helvetica", 20), bg="#f0f0f0")
    title_label.pack()

    rock_button = tk.Button(buttons_frame, text="Rock", font=("Arial", 14), width=10, command=lambda: play_game("Rock"))
    rock_button.grid(row=0, column=0, padx=5, pady=5)

    paper_button = tk.Button(buttons_frame, text="Paper", font=("Arial", 14), width=10,
                             command=lambda: play_game("Paper"))
    paper_button.grid(row=0, column=1, padx=5, pady=5)

    scissors_button = tk.Button(buttons_frame, text="Scissors", font=("Arial", 14), width=10,
                                command=lambda: play_game("Scissors"))
    scissors_button.grid(row=0, column=2, padx=5, pady=5)

    global label34
    label34 = Label(root, text="")
    label34.pack()


def main():
    root = tk.Tk()
    root.title("Rock Paper Scissors Game")
    root.configure(bg="#f0f0f0")

    create_widgets(root)
    root.mainloop()


main()
