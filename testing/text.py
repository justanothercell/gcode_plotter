from plotter import Plotter
from plot_text import draw_text

plotter = Plotter(185, 185, 0, 50, 5, 7)

plotter.goto(10, 160)
# plotter.goto(-700, 180)

with plotter.with_local_zero(s=5):
    plotter.goto(-0.5, 3.5)
    plotter.down()
    plotter.goto(33, 3.5)
    plotter.goto(33, -23.5)
    plotter.goto(-0.5, -23.5)
    plotter.goto(-0.5, 3.5)
    plotter.up()
    for i, line in enumerate([
        'ABCDEFGHIJKLM',
        'NOPQRSTUVWXYZ',
        '1234567890',
        '+-*/{}()[]\\\'-_".,:;#~><|=^°!?%&',
        '',
        'LOREM IPSUM DOLOR SIT AMET, CONSECTETUR',
        'ADIPISCING ELIT, SED DO EIUSMOD TEMPOR',
        'INCIDIDUNT UT LABORE ET DOLORE MAGNA',
        'ALIQUA. UT ENIM AD MINIM VENIAM, QUIS',
        'NOSTRUD EXERCITATION ULLAMCO LABORIS',
        'NISI UT ALIQUIP EX EA COMMODO CONSEQUAT.',
        'DUIS AUTE IRURE DOLOR IN REPREHENDERIT',
        'IN VOLUPTATE VELIT ESSE CILLUM DOLORE',
        'EU FUGIAT NULLA PARIATUR. EXCEPTEUR SINT',
        'OCCAECAT CUPIDATAT NON PROIDENT, SUNT IN',
        'CULPA QUI OFFICIA DESERUNT MOLLIT ANIM',
        'ID EST LABORUM.'
    ]):
        plotter.goto(0, 1.5 * (1-i))
        draw_text(plotter, line)