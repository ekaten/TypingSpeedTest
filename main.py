import random
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


#### GLOBAL VARIABLES ####
ROOT_WIDTH = 800
ROOT_HEIGHT = 600
TOP_TEXT = "Please, familiarize yourself with the text:"
BOTTOM_TEXT = "Click below to start the typing speed test"
LABEL_FONT = ("Birch Std", 30, "bold")
TEXT_FONT = ("Courier New", 20, "normal")
RESULT_LABEL_FONT = ("Birch Std", 20, "bold")

timer = 60
count = 3
input_text = ""
typing_speed_level = ""
speed_words_per_minute = 0


#### FUNCTION DECLARATIONS ####
def get_text():
    global text
    with open("text/text.txt") as file:
        list_of_texts = file.readlines()
        text = random.choice(list_of_texts)
    return text


def countdown():
    global count
    instruction_bottom.configure(text=f"{count}")
    if count > 0:
        count = count - 1
    else:
        instruction_bottom.pack(pady=0)
        instruction_bottom.configure(text="START TYPING", font=("Arial", 25, "bold"))
        start_test()
        return
    root.after(1000, countdown)


def start_timer():
    global root, timer, timer_text, input_text, typing_speed_level, speed_words_per_minute
    if timer >= 10:
        timer_text.configure(text=f"00:{timer}")
    else:
        timer_text.configure(text=f"00:0{timer}")

    if timer > 0:
        timer -= 1
    else:
        root.geometry(f"{ROOT_WIDTH}x{ROOT_HEIGHT + 70}")
        instruction_bottom.configure(text="STOP")
        input_text = input_field.get("1.0", END)
        input_field.pack_forget()
        see_result.pack(pady=50)
        return
    root.after(1000, start_timer)


def launch_test_page():
    global count
    instruction_bottom.configure(text=f"{count}", font=("Arial", 100, "bold"), foreground="red")
    go_to_test.pack_forget()
    text_frame.pack(pady=30)
    countdown()


def start_test():
    global root, input_field, input_text
    root.geometry(f"{ROOT_WIDTH}x{ROOT_HEIGHT + 300}")
    instruction_top.pack_forget()
    timer_text.pack()
    input_field.pack(pady=30)
    input_field.focus()
    start_timer()


def show_score_explanation():
    scores_explained_bar.pack(side=TOP, pady=50, fill="y")
    scores_label.pack(side=TOP, pady=20)
    below.pack(side=LEFT, padx=10, pady=5)
    average.pack(side=LEFT, padx=10, pady=5)
    above.pack(side=LEFT, padx=10, pady=5)
    superior.pack(side=LEFT, padx=10, pady=5)

    below_speed.pack()
    average_speed.pack()
    above_speed.pack()
    superior_speed.pack()

    below_number.pack()
    average_number.pack()
    above_number.pack()
    superior_number.pack()

    see_result.pack_forget()


def show_user_result():
    global input_text, text_frame, speed_words_per_minute, typing_speed_level
    instruction_bottom.pack_forget()
    timer_text.pack_forget()
    text_frame.pack_forget()
    chars_typed = len(input_text) - 1
    print(chars_typed)
    speed_words_per_minute = int(chars_typed / 5)

    if speed_words_per_minute < 35:
        typing_speed_level = "BELOW AVERAGE"
    elif 35 <= speed_words_per_minute <= 45:
        typing_speed_level = "AVERAGE"
    elif 45 < speed_words_per_minute < 80:
        typing_speed_level = "ABOVE AVERAGE"
    elif speed_words_per_minute >= 80:
        typing_speed_level = "SUPERIOR"

    show_score_explanation()
    user_speed_frame.pack(pady=50)
    user_score.pack()
    your_result.pack(side=LEFT)
    user_speed.pack(side=LEFT)
    number_characters_typed.pack()
    result_page_buttons_frame.pack(pady=70)
    try_again.pack(side=LEFT, padx=10)
    quit_program.pack(side=LEFT, padx=10)
    number_characters_typed.config(text=f"({chars_typed} characters per minute)")
    user_score.config(text=f"{speed_words_per_minute} words/minute")
    user_speed.config(text=typing_speed_level)


def restart_program():
    global text_frame, the_text, instruction_bottom, go_to_test, count, timer
    scores_explained_bar.pack_forget()
    result_page_buttons_frame.pack_forget()
    user_speed_frame.pack_forget()
    number_characters_typed.pack_forget()
    user_score.pack_forget()
    instruction_bottom.config(text="")
    timer_text.config(text="")
    instruction_top.config(text=TOP_TEXT)
    instruction_top.pack(pady=10)
    text_frame.pack()
    instruction_bottom.pack()
    timer_text.pack()

    input_field.delete('1.0', END)
    timer = 60
    count = 10
    the_text = get_text()
    launch_test_page()


