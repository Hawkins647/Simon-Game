import tkinter as tk
import random

# initialise global variables
game_order = []
player_order = []
time_delay = 500


# functions
def play_game():
    """Play the game!"""
    disable_buttons()
    change_label("Playing!")
    pick_sequence()


def pick_sequence():
    """Pick a sequence to begin the game with"""
    while True:
        next_value = random.randint(1, 4)
        if len(game_order) == 0:
            game_order.append(next_value)
            break
        elif game_order[-1] != next_value:
            game_order.append(next_value)
            break
    flash_buttons()


def change_label(message):
    """Change the text of the playing label"""
    play_button.config(text=message)
    if message == "Playing!":
        play_button.config(state=tk.DISABLED)


def flash_buttons():
    """Flash all buttons in the list order"""
    global red_button
    global yellow_button
    global blue_button
    global green_button

    delay = 500
    for button in game_order:
        if button == 1:
            root.after(delay, lambda:animate(red_button))
        if button == 2:
            root.after(delay, lambda:animate(blue_button))
        if button == 3:
            root.after(delay, lambda:animate(yellow_button))
        if button == 4:
            root.after(delay, lambda:animate(green_button))

        delay += time_delay

    enable_buttons()


def enable_buttons():
    green_button.config(state=tk.ACTIVE, bg="green")
    red_button.config(state=tk.ACTIVE, bg="red")
    blue_button.config(state=tk.ACTIVE, bg="blue")
    yellow_button.config(state=tk.ACTIVE, bg="yellow")


def animate(button):
    """Animate a given button by changing its colour"""
    button.config(state=tk.ACTIVE)
    root.after(time_delay, lambda:button.config(state=tk.NORMAL))


def disable_buttons():
    """Disable all buttons and change their colours to a darker shade."""
    green_button.config(state=tk.DISABLED, bg="dark green")
    red_button.config(state=tk.DISABLED, bg="dark red")
    blue_button.config(state=tk.DISABLED, bg="dark blue")
    yellow_button.config(state=tk.DISABLED, bg="#ab9208")


def press_button(value):
    player_order.append(value)
    if len(player_order) == len(game_order):
        check_loss()


def check_loss():
    """Check for a loss in the game, reset game if so"""
    disable_buttons()
    if player_order == game_order:
        change_label("Correct!")
        root.after(2000, pick_sequence())
        change_label("Playing!")
    else:
        change_label("You lost!")
        disable_buttons()
        reset_game()


def reset_game():
    global player_order
    global game_order

    player_order = []
    game_order = []
    root.after(2000, play_button.config(text="Play!", state=tk.ACTIVE))


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
red_button = tk.Button(game_frame, bg="red", font=("Rubrik", 50), text="", width=4, activebackground="pink", command=press_button(1))
red_button.grid(row=0, column=0, padx=20, pady=20)
blue_button = tk.Button(game_frame, bg="blue", font=("Rubrik", 50), text="", width=4, activebackground="light blue", command=press_button(2))
blue_button.grid(row=1, column=0, padx=20, pady=20)
yellow_button = tk.Button(game_frame, bg="yellow", font=("Rubrik", 50), text="", width=4, activebackground="light yellow", command=press_button(3))

yellow_button.grid(row=0, column=1, padx=20, pady=20)
green_button = tk.Button(game_frame, bg="green", font=("Rubrik", 50), text="", width=4, activebackground="light green", command=press_button(4))
green_button.grid(row=1, column=1, padx=20, pady=20)

play_button = tk.Button(score_frame, text="Play!", font=("Rubrik", 25), bg="green", command=play_game)
play_button.grid(row=0, column=0)

score_label = tk.Label(score_frame, text="Score:   ", font=("Rubrik", 25), bg="#adc698")
score_label.grid(row=0, column=1, padx=20)

disable_buttons()
root.mainloop()
