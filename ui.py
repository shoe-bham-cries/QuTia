import tkinter as tki

THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self):
        self.window = tki.Tk()
        self.window.title("QuTia")
        self.window.minsize(width=350, height=500)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.scorelabel = tki.Label(text="Score", fg="white", bg=THEME_COLOR)
        self.scorelabel.grid(column=1, row=0)

        self.canvas = tki.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="placeholder",
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true_image = tki.PhotoImage("images/true.png")
        self.true = tki.Button(image=true_image, highlightthickness=0, height=100, width=100)
        self.true.grid(column=0, row=2)
        false_image = tki.PhotoImage('images/false.png')
        self.false = tki.Button(image=false_image)
        self.false.grid(column=1, row=2)
        self.window.mainloop()
