import tkinter as tk
import random

# initialise global variables
list_order = []


# functions
def play_game():
    """Main game logic."""
    global list_order
    lost = False

    buttons = [red_button, blue_button, yellow_button, green_button]
    disable_buttons()

    # while not lost:
    #     list_order.append(random.choice(buttons))
    #     flash_buttons()
    list_order.append(green_button)
    flash_buttons()


def flash_buttons():
    """Flash all buttons in the list order"""
    global red_button
    global yellow_button
    global blue_button
    global green_button

    global list_order

    for button in list_order:
        if button == green_button:
            button.config(bg="green")
            root.after(1000, button.config(bg="dark green"))
        if button == yellow_button:
            button.config(bg="yellow")
            root.after(1, button.config(bg="#ab9208"))
        if button == red_button:
            button.config(bg="red")
            root.after(1, button.config(bg="dark red"))
        if button == blue_button:
            button.config(bg="blue")
            root.after(1, button.config(bg="dark blue"))


def disable_buttons():
    """Disable all buttons and change their colours to a darker shade."""
    global red_button
    global yellow_button
    global blue_button
    global green_button

    green_button.config(state=tk.DISABLED, bg="dark green")
    red_button.config(state=tk.DISABLED, bg="dark red")
    blue_button.config(state=tk.DISABLED, bg="dark blue")
    yellow_button.config(state=tk.DISABLED, bg="#ab9208")


def show_button_order():
    global list_order
    for button in list_order:
        if button.bg == "dark green":
            print("dark green")


root = tk.Tk()
root.title("Simon")
root.iconbitmap("brain.ico")
root.geometry("600x600")
root.config(bg="#c05746")
root.resizable(0, 0)

title_frame = tk.Frame(root)
title_frame.pack()
game_frame = tk.Frame(root, bg="#adc698")
game_frame.pack(pady=20)
score_frame = tk.Frame(root, bg="#adc698")
score_frame.pack()

title = tk.Label(title_frame, text="Simon", font=("Rubrik", 40), bg="#c05746")
title.pack()

# create game buttons
red_button = tk.Button(game_frame, bg="red", font=("Rubrik", 50), text="", width=4)
red_button.grid(row=0, column=0, padx=20, pady=20)
blue_button = tk.Button(game_frame, bg="blue", font=("Rubrik", 50), text="", width=4)
blue_button.grid(row=1, column=0, padx=20, pady=20)
yellow_button = tk.Button(game_frame, bg="yellow", font=("Rubrik", 50), text="", width=4)
yellow_button.grid(row=0, column=1, padx=20, pady=20)
green_button = tk.Button(game_frame, bg="green", font=("Rubrik", 50), text="", width=4)
green_button.grid(row=1, column=1, padx=20, pady=20)

play_button = tk.Button(score_frame, text="Play!", font=("Rubrik", 25), bg="green", command=play_game)
play_button.grid(row=0, column=0)

score_label = tk.Label(score_frame, text="Score:   ", font=("Rubrik", 25), bg="#adc698")
score_label.grid(row=0, column=1, padx=20)

root.mainloop()
