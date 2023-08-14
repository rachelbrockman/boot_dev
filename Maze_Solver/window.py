from tkinter import Tk, BOTH, Canvas  # how do i import tkinter??


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

    def close(self):
        self.running = False
    
class Point:
    x = 0
    y = 0

class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2
    
    def draw(self):
        
