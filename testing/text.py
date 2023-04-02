from plotter import Plotter

plotter = Plotter(185, 185, 0, 50, 5, 7)

letters = [[] for _ in range(256)]
letters[ord(' ')] = []
letters[ord('A')] = [False, (0.175, 0), True, (0.25+0.175, 1), (0.4+0.175, 1), (0.65+0.175, 0), False, (0.125+0.175, 0.5), True, (0.525+0.175, 0.5)]
letters[ord('B')] = [False, (0.3, 0), True, (0.3, 1), (0.55, 1), (0.7, 0.85), (0.7, 0.65), (0.55, 0.5), (0.3, 0.5), False, (0.55, 0.5), True, (0.7, 0.35), (0.7, 0.15), (0.55, 0), (0.3, 0)]
letters[ord('C')] = [False, (0.75, 0), True, (0.4, 0), (0.25, 0.15), (0.25, 0.85), (0.4, 1), (0.75, 1)]
letters[ord('D')] = [False, (0.25, 0), True, (0.6, 0), (0.75, 0.15), (0.75, 0.85), (0.6, 1), (0.25, 1), (0.25, 0)]
letters[ord('E')] = [False, (0.75, 0), True, (0.25, 0), (0.25, 1), (0.75, 1), False, (0.25, 0.5), True, (0.75, 0.5)]
letters[ord('F')] = [False, (0.25, 0), True, (0.25, 1), (0.75, 1), False, (0.25, 0.5), True, (0.75, 0.5)]
letters[ord('G')] = [False, (0.8, 0.85), True, (0.65, 1), (0.35, 1), (0.2, 0.85), (0.2, 0.15), (0.35, 0), (0.65, 0), (0.8, 0.15), (0.8, 0.45), (0.5, 0.45)]
letters[ord('H')] = [False, (0.25, 1), True, (0.25, 0), False, (0.75, 1), True, (0.75, 0), False, (0.25, 0.5), True, (0.75, 0.5)]
letters[ord('I')] = [False, (0.5, 1), True, (0.5, 0), False, (0.4, 0), True, (0.6, 0), False, (0.4, 1), True, (0.6, 1)]
letters[ord('J')] = [False, (0.25, 1), True, (0.75, 1), (0.75, 0.15), (0.6, 0), (0.4, 0), (0.25, 0.15)]
letters[ord('K')] = [False, (0.25, 1), True, (0.25, 0), False, (0.75, 1), True, (0.25, 0.5), (0.75, 0)]
letters[ord('L')] = [False, (0.25, 1), True, (0.25, 0), (0.75, 0)]
letters[ord('M')] = [False, (0.2, 0), True, (0.2, 1), (0.5, 0.3), (0.8, 1), (0.8, 0)]
letters[ord('N')] = [False, (0.25, 0), True, (0.25, 1), (0.75, 0), (0.75, 1)]
letters[ord('O')] = [False, (0.35, 0), True, (0.2, 0.15), (0.2, 0.85), (0.35, 1), (0.65, 1), (0.8, 0.85), (0.8, 0.15), (0.65, 0), (0.35, 0)]
letters[ord('P')] = [False, (0.25, 0), True, (0.25, 1), (0.6, 1), (0.75, 0.85), (0.75, 0.65), (0.6, 0.5), (0.25, 0.5)]
letters[ord('Q')] = [False, (0.35, 0), True, (0.2, 0.15), (0.2, 0.85), (0.35, 1), (0.65, 1), (0.8, 0.85), (0.8, 0.15), (0.65, 0), (0.35, 0), False, (0.6, 0.2), True, (0.825, -0.025)]
letters[ord('R')] = [False, (0.25, 0), True, (0.25, 1), (0.6, 1), (0.75, 0.85), (0.75, 0.65), (0.6, 0.5), (0.25, 0.5), (0.75, 0)]
letters[ord('S')] = [False, (0.75, 0.85), True, (0.6, 1), (0.4, 1), (0.25, 0.85), (0.25, 0.65), (0.75, 0.35), (0.75, 0.15), (0.6, 0), (0.4, 0), (0.25, 0.15)]
letters[ord('T')] = [False, (0.5, 1), True, (0.5, 0), False, (0.25, 1), True, (0.75, 1)]
letters[ord('U')] = [False, (0.2, 1), True, (0.2, 0.15), (0.35, 0), (0.65, 0), (0.8, 0.15), (0.8, 1)]
letters[ord('V')] = [False, (0.25, 1), True, (0.5, 0), (0.75, 1)]
letters[ord('W')] = [False, (0.2, 1), True, (0.2, 0), (0.5, 0.7), (0.8, 0), (0.8, 1)]
letters[ord('X')] = [False, (0.25, 1), True, (0.75, 0), False, (0.25, 0), True, (0.75, 1)]
letters[ord('Y')] = [False, (0.25, 1), True, (0.5, 0.5), False, (0.75, 1), True, (0.5, 0.5), (0.5, 0)]
letters[ord('Z')] = [False, (0.25, 1), True, (0.75, 1), (0.25, 0), (0.75, 0)]

