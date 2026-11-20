# -*- coding: utf-8 -*-
import testlib
import os
import sys
from testlib import my_print, COL, check_expected

############ check that you have renamed the file as program.py   ###########
if not os.path.isfile('program.py'):
    print(  'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
#############################################################################

import program

#############################################################################
#### Mettete DEBUG=True per attivare la stack trace completa degli errori ###
DEBUG = True
#DEBUG = False
#############################################################################

################################################################################
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################


def test_personal_data_entry(run=True):
    assert program.nome      != 'NOME', f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
    assert program.cognome   != 'COGNOME', f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
    assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
    print(f'{COL["GREEN"]}Informazioni studente: {program.nome} {program.cognome} {program.matricola}{COL["RST"]}')
    return 1e-9

###############################################################################

# ----------------------------------- FUNC. 1 ----------------------------------- #

def do_test_func1(ID, expected):
    png_in  = f'func1/in_{ID}.png'
    res = program.func1(png_in)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il numero stelline è sbagliato! / The number of stars are incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 2


def test_func1_1(run=True):
    '''
    png_file = func1/in_1.png
    '''
    ID = 1
    expected = {(217, 159, 157): 3, (166, 93, 67): 2}
    return do_test_func1(ID, expected)


def test_func1_2(run=True):
    '''
    png_file = func1/in_2.png
    '''
    ID = 2
    expected = {(141, 103, 192): 1, (119, 174, 75): 3, (243, 120, 236): 1, (205, 231, 221): 2, (130, 146, 61): 2, (146, 91, 103): 1}
    return do_test_func1(ID, expected)


def test_func1_3(run=True):
    '''
    png_file = func1/in_3.png
    '''
    ID = 3
    expected = {(167, 116, 123): 3, (174, 166, 199): 2, (117, 86, 218): 1, (195, 157, 81): 1, (85, 246, 156): 2,
                (153, 242, 115): 5, (180, 118, 186): 1, (183, 131, 81): 2, (216, 102, 132): 4, (170, 230, 179): 1}
    return do_test_func1(ID, expected)


def test_func1_4(run=True):
    '''
    png_file = func1/in_4.png
    '''
    ID = 4
    expected = {(84, 231, 107): 2, (142, 154, 96): 5, (140, 86, 112): 3, (206, 155, 85): 5, (111, 237, 202): 2,
                (177, 177, 217): 6, (66, 251, 172): 4, (123, 237, 150): 3, (107, 129, 164): 2, (93, 113, 117): 1,
                (64, 133, 129): 3, (232, 235, 208): 3, (94, 95, 235): 1}
    return do_test_func1(ID, expected)

# ----------------------------------- FUNC. 2 ----------------------------------- #

def do_test_func2(ID, W, H, expected):
    txt_in  = f'func2/in_{ID}.txt'
    img_out = f'func2/your_image_{ID}.png'
    img_exp = f'func2/expected_{ID}.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run
    res = program.func2(txt_in, W, H, img_out)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il numero di diagUP e diagDOWN è sbagliato! / The values of diagUP e diagDOWN are incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    testlib.check_img_file(img_out, img_exp)
    return 2.5


def test_func2_1(run=True):
    '''
    txt_file = func2/in_1.txt
    output_imagefile = func2/your_image_1.png
    width = 30
    heigth = 30
    expected_imagefile = func2/expected_1.png
    '''
    ID = 1
    width = 30
    heigth = 30
    expected = (2, 1)
    return do_test_func2(ID, width, heigth, expected)


def test_func2_2(run=True):
    '''
    txt_file = func2/in_2.txt
    output_imagefile = func2/your_image_2.png
    width = 40
    heigth = 40
    expected_imagefile = func2/expected_2.png
    '''
    ID = 2
    width = 40
    heigth = 40
    expected = (3, 3)
    return do_test_func2(ID, width, heigth, expected)


def test_func2_3(run=True):
    '''
    txt_file = func2/in_3.txt
    output_imagefile = func2/your_image_3.png
    width = 60
    heigth = 50
    expected_imagefile = func2/expected_3.png
    '''
    ID = 3
    width = 60
    heigth = 50
    expected = (4, 6)
    return do_test_func2(ID, width, heigth, expected)


def test_func2_4(run=True):
    '''
    txt_file = func2/in_4.txt
    output_imagefile = func2/your_image_4.png
    width = 80
    heigth = 60
    expected_imagefile = func2/expected_4.png
    '''
    ID = 4
    width = 80
    heigth = 60
    expected = (7, 8)
    return do_test_func2(ID, width, heigth, expected)

# ----------------------------------- FUNC. 3 ----------------------------------- #

def do_test_func3(ID, color, expected):
    img_in  = f'func3/image0{ID}.png'
    img_out = f'func3/your_image0{ID}.png'
    img_exp = f'func3/expected0{ID}.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run
    res = program.func3(img_in, img_out, color)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] La lunghezza massima è sbagliata! / The maximum length is incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    testlib.check_img_file(img_out, img_exp)
    return 1.5


