#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Simulazione 2 M-Z: correttore basato su testlib.py (32 punti)."""
import copy
from pathlib import Path
import traceback
import program
import testlib

DEBUG = True
ROOT = Path(__file__).resolve().parent

CASES2 = [
    ([('cat',[7,3]),('dog',[1,4,7]),('cat',[2,7])], {1:['dog'],2:['cat'],3:['cat'],4:['dog'],7:['cat','dog']}),
    ([], {}),
    ([('a',[1,1]),('a',[1]),('b',[1,2])], {1:['a','b'],2:['b']}),
    ([('z',[-1,0]),('x',[0]),('a',[-1])], {-1:['a','z'],0:['x','z']}),
]
CASES3 = [
    ([('Luna',28,2),('Ron',16,0),('Harry',28,1),('Hermione',30,4),('Neville',28,1)], [('Harry',28),('Neville',28),('Luna',28)]),
    ([], []),
    ([('A',18,3),('B',18,4),('C',17,0)], [('A',18)]),
    ([('Z',30,1),('A',30,1),('Z',30,1)], [('A',30),('Z',30),('Z',30)]),
]
CASES4 = [
    ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [[12,8,4],[11,7,3],[10,6,2],[9,5,1]]),
    ([[1]], [[1]]),
    ([[1,2,3]], [[3],[2],[1]]),
    ([[1],[2],[3]], [[3,2,1]]),
    ([[1,2],[3,4]], [[4,2],[3,1]]),
]
CASES5 = [
    (5,'as',['elephant','cobra','horse','panda','snake']),
    (2,'z',[]),
    (3,'a',['aba','aba','bab']),
    (2,'A',['Aa','aA']),
    (0,'e',['three','one']),
    (0,'',[]),
    (4,'ap',['apricot','apple','pear','pear']),
]


def check_value(actual, expected):
    assert type(actual) is type(expected), f'Tipo errato: {type(actual).__name__}, atteso {type(expected).__name__}'
    testlib.check(actual, expected)


def verify_unchanged(original, snapshot):
    assert original == snapshot, 'La funzione ha modificato il parametro di ingresso'


def verify_files_unchanged():
    # La libreria ufficiale controlla le copie di backup degli input e degli expected.
    testlib.check_expected()


def make_test(fn, case_index, weight, runner):
    def test():
        runner(case_index)
        return weight
    test.__name__ = f'test_{fn}_{case_index:02}'
    return test


def run_func1(i):
    fi=ROOT/'func1'/f'input_{i:02}.txt'
    fo=ROOT/'func1'/f'output_{i:02}.txt'
    expected=ROOT/'func1'/f'expected_{i:02}.txt'
    fo.unlink(missing_ok=True)
    value=program.func1(str(fi),str(fo))
    check_value(value,[12,1,6,6,4][i-1])
    assert fo.is_file(), 'File di output non creato'
    assert fo.read_bytes()==expected.read_bytes(), 'Contenuto del file di output non corretto'
    verify_files_unchanged()


def run_memory(fn, cases, i):
    source,expected=cases[i-1]
    arg=copy.deepcopy(source)
    snapshot=copy.deepcopy(arg)
    value=getattr(program,fn)(arg)
    check_value(value,expected)
    verify_unchanged(arg,snapshot)


def run_func5(i):
    fi=ROOT/'func5'/f'input_{i:02}.txt'
    fo=ROOT/'func5'/f'output_{i:02}.txt'
    expected=ROOT/'func5'/f'expected_{i:02}.txt'
    fo.unlink(missing_ok=True)
    length,chars,result=CASES5[i-1]
    value=program.func5(str(fi),str(fo),length,chars)
    check_value(value,result)
    assert fo.is_file(), 'File di output non creato'
    assert fo.read_bytes()==expected.read_bytes(), 'Contenuto del file di output non corretto'
    verify_files_unchanged()


def main():
    import os
    os.chdir(ROOT)  # backup paths in testlib are relative to the working directory
    verify_files_unchanged()
    tests=[]
    for i in range(1,6): tests.append(make_test('func1',i,1.2,run_func1))
    for fn,cases,weight in [('func2',CASES2,1.5),('func3',CASES3,1.5),('func4',CASES4,1.2)]:
        for i in range(1,len(cases)+1):
            tests.append(make_test(fn,i,weight,lambda j, fn=fn, cases=cases: run_memory(fn,cases,j)))
    for i in range(1,8): tests.append(make_test('func5',i,8/7,run_func5))
    testlib.runtests(tests, logfile='grade.csv', stack_trace=DEBUG)
    verify_files_unchanged()
    import csv
    with open('grade.csv', newline='', encoding='utf-8') as f:
        scores=[(row[0],float(row[1])) for row in csv.reader(f)]
    total=sum(v for _,v in scores)
    print(f'\nPUNTEGGIO TOTALE: {total:.2f}/32')
    print('SOGLIA 18:', 'RAGGIUNTA' if total>=18-1e-9 else 'NON RAGGIUNTA')
    return total

if __name__=='__main__':
    main()
