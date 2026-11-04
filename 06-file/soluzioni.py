# Ignorare le righe fino alla 31 (servono per eseguire i test)
from typing import Any, Callable, List, Tuple, Dict, Union
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Esegue un test e controlla il risultato
def check_test(func: Callable, expected: Any, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        expected_str = repr(expected)
        test_outcome = "superato" if (result == expected) else "fallito"
        color = bcolors.OKGREEN if (result == expected) else bcolors.FAIL
        print(f'{color}Test di {func_str} con input {args_str} {test_outcome}. Risultato: {result_str} Atteso: {expected_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'{bcolors.FAIL}ERRORE: {func_str}({args_str}) => {error_str}')


# Funzione di supporto
def load_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


# Dato il nome di un file di testo, ritornare il numero di volte che una parola
# e' presente nel file. La ricerca ignora la distinzione tra maiuscole e minuscole,
# e la punteggiatura.
def search_word(filename: str, word: str) -> int:
    text = load_file(filename)
    # Soluzione compatta
    #text = ''.join(character for character in text
    #               if character.isalnum() or character.isspace()).lower()
    #return text.split().count(word)
    # Soluzione prolissa
    r = ""
    for character in text:
        if character.isalnum() or character.isspace():
            r += character.lower()
    return r.split().count(word)


# Dato il nome di un file di testo, si ritorna una "tabella" formata da una
# lista di dizionari. Nel file, la prima riga contiene i nomi delle colonne
# (chiavi nel dizionario) e le righe contengono i valori, tutti separati da
# spazi.
def load_table(filename: str) -> List[Dict[str, str]]:
    lines = load_file(filename).splitlines()
    keys = lines[0].split()
    # Soluzione compatta
    #return [dict(zip(keys, line.split())) for line in lines[1:]]
    # Soluzione prolissa
    r = []
    for line in lines[1:]:
        d = {}
        values = line.split()
        for i in range(len(keys)):
            key = keys[i]
            value = values[i]
            d[key] = value
        r += [d]
    return r


# Caricare una tabella in modo simile al precente. In questo caso però, i valori
# che rappresentano numeri interi vanno convertiti in interi e non lasciati come
# stringhe.
def load_data(filename: str) -> List[Dict[str, Union[int, str]]]:
    lines = load_file(filename).splitlines()
    keys = lines[0].split()
    # Soluzione compatta
    #return [{key: int(value) if value.isdigit() else value for key, value in zip(keys, line.split())} for line in lines[1:]]
    # Soluzione prolissa
    r = []
    for line in lines[1:]:
        d = {}
        values = line.split()
        for i in range(len(keys)):
            key = keys[i]
            value = values[i]
            if value.isdigit():
                d[key] = int(value)
            else:
                d[key] = value
        r += [d]
    return r


# Caricare una tabella in modo simile al precente. In questo caso però, i valori
# sono separati da virgole e ci posso essere valori non presenti (due virgole
# consecutive). I valori mancanti devono essere aggiunti se `empties==True` come
# None, oppure essere omessi.
def load_csv(filename: str, empties: bool) -> List[Dict[str, Union[int, str, None]]]:
    lines = load_file(filename).splitlines()
    keys = lines[0].split(',')
    # Soluzione compatta
    #if empties:
    #    return [{key: int(value) if value.isdigit() else (value if value else None) for key, value in zip(keys, line.split(','))} for line in lines[1:]]
    #else:
    #    return [{key: int(value) if value.isdigit() else value for key, value in zip(keys, line.split(',')) if value} for line in lines[1:]]
    # Soluzione prolissa
    r = []
    for line in lines[1:]:
        d = {}
        values = line.split(',')
        for i in range(len(keys)):
            key = keys[i]
            value = values[i]
            if value.isdigit():
                d[key] = int(value)
            elif value:
                d[key] = value
            elif empties:
                d[key] = None
        r += [d]
    return r


# Dato una file CSV, che si carica con la funzione precedente, ritornare un
# dizionario con la somma dei valori di ogni colonna numerica.
# Usare la funzione load_csv(), con la variabile empties data a vostra scelta.
def column_stats(filename: str) -> Dict[str, Tuple[str, int]]:
    data = load_csv(filename, True)
    # Soluzione compatta
    #keys = {key for item in data
    #        for key, value in item.items() if isinstance(value, int)}
    #return {key: sum(item[key] for item in data if item[key]) for key in keys}
    # Soluzione prolissa
    keys = set()
    for item in data:        
        for key, value in item.items():
            if isinstance(value, int):
                keys.add(key)
    r = {}
    for item in data:                
        for key in keys:   
            if item[key]: 
                if key in r:               
                    r[key] += item[key]
                else:
                    r[key] = item[key]
    return r


# Test funzioni
check_test(search_word, 4, 'file01.txt', 'ciao')
check_test(search_word, 0, 'file01.txt', 'buon')
check_test(search_word, 1, 'file01.txt', 'buongiorno')
check_test(
    load_table, [{'Nome': "Luigi", "Telefono": '555-871612'},
                 {'Nome': "Mario", "Telefono": '555-826781'}], 'file02.txt')
check_test(
    load_data, [{'Nome': "Luigi", "Spese": 100},
                {'Nome': "Mario", "Spese": 1000}], 'file03.txt')
check_test(
    load_csv, [{'Nome': "Luigi", "Telefono": None, "Spese": 100, "Tasse": 10},
               {'Nome': "Mario", "Telefono": '555-1234', "Spese": 1000, "Tasse": None}], 'file04.csv', True)
check_test(
    load_csv, [{'Nome': "Luigi", "Spese": 100, "Tasse": 10},
               {'Nome': "Mario", "Telefono": '555-1234', "Spese": 1000}], 'file04.csv', False)
check_test(
    column_stats, {"Spese": 2100, "Tasse": 1011}, 'file05.csv')
