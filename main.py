import tkinter as tk
from tkinter import *
import random
import time
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Typing speed test")
root.configure(background="black")
root.geometry("650x600")

TextFrame = Frame(root, bg="#ed4857")
TextFrame.grid(row=1, column=0, padx=30)

MainFrame = Frame(root, bg="black", bd=0)
MainFrame.grid(row=2, column=0, padx=0)

keys_list = [["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"],
             ["Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P"],
             ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
             ["Z", "X", "C", "V", "B", "N", "M"]]

word_list = []
start_time = None
typed_words = []

#   ----------NUMBERS-----------
one_img = Image.open("./Keyboard/1.png")
one_img = one_img.resize((100, 100))
one = ImageTk.PhotoImage(one_img)

two_img = Image.open("./Keyboard/2.png")
two_img = two_img.resize((100, 100))
two = ImageTk.PhotoImage(two_img)

three_img = Image.open("./Keyboard/3.png")
three_img = three_img.resize((100, 100))
three = ImageTk.PhotoImage(three_img)

four_img = Image.open("./Keyboard/4.png")
four_img = four_img.resize((100, 100))
four = ImageTk.PhotoImage(four_img)

five_img = Image.open("./Keyboard/5.png")
five_img = five_img.resize((100, 100))
five = ImageTk.PhotoImage(five_img)

six_img = Image.open("./Keyboard/6.png")
six_img = six_img.resize((100, 100))
six = ImageTk.PhotoImage(six_img)

seven_img = Image.open("./Keyboard/7.png")
seven_img = seven_img.resize((100, 100))
seven = ImageTk.PhotoImage(seven_img)

eight_img = Image.open("./Keyboard/8.png")
eight_img = eight_img.resize((100, 100))
eight = ImageTk.PhotoImage(eight_img)

nine_img = Image.open("./Keyboard/9.png")
nine_img = nine_img.resize((100, 100))
nine = ImageTk.PhotoImage(nine_img)

zero_img = Image.open("./Keyboard/0.png")
zero_img = zero_img.resize((100, 100))
zero = ImageTk.PhotoImage(zero_img)

#   ----------LETTERS-----------

q_img = Image.open("./Keyboard/Q.png")
q_img = q_img.resize((100, 100))
Q = ImageTk.PhotoImage(q_img)

w_img = Image.open("./Keyboard/W.png")
w_img = w_img.resize((100, 100))
W = ImageTk.PhotoImage(w_img)

e_img = Image.open("./Keyboard/E.png")
e_img = e_img.resize((100, 100))
E = ImageTk.PhotoImage(e_img)

r_img = Image.open("./Keyboard/R.png")
r_img = r_img.resize((100, 100))
R = ImageTk.PhotoImage(r_img)

t_img = Image.open("./Keyboard/T.png")
t_img = t_img.resize((100, 100))
T = ImageTk.PhotoImage(t_img)

y_img = Image.open("./Keyboard/Y.png")
y_img = y_img.resize((100, 100))
Y = ImageTk.PhotoImage(y_img)

u_img = Image.open("./Keyboard/U.png")
u_img = u_img.resize((100, 100))
U = ImageTk.PhotoImage(u_img)

i_img = Image.open("./Keyboard/I.png")
i_img = i_img.resize((100, 100))
I = ImageTk.PhotoImage(i_img)

o_img = Image.open("./Keyboard/O.png")
o_img = o_img.resize((100, 100))
O = ImageTk.PhotoImage(o_img)

p_img = Image.open("./Keyboard/P.png")
p_img = p_img.resize((100, 100))
P = ImageTk.PhotoImage(p_img)

a_img = Image.open("./Keyboard/A.png")
a_img = a_img.resize((100, 100))
A = ImageTk.PhotoImage(a_img)

s_img = Image.open("./Keyboard/S.png")
s_img = s_img.resize((100, 100))
S = ImageTk.PhotoImage(s_img)

d_img = Image.open("./Keyboard/D.png")
d_img = d_img.resize((100, 100))
D = ImageTk.PhotoImage(d_img)

f_img = Image.open("./Keyboard/F.png")
f_img = f_img.resize((100, 100))
F = ImageTk.PhotoImage(f_img)

g_img = Image.open("./Keyboard/G.png")
g_img = g_img.resize((100, 100))
G = ImageTk.PhotoImage(g_img)

