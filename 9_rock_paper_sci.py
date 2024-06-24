import tkinter as tk
import random

def playbutton(player_choice):
    global user_score, computer_score

    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result_label.config(text=f"Computer chose {computer_choice}. It's a tie!")
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
            (player_choice == 'Paper' and computer_choice == 'Rock') or \
            (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result_label.config(text=f"Computer chose {computer_choice}. You win!")
        user_score += 1
    else:
        result_label.config(text=f"Computer chose {computer_choice}. You lose!")
        computer_score += 1

    scores_label.config(text=f"User: {user_score}  Computer: {computer_score}")


def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    scores_label.config(text="User: 0  Computer: 0")
    result_label.config(text="")

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("450x370")
root.configure(bg="black")
user_score = 0
computer_score = 0

frame = tk.Frame(root,bg="black")
frame.pack(padx=20, pady=20)
myLabel=tk.Label(frame,text="Rock Paper Scissor Game",font=("Times New Roman",25,'bold'),bg="black",fg="white")
myLabel.grid(row=0,column=0,columnspan=5,pady=10)
instructions_label = tk.Label(frame, text="Select your choice",font=("Helvetica",16),bg="black",fg="white")
instructions_label.grid(row=1, column=0, columnspan=3, pady=10)

rock_button = tk.Button(frame, text="Rock",font=("Aerial",14),width=10, command=lambda: playbutton('Rock'))
rock_button.grid(row=2, column=0, padx=10,pady=7)

paper_button = tk.Button(frame, text="Paper",font=("Aerial",14),width=10, command=lambda: playbutton('Paper'))
paper_button.grid(row=2, column=1, padx=10,pady=7)

scissors_button = tk.Button(frame, text="Scissors",font=("Aerial",14) ,width=10, command=lambda: playbutton('Scissors'))
scissors_button.grid(row=2, column=2, padx=10,pady=7)

# Label to display result
result_label = tk.Label(root, text="", font=('Helvetica', 16), pady=20)
result_label.pack()


scores_label = tk.Label(root, text="User: 0  Computer: 0", font=('Helvetica', 12),bg="black",fg="white")
scores_label.pack(padx=10,pady=8)


play_again_button = tk.Button(root, text="Play Again",font=("Calibri",12),command=reset_game)
play_again_button.pack(padx=10,pady=10)


root.mainloop()
