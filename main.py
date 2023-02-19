import tkinter as tk


class Snake(tk.Canvas):  # "SnakeGame"
    def __init__(self):
        super().__init__(
            width=600, height=620, background="black", highlightthickness=0
        )

        self.pack()


root = tk.Tk()
root.title("TK-Snake")
root.resizable(False, False)
root.tk.call("tk", "scaling", 4.0)

board = Snake()
root.mainloop()
