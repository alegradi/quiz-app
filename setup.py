import tkinter as tk

# Constants
THEME_COLOR = "#375362"
FONT = ("Arial", 12, "normal")

CATEGORIES = {
    "Information Technology": {
        "index": 18
    },
    "Films": {
        "index": 11
    },
    "History": {
        "index": 23
    }
}

QUESTION_COUNT = [
    10,
    20,
    50
]
DIFFICULTY = [
    "Easy",
    "Medium",
    "Hard"
]


class SetupInterface:

    def __init__(self):
        self.setup_window = tk.Tk()
        self.setup_window.title("Quiz App: Setup")
        self.setup_window.config(padx=20, pady=20, background=THEME_COLOR)

        # Title label
        self.title_label = tk.Label(text="Quiz App", font=("Arial", 20, "bold"), background=THEME_COLOR,
                                    foreground="white", pady=20)
        self.title_label.grid(column=0, row=0, columnspan=2)

        # Difficulty label
        self.diff_label = tk.Label(text="Difficulty:", font=FONT, background=THEME_COLOR, foreground="white",
                                   anchor="w", justify="left")
        self.diff_label.grid(column=0, row=1)

        self.difficulty = tk.StringVar(self.setup_window)
        self.difficulty.set("Easy")

        self.difficulty_drop = tk.OptionMenu(self.setup_window, self.difficulty, *DIFFICULTY)
        self.difficulty_drop.grid(column=1, row=1)

        # Question count label
        self.q_count_label = tk.Label(text="Number of questions:", font=FONT, background=THEME_COLOR,
                                      foreground="white", anchor="w", padx=15)
        self.q_count_label.grid(column=0, row=2)

        self.q_count = tk.StringVar(self.setup_window)
        self.q_count.set("10")

        self.q_count_drop = tk.OptionMenu(self.setup_window, self.q_count, *QUESTION_COUNT)
        self.q_count_drop.grid(column=1, row=2)

        # Topic label
        self.q_count_label = tk.Label(text="Quiz topic:", font=FONT, background=THEME_COLOR,
                                      foreground="white", anchor="w")
        self.q_count_label.grid(column=0, row=3)

        self.topic = tk.StringVar(self.setup_window)
        self.topic.set("Films")

        self.topic_drop = tk.OptionMenu(self.setup_window, self.topic, *CATEGORIES)
        self.topic_drop.grid(column=1, row=3)

        # Submit button
        self.submit_button = tk.Button(text="Submit", pady=15, command=self.submit_selections)
        self.submit_button.grid(column=0, row=4, columnspan=2)

        self.parameters = {}

        self.setup_window.mainloop()

    def submit_selections(self):
        self.parameters = {
            "amount": self.q_count.get(),
            "type": "boolean",
            "category": CATEGORIES[self.topic.get()]["index"],
            "difficulty": self.difficulty.get().lower()
        }

        # Close setup window
        self.setup_window.destroy()
