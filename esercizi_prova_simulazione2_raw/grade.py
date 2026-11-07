# -*- coding: utf-8 -*-
import testlib, os
from testlib import my_print, COL, test_personal_data_entry

# Import the student's code
import program

###############################################################################
#### Mettete DEBUG=True per fare debug delle funzioni più facilmente attivando
#### la stack trace degli errori (più verbosa)
DEBUG = True
# DEBUG = False
###############################################################################

################################################################################
################################################################################
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################
################################################################################

################################################################################
# %% ---------------------- TEST SECTION -------------------
################################################################################

# ----------------------------------- EX. A ----------------------------------- #

def do_esA_tests(ID, expected_count, points):
    input_file    = f'esA/input_{ID}.txt'
    output_file   = f'esA/output_{ID}.txt'
    expected_file = f'esA/expected_{ID}.txt'

    # remove the previous output each time if it is there
    if os.path.exists(output_file):
        os.remove(output_file)

    res = program.esA(input_file, output_file)
    if res is None:
        raise testlib.NotImplemented()
    if res != expected_count:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato non è corretto! / Returned value is incorrect!\n'''
                 f'''[ERROR] Expected {expected_count} returned {res}\n{'*'*50}''')
        return 0
    testlib.check_text_file(output_file, expected_file)
    return points


def test_esA_1():
    '''
    input_file = esA/input_1.txt
    output_file = esA/output_1.txt
    expected count = 5
    '''
    return do_esA_tests(1, 5, 2)

def test_esA_2():
    '''
    input_file = esA/input_2.txt
    output_file = esA/output_2.txt
    expected count = 5
    '''
    return do_esA_tests(2, 5, 2)

def test_esA_3():
    '''
    input_file = esA/input_3.txt
    output_file = esA/output_3.txt
    expected count = 7
    '''
    return do_esA_tests(3, 7, 1)


# ----------------------------------- EX. B ----------------------------------- #

def do_esB_tests(ID, expected, points):
    input_file = f'esB/input_{ID}.txt'
    res = program.esB(input_file)
    if res is None:
        raise testlib.NotImplemented()
    testlib.checkList(res, expected)
    return points


def test_esB_1():
    '''
    input_file = esB/input_1.txt
    expected = [6, 15, 24]
    '''
    return do_esB_tests(1, [6, 15, 24], 2)

def test_esB_2():
    '''
    input_file = esB/input_2.txt
    expected = [9, 0, 3]
    '''
    return do_esB_tests(2, [9, 0, 3], 2)

def test_esB_3():
    '''
    input_file = esB/input_3.txt
    expected = [5, 8]
    '''
    return do_esB_tests(3, [5, 8], 1)


################################################################################
# %% --------------------- TESTS ---------------------
tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_esA_1, test_esA_2, test_esA_3,
    test_esB_1, test_esB_2, test_esB_3,
    test_personal_data_entry,
]

# %% --------------------- MAIN ---------------------
if __name__ == '__main__':
    test_personal_data_entry()
    # Check that input files have not been changed
    testlib.check_expected()
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)

################################################################################
# %% --------------------- END OF FILE ---------------------
