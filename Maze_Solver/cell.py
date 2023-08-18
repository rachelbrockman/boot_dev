class Cell:
    def __init__(
        self,
        has_left_wall,
        has_right_wall,
        has_top_wall,
        has_bottom_wall,
        _x1,
        _x2,
        _y1,
        _y2,
        _win,
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self._win = _win


def draw(self):
    if self.has_left_wall:
        self._win.canvas.draw_line(self._x1, self._y1, self._x1, self._y2)
    if self.has_right_wall:
        self._win.canvas.draw_line(self._x2, self._y1, self._x2, self._y2)
    if self.has_top_wall:
        self._win.canvas.draw_line(self._x1, self._y1, self._x2, self._y1)
    if self.has_bottom_wall:
        self._win.canvas.draw_line(self._x1, self._y2, self._x2, self._y2)
