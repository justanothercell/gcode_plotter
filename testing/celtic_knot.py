from plotter import Plotter

plotter = Plotter(185, 185, 0, 50, 5, 7)


def quarter():
    global plotter
    with plotter.with_local_zero():
        with plotter.with_pen():
            # inner arc
            plotter.down()
            plotter.move(3, 0)
            plotter.up()
            plotter.move(1, 0)
            plotter.down()
            plotter.move(0.5, 0)
            plotter.move(0.5, 0.5)
            plotter.move(-0.5, 0.5)
            plotter.move(-2.5, 0)
            plotter.up()
            plotter.move(-1, 0)
            plotter.down()
            plotter.move(-3, 0)
            
            # goto outer arc
            plotter.up()
            plotter.move(0, 1)
            plotter.down()
            
            # outer arc
            plotter.move(3, 0)
            plotter.up()
            plotter.move(1, 0)
            plotter.down()
            plotter.move(2.7, 0)
            plotter.move(1.5, -1.5)
            plotter.move(-1.5, -1.5)
            plotter.move(-0.7, 0)
            plotter.up()
            plotter.move(-1, 0)
            plotter.down()
            plotter.move(-3, 0)
            
            # goto ring
            plotter.up()
            plotter.move(0.7, -1)
            plotter.down()
            
            # outer ring
            plotter.move(-2.7, 0)
            plotter.up()
            plotter.move(-1, 0)
            plotter.down()
            plotter.move(-0.7, 0)
            plotter.move(-1.5, -1.5)
            plotter.move(1.5, -1.5)
            plotter.move(2.7, 0)
            plotter.up()
            plotter.move(1, 0)
            plotter.down()
            plotter.move(0.7, 0)
            plotter.move(1.5, 1.5)
            plotter.move(-1.5, 1.5)
            
            # goto inner ring
            plotter.up()
            plotter.move(-0.2, -1)
            plotter.down()
            
            # inner ring
            plotter.move(-2.5, 0)
            plotter.up()
            plotter.move(-1, 0)
            plotter.down()
            plotter.move(-0.5, 0)
            plotter.move(-0.5, -0.5)
            plotter.move(0.5, -0.5)
            plotter.move(2.5, 0)
            plotter.up()
            plotter.move(1, 0)
            plotter.down()
            plotter.move(0.5, 0)
            plotter.move(0.5, 0.5)
            plotter.move(-0.5, 0.5)


def plot_knot():
    global plotter
    global quarter
    from math import pi
    dx = 1.5
    dy = -0.5
    for i in range(4):
        with plotter.with_local_zero(a=pi/2*i):
            plotter.goto(dx, dy)
            quarter()


plotter.goto(90, 90)
with plotter.with_local_zero(s=5):
    offset = 8.15
    plotter.goto(offset, 0)
    plot_knot()
    plotter.goto(-offset, 0)
    plot_knot()
    plotter.goto(0, offset)
    plot_knot()
    plotter.goto(0, -offset)
    plot_knot()