h_img = Image.open("./Keyboard/H.png")
h_img = h_img.resize((100, 100))
H = ImageTk.PhotoImage(h_img)

j_img = Image.open("./Keyboard/J.png")
j_img = j_img.resize((100, 100))
J = ImageTk.PhotoImage(j_img)

k_img = Image.open("./Keyboard/K.png")
k_img = k_img.resize((100, 100))
K = ImageTk.PhotoImage(k_img)

l_img = Image.open("./Keyboard/L.png")
l_img = l_img.resize((100, 100))
L = ImageTk.PhotoImage(l_img)

z_img = Image.open("./Keyboard/Z.png")
z_img = z_img.resize((100, 100))
Z = ImageTk.PhotoImage(z_img)

x_img = Image.open("./Keyboard/X.png")
x_img = x_img.resize((100, 100))
X = ImageTk.PhotoImage(x_img)

c_img = Image.open("./Keyboard/C.png")
c_img = c_img.resize((100, 100))
C = ImageTk.PhotoImage(c_img)

v_img = Image.open("./Keyboard/V.png")
v_img = v_img.resize((100, 100))
V = ImageTk.PhotoImage(v_img)

b_img = Image.open("./Keyboard/B.png")
b_img = b_img.resize((100, 100))
B = ImageTk.PhotoImage(b_img)

n_img = Image.open("./Keyboard/N.png")
n_img = n_img.resize((100, 100))
N = ImageTk.PhotoImage(n_img)

m_img = Image.open("./Keyboard/M.png")
m_img = m_img.resize((100, 100))
M = ImageTk.PhotoImage(m_img)

# Create buttons with corresponding images
for i, key_row in enumerate(keys_list):
    for j, key in enumerate(key_row):
        img = None
        if key == "one":
            img = one
        elif key == "two":
            img = two
        elif key == "three":
            img = three
        elif key == "four":
            img = four
        elif key == "five":
            img = five
        elif key == "six":
            img = six
        elif key == "seven":
            img = seven
        elif key == "eight":
            img = eight
        elif key == "nine":
            img = nine
        elif key == "zero":
            img = zero
        elif key == "Q":
            img = Q
        elif key == "W":
            img = W
        elif key == "E":
            img = E
        elif key == "R":
            img = R
        elif key == "T":
            img = T
        elif key == "Y":
            img = Y
        elif key == "U":
            img = U
        elif key == "I":
            img = I
        elif key == "O":
            img = O
        elif key == "P":
            img = P
        elif key == "A":
            img = A
        elif key == "S":
            img = S
        elif key == "D":
            img = D
        elif key == "F":
            img = F
        elif key == "G":
            img = G
        elif key == "H":
            img = H
        elif key == "J":
            img = J
        elif key == "K":
            img = K
        elif key == "L":
            img = L
        elif key == "Z":
            img = Z
        elif key == "X":
            img = X
        elif key == "C":
            img = C
        elif key == "V":
            img = V
        elif key == "B":
            img = B
        elif key == "N":
            img = N
        elif key == "M":
            img = M

        if img:
            btn = tk.Button(MainFrame, highlightthickness=0, bd=0, image=img, bg="black", width=60, height=60)
            btn.grid(row=i, column=j, padx=0, pady=0)

display = tk.Entry(MainFrame, font=("arial", 28, "bold"), bd=5, width=28, bg="#ed4857", relief=FLAT)
display.grid(row=len(keys_list), column=0, columnspan=len(keys_list[0]), pady=10)


# def button_click(key):
#     current = display.get()
#     display.delete(0, tk.END)
#     display.insert(0, str(current) + str(key))

# for i, key_row in enumerate(keys_list):
#     for j, key in enumerate(key_row):
#         tk.Button(MainFrame, font=("arial", 14, "bold"), text=key, width=7, height=2, command=lambda key=key:
#                   button_click(key)).grid(row=i, column=j)


def get_words():
    global word_list  # Use the global keyword to modify the global word_list
    with open("words.txt", "r") as words:
        all_words = words.read().split()  # Split words into a list
        word_list = random.sample(all_words, 15)  # Get 15 random words
        result.delete(1.0, tk.END)
        result.insert(END, list_to_string(word_list).lower())


