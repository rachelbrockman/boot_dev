from tkinter import * (
    Tk,
    BOTH,
    Canvas,
)  # how do i import tkinter>>> installed via homebrew


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()  # create new root widget
        self.root.title("Maze Solver")  # set the title property of the root widget
        self.canvas = Canvas(self.root, width=self.width, height=self.height)  # create
        # a Canvas and save it as a data member
        self.canvas.pack()
        self.running = False
        self.root.protocol(
            "WM_DELETE_WINDOW", self.close
        )  ##removed __ from self.root.protocol

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.point_1.x,
            self.point_1.y,
            self.point_2.x,
            self.point_2.y,
            fill=fill_color,
            width=2,
        )
        canvas.pack(fill=BOTH, expand=1)