def quit_program():
    quit()


#### GUI SETUP ####

root = ttk.Window(themename="journal")
root.title("Typing Speed Test")
root.geometry(f"{ROOT_WIDTH}x{ROOT_HEIGHT}")
icon = ttk.PhotoImage(file='images/logo.png')
root.iconphoto(False, icon)

instruction_top = ttk.Label(root, text=TOP_TEXT, font=LABEL_FONT)
instruction_top.pack(pady=10)

the_text = get_text()
text_frame = ttk.Labelframe(root, text="Text sample:", padding=5, style='dark.TLabelframe')
text_frame.pack(pady=20)

text = Text(text_frame, font=TEXT_FONT, width=50, height=12, wrap=WORD, )
text.pack(padx=10, pady=10)
text.insert(INSERT, the_text)
text.configure(state=DISABLED, bg="black", fg="white")

instruction_bottom = ttk.Label(root, text=BOTTOM_TEXT, font=LABEL_FONT)
instruction_bottom.pack(pady=10)

go_to_test = ttk.Button(root, text="Start Test", bootstyle="success", width=20, command=launch_test_page)
go_to_test.pack(pady=20)

timer_text = ttk.Label(root, text="01.00", font=("Birch Std", 60, "bold"), foreground="red")

input_field = Text(root, height=12, width=50, font=("Courier New", 20, "bold"))
see_result = ttk.Button(root, text="See Your Result", bootstyle="success", width=20, command=show_user_result)

scores_explained_bar = ttk.Frame(root, width=ROOT_WIDTH - 20, height=ROOT_HEIGHT / 3)
scores_label = ttk.Label(scores_explained_bar, text="Typing Speed in Words Per Minute (WPM):", font=LABEL_FONT)
below = ttk.Frame(scores_explained_bar, width =(ROOT_WIDTH - 20) / 4, height=ROOT_HEIGHT / 3, )
average = ttk.Frame(scores_explained_bar, width =(ROOT_WIDTH - 20) / 4, height=ROOT_HEIGHT / 3)
above = ttk.Frame(scores_explained_bar, width =(ROOT_WIDTH - 20) / 4, height=ROOT_HEIGHT / 3)
superior = ttk.Frame(scores_explained_bar, width =(ROOT_WIDTH - 20) / 4, height=ROOT_HEIGHT / 3)

below_speed = ttk.Label(below, text="Below Average", background="black", font=RESULT_LABEL_FONT, foreground="white")
average_speed = ttk.Label(average, text="Average Speed", background="black", font=RESULT_LABEL_FONT, foreground="white")
above_speed = ttk.Label(above, text="Above Average", background="black", font=RESULT_LABEL_FONT, foreground="white")
superior_speed = ttk.Label(superior, text="Superior Speed", background="black", font=RESULT_LABEL_FONT, foreground="white")

below_number = ttk.Label(below, text="> 35", background="white", font=LABEL_FONT, foreground="red")
average_number = ttk.Label(average, text="35-45", background="white", font=LABEL_FONT, foreground="red")
above_number = ttk.Label(above, text="< 45", background="white", font=LABEL_FONT, foreground="red")
superior_number = ttk.Label(superior, text="< 80", background="white", font=LABEL_FONT, foreground="red")

user_speed_frame = ttk.Frame(root, width=ROOT_WIDTH - 20, height=ROOT_HEIGHT / 3)
your_result = ttk.Label(user_speed_frame, text="Your Typing speed is:", font=LABEL_FONT)
user_speed = ttk.Label(user_speed_frame, text=f"{typing_speed_level}", font=LABEL_FONT, foreground="red")
user_score = ttk.Label(root, text=f"", font=("Birch Std", 60, "bold"), foreground="red")
number_characters_typed = ttk.Label(root, text="", font=("Birch Std", 20, "bold"), foreground="black")

result_page_buttons_frame = ttk.Frame(root, width=ROOT_WIDTH - 20, height=40)
try_again = ttk.Button(result_page_buttons_frame, text="Try Again", bootstyle="success", width=20, command=restart_program)
quit_program = ttk.Button(result_page_buttons_frame, text="Quit", bootstyle="success", width=20, command=quit_program)

root.mainloop()