def test_func3_1(run=True):
    '''
    imagefile = func3/image01.png
    output_imagefile = func3/your_image01.png
    color = (255,0,0)
    '''
    ID = 1
    color = (255,0,0)
    expected = 55
    return do_test_func3(ID, color, expected)


def test_func3_2(run=True):
    '''
    imagefile = func3/image02.png
    output_imagefile = func3/your_image02.png
    color = (0,255,0)
    '''
    ID = 2
    color = (0,255,0)
    expected = 94
    return do_test_func3(ID, color, expected)


def test_func3_3(run=True):
    '''
    imagefile = func3/image03.png
    output_imagefile = func3/your_image03.png
    color = (100,160,200)
    '''
    ID = 3
    color = (100,160,200)
    expected = 56
    return do_test_func3(ID, color, expected)


def test_func3_4(run=True):
    '''
    imagefile = func3/image04.png
    output_imagefile = func3/your_image04.png
    color = (0,0,255)
    '''
    ID = 4
    color = (0,0,255)
    expected = 87
    return do_test_func3(ID, color, expected)

# ----------------------------------- FUNC. 4 ----------------------------------- #

def do_test_func4(ID, W, H, color, expected):
    txt_in  = f'func4/rect_0{ID}.txt'
    img_out = f'func4/out_0{ID}.png'
    img_exp = f'func4/expected_0{ID}.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run
    res = program.func4(W, H, color, txt_in, img_out)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] L'area totale è sbagliata! / The total area is incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    testlib.check_img_file(img_out, img_exp)
    return 1.5


def test_func4_1(run=True):
    '''
    L = 40
    A = 40
    sfondo = (0, 255, 0)
    file_rettangoli = func4/rect_01.txt
    imagefile_out = func4/out_01.png
    '''
    ID = 1
    L = A = 40
    color = (0,255,0)
    expected = 85
    return do_test_func4(ID, L, A, color, expected)


def test_func4_2(run=True):
    '''
    L = 60
    A = 40
    sfondo = (0, 0, 0)
    file_rettangoli = func4/rect_02.txt
    imagefile_out = func4/out_02.png
    '''
    ID = 2
    L = 60
    A = 40
    color = (0,0,0)
    expected = 484
    return do_test_func4(ID, L, A, color, expected)


def test_func4_3(run=True):
    '''
    L = 100
    A = 80
    sfondo = (255, 255, 255)
    file_rettangoli = func4/rect_03.txt
    imagefile_out = func4/out_03.png
    '''
    ID = 3
    L = 100
    A = 80
    color = (255,255,255)
    expected = 2668
    return do_test_func4(ID, L, A, color, expected)


def test_func4_4(run=True):
    '''
    L = 150
    A = 100
    sfondo = (255, 128, 0)
    file_rettangoli = func4/rect_04.txt
    imagefile_out = func4/out_04.png
    '''
    ID = 4
    L = 150
    A = 100
    color = (255,128,0)
    expected = 7101
    return do_test_func4(ID, L, A, color, expected)

################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,   # OK
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,   # OK
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,   # OK
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,   # OK
    test_personal_data_entry,
]


if __name__ == '__main__':
    if test_personal_data_entry() < 0:
        print(f"{COL['RED']}PERSONAL INFO MISSING. PLEASE FILL THE INITIAL VARS WITH YOUR NAME SURNAME AND STUDENT_ID{COL['RST']}")
        sys.exit()
    check_expected()
    testlib.runtests(   tests,
                        verbose=True,
                        logfile='grade.csv',
                        stack_trace=DEBUG)
    # esito finale: almeno 3 esercizi func risolti e punteggio totale >= 18
    testlib.check_exam_constraints()
################################################################################