letters[ord(',')] = [False, (0.5, 0.2), True, (0.5, -0.2)]
letters[ord('.')] = [False, (0.5, 0), True, (0.5, 0)]

letters[ord('1')] = [False, (0.25, 0.7), True, (0.5, 1), (0.5, 0), False, (0.3, 0), True, (0.7, 0)]
letters[ord('2')] = [False, (0.25, 0.85), True, (0.4, 1), (0.6, 1), (0.75, 0.85), (0.75, 0.6), (0.25, 0), (0.75, 0)]
letters[ord('3')] = [False, (0.3, 1), True, (0.55, 1), (0.7, 0.85), (0.7, 0.65), (0.55, 0.5), (0.3, 0.5), False, (0.55, 0.5), True, (0.7, 0.35), (0.7, 0.15), (0.55, 0), (0.3, 0)]
letters[ord('4')] = [False, (0.4, 1), True, (0.25, 0.35), (0.75, 0.35), False, (0.6, 0.75), True, (0.6, 0)]
letters[ord('5')] = [False, (0.75, 1), True, (0.25, 1), (0.25, 0.5), (0.6, 0.5), (0.75, 0.35), (0.75, 0.15), (0.6, 0), (0.4, 0), (0.25, 0.15)]
letters[ord('6')] = [False, (0.75, 0.85), True, (0.6, 1), (0.4, 1), (0.25, 0.85), (0.25, 0.15), (0.4, 0), (0.6, 0), (0.75, 0.15), (0.75, 0.35), (0.6, 0.5), (0.4, 0.5), (0.25, 0.35)]
letters[ord('7')] = [False, (0.25, 1), True, (0.75, 1), (0.3, 0), False, (0.35, 0.5), True, (0.7, 0.5)]
letters[ord('8')] = [False, (0.75, 0.65), True, (0.75, 0.85), (0.6, 1), (0.4, 1), (0.25, 0.85), (0.25, 0.65), (0.75, 0.35), (0.75, 0.15), (0.6, 0), (0.4, 0), (0.25, 0.15), (0.25, 0.35), (0.75, 0.65)]
letters[ord('9')] = [False, (0.25, 0.15), True, (0.4, 0), (0.6, 0), (0.75, 0.15), (0.75, 0.85), (0.6, 1), (0.4, 1), (0.25, 0.85), (0.25, 0.65), (0.4, 0.5), (0.6, 0.5), (0.75, 0.65)]
letters[ord('0')] = [False, (0.225, 0.15), True, (0.225, 0.85), (0.375, 1), (0.625, 1), (0.775, 0.85), (0.775, 0.15), (0.625, 0), (0.375, 0), (0.225, 0.15), (0.775, 0.85)]

def draw_letter(letter: str):
    global letters
    letter = letters[ord(letter)]
    with plotter.with_pen():
        with plotter.with_local_zero():
            for x in letter:
                if isinstance(x, bool):
                    if x:
                        plotter.down()
                    else:
                        plotter.up()
                else:
                    plotter.goto(*x)

def draw_text(text):
    global draw_letter, plotter
    for char in text:
        draw_letter(char)
        plotter.move(0.8, 0)
    

plotter.goto(10, 160)

with plotter.with_local_zero(s=5):
    plotter.goto(-0.5, 3.5)
    plotter.down()
    plotter.goto(33, 3.5)
    plotter.goto(33, -22)
    plotter.goto(-0.5, -22)
    plotter.goto(-0.5, -22)
    plotter.goto(-0.5, 3.5)
    plotter.up()
    for i, line in enumerate([
        'ABCDEFGHIJKLM',
        'NOPQRSTUVWXYZ',
        '1234567890 , .',
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
        draw_text(line)