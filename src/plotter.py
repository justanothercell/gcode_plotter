from math import cos, sin


class Context:
    def __init__(self, pop):
        self.pop = pop

    def __enter__(self):
        pass

    def __exit__(self, ty, value, traceback):
        self.pop()


class Plotter:
    def __init__(self, width: float, height: float, offset_x, offset_y, h_down, h_up):
        self.width = width
        self.height = height
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.h_down = h_down
        self.h_up = h_up
        self.instructions = []
        self.color = (255, 255, 255)
        self.zero_x = 0.0
        self.zero_y = 0.0
        self.angle = 0
        self.scale = 1
        self.x = 0.0
        self.y = 0.0
        self.is_down = False
        self.instructions.append((self.x, self.y, self.is_down, self.color))

    def up(self):
        self.is_down = False

    def down(self):
        self.is_down = True

    def with_pen(self):
        pen = self.is_down

        def pop():
            self.is_down = pen

        return Context(pop)

    def move(self, dx: float, dy: float):
        self.x += dx
        self.y += dy
        if not self.is_down and not self.instructions[-1][2]:
            self.instructions.pop()
        self.instructions.append((self.x * cos(self.angle) * self.scale - self.y * sin(self.angle) * self.scale + self.zero_x,
                                  self.x * sin(self.angle) * self.scale + self.y * cos(self.angle) * self.scale + self.zero_y,
                                  self.is_down, self.color))

    def goto(self, x: float, y: float):
        self.x = x
        self.y = y
        if not self.is_down and not self.instructions[-1][2]:
            self.instructions.pop()
        self.instructions.append((self.x * cos(self.angle) * self.scale - self.y * sin(self.angle) * self.scale + self.zero_x,
                                  self.x * sin(self.angle) * self.scale + self.y * cos(self.angle) * self.scale + self.zero_y,
                                  self.is_down, self.color))

    def with_local(self, zx: float, zy: float) -> Context:
        self.zero_x += zx * cos(self.angle) * self.scale + zy * sin(self.angle) * self.scale
        self.zero_y += zy * cos(self.angle) * self.scale + zx * sin(self.angle) * self.scale
        px = self.x
        py = self.y
        self.x -= zx
        self.y -= zy

        def pop():
            self.zero_x -= zx * cos(self.angle) * self.scale + zy * sin(self.angle) * self.scale
            self.zero_y -= zy * cos(self.angle) * self.scale + zx * sin(self.angle) * self.scale
            self.x = px
            self.y = py

        return Context(pop)

    def with_local_zero(self, a: float = 0, s: float = 1) -> Context:
        zx = self.x * cos(self.angle) * self.scale - self.y * sin(self.angle) * self.scale
        zy = self.x * sin(self.angle) * self.scale + self.y * cos(self.angle) * self.scale
        px = self.x
        py = self.y
        self.zero_x += zx
        self.zero_y += zy
        self.x = 0
        self.y = 0
        self.angle += a
        self.scale *= s

        def pop():
            self.zero_x -= zx
            self.zero_y -= zy
            self.x = px
            self.y = py
            self.angle -= a
            self.scale /= s

        return Context(pop)

    def with_color(self, r: int, g: int, b: int):
        oc = self.color
        self.color = (r, g, b)

        def pop():
            self.color = oc

        return Context(pop)