def list_to_string(words_list):
    return " ".join(words_list)


def spelling_check(event=None):
    global typed_words
    user_input = display.get().strip()
    if user_input:
        typed_words.append(user_input)

    correct_words = 0
    result.delete(1.0, tk.END)

    for idx, word in enumerate(word_list):
        if idx < len(typed_words):
            user_word = typed_words[idx]
            if user_word.lower() == word:
                result.insert(tk.END, word + " ", 'correct')
                correct_words += 1
            else:
                result.insert(tk.END, word + " ", 'incorrect')
        else:
            result.insert(tk.END, word + " ")

    result.tag_config('correct', foreground='green')
    result.tag_config('incorrect', foreground='red')

    elapsed_time = time.time() - start_time
    wpm = (len(typed_words) / (elapsed_time / 60)) if elapsed_time > 0 else 0
    result_label.config(text=f"WPM: {wpm:.2f}, Correct Words: {correct_words}, "
                             f"Incorrect Words: {len(typed_words) - correct_words}")

    display.delete(0, tk.END)

    if len(typed_words) >= len(word_list):
        pause_timer()


def update_timer():
    if start_time:
        elapsed_time = time.time() - start_time
        # timer_label.config(text=f"Time: {elapsed_time:.2f} seconds")
    root.after(100, update_timer)


def start_timer(event=None):
    global start_time
    if not start_time:
        start_time = time.time()
        display.unbind("<KeyPress>", on_keypress_id)
        display.bind("<space>", space_pressed)
        update_timer()


def space_pressed(event):
    spelling_check()
    return "break"


def pause_timer():
    global start_time
    display.unbind("<space>")
    elapsed_time = time.time() - start_time
    wpm = (len(typed_words) / (elapsed_time / 60)) if elapsed_time > 0 else 0
    result_label.config(text=f"Completed! Time: {elapsed_time:.2f} seconds, WPM: {wpm:.2f}")
    start_time = None


def reset_timer():
    global start_time, typed_words
    start_time = None
    typed_words = []
    result.delete(1.0, tk.END)
    result.insert(END, list_to_string(word_list).lower())
    display.delete(0, tk.END)
    result_label.config(text="WPM: 0.00, Correct Words: 0, Incorrect Words: 0")
    # timer_label.config(text="Time: 0.00 seconds")
    display.bind("<KeyPress>", start_timer)


def reset_app():
    global start_time, typed_words
    start_time = None
    typed_words = []
    get_words()
    display.delete(0, tk.END)
    result_label.config(text="WPM: 0.00, Correct Words: 0, Incorrect Words: 0")
    # timer_label.config(text="Time: 0.00 seconds")
    display.bind("<KeyPress>", start_timer)


# Add labels to display the result of the spelling check and the timer
result_label = Label(MainFrame, text="WPM: 0.00, Correct Words: 0, Incorrect Words: 0", font=("arial", 14, "bold"),
                     bg="black", fg="white")
result_label.grid(row=len(keys_list) + 1, column=0, columnspan=len(keys_list[0]), pady=10)

# timer_label = Label(MainFrame, text="Time: 0.00 seconds", font=("arial", 14, "bold"), bg="#ed4857")
# timer_label.grid(row=len(keys_list) + 2, column=0, columnspan=len(keys_list[0]), pady=10)

# Add buttons for resetting the timer and the app
reset_timer_button = Button(MainFrame, text="Try again", font=("arial", 14, "bold"), command=reset_timer,
                            bg="black", fg="white")
reset_timer_button.grid(row=len(keys_list) + 3, column=0, columnspan=len(keys_list[0]) // 2, pady=10)

reset_app_button = Button(MainFrame, text="New words", font=("arial", 14, "bold"), command=reset_app,
                          bg="black", fg="white")
reset_app_button.grid(row=len(keys_list) + 3, column=len(keys_list[0]) // 2, columnspan=len(keys_list[0]) // 2, pady=10)

# Bind the first key press to start the timer
on_keypress_id = display.bind("<KeyPress>", start_timer)

result = Text(TextFrame, bg="black", fg="white", highlightthickness=0, font=("arial", 14, "bold"),
              wrap=WORD, height=5, width=55)
result.grid(column=0, row=0)

get_words()
root.mainloop()
