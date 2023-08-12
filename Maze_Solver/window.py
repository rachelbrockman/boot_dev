from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.root = Tk()  # create new root widget
        self.root.title(title)  # set the title property of the root widget
        self.canvas = Canvas(self.root, width=self.width, height=self.height)  # create
        # a Canvas and save it as a data member
        self.canvas.pack()
        self.running = False
