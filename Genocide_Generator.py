import tkinter as tk
from tkinter import filedialog


def get_first_number(taco):
    """Returns the first numbers of the line as an integer"""
    result = ''
    for char in taco:
        if char.isdigit():
            # The character is a number
            result += char
        else:
            # The character is not a number
            break
    if result == '':
        return 0
    x = int(result)
    return x


def list_out_lines(file):
    line_list = []
    with open(file, 'r+') as g:
        lines = g.read().splitlines()
        for line in lines:
            if get_first_number(line) < 1347:
                line_list.append(line)
    return line_list
"""Takes the lines that match the parameter and folds them into a list"""


def end_of_history():
    saved_list = list_out_lines(Eu4)
    f = open(Eu4, 'w')
    f.writelines(["%s\n" % item for item in saved_list])
    f.close()
"""Overwrites file with the list"""


def black_plague():
    fk = open(Eu4, 'a+')
    fk.writelines(['\n',
                       '1347.1.1 = {} # Black Death Arrives\n',
                       '1370.1.1 = {    base_manpower = 1\n',
                       '                base_tax = 1\n',
                       '                base_production = 1}\n'
                       '# Edit each to be 1/3 of last base. End of 20 year Plague\n',
                       '1404.1.1 = {} # Final Death Arrives\n',
                       '1405.1.1 = {    owner = XXX\n',
                       '                controller = XXX\n',
                       '                citysize = 0\n',
                       '                base_tax = 1\n',
                       '                base_production = 1\n',
                       '                base_manpower = 1} # Final Death is complete, this makes the provence empty\n'])
    fk.close()


while True:
    root = tk.Tk()
    root.withdraw()
    Eu4 = filedialog.askopenfilename()
    end_of_history()
    black_plague()

'''
Assigns filename to Eu4 variable and commits genocide
'''
