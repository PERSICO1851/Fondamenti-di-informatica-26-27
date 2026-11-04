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
    with open(filename) as f:
        return sum(''.join(char for char in token.lower() if char.isalnum()) == word for token in f.read().split())


def load_(filename: str, entry_loader = lambda x: x.split()) -> List[Dict[str, str]]:
    with open(filename) as f:
        header = f.readline().split()
        return [dict(zip(header, entry_loader(entry))) for entry in f]


# Dato il nome di un file di testo, si ritorna una "tabella" formata da una
# lista di dizionari. Nel file, la prima riga contiene i nomi delle colonne
# (chiavi nel dizionario) e le righe contengono i valori, tutti separati da
# spazi.
def load_table(filename: str) -> List[Dict[str, str]]:
    # with open(filename) as f:
    #     header = f.readline().split()
    #     return [dict(zip(header, entry.split())) for entry in f]
    return load_(filename)


# Caricare una tabella in modo simile al precente. In questo caso però, i valori
# che rappresentano numeri interi vanno convertiti in interi e non lasciati come
# stringhe.
def load_data(filename: str) -> List[Dict[str, Union[int, str]]]:
    return load_(filename, lambda entry: [int(i) if i.isdigit() else i for i in entry.split() ])


# Caricare una tabella in modo simile al precente. In questo caso però, i valori
# sono separati da virgole e ci posso essere valori non presenti (due virgole
# consecutive). I valori mancanti devono essere aggiunti se `empties==True` come
# None, oppure essere omessi.
def load_csv(filename: str, empties: bool) -> List[Dict[str, Union[int, str, None]]]:
    with open(filename) as f:
        header = f.readline().strip().split(',')

        def handle_empties(entry, empties):
            to_return = list()
            for value in entry.strip().split(','):
                # print(f'val: {value}')
                if value.isdigit():
                    to_return.append(int(value))
                elif ((not value) or (not len(value))) and empties:
                    to_return.append(None)
                else:
                    to_return.append(value)
            return to_return
        return [dict(zip(header, handle_empties(entry, empties))) for entry in f]


# Dato una file CSV, che si carica con la funzione precedente, ritornare un
# dizionario con la somma dei valori di ogni colonna numerica.
# Usare la funzione load_csv(), con la variabile empties data a vostra scelta.
def column_stats(filename: str) -> Dict[str, Tuple[str, int]]:
    data = load_csv(filename, empties=False)
    keys = {k for entry in data for k, v in entry.items() if isinstance(v, int) }
    return {k:sum(entry[k] for entry in data  if isinstance(entry[k], int)) for k in keys}


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
load_csv('file04.csv', False)
# check_test(
#     load_csv, [{'Nome': "Luigi", "Telefono": None, "Spese": 100, "Tasse": 10},
#                {'Nome': "Mario", "Telefono": '555-1234', "Spese": 1000, "Tasse": None}], 'file04.csv', True)
# check_test(
#     load_csv, [{'Nome': "Luigi", "Spese": 100, "Tasse": 10},
#                {'Nome': "Mario", "Telefono": '555-1234', "Spese": 1000}], 'file04.csv', False)
check_test(
    column_stats, {"Spese": 2100, "Tasse": 1011}, 'file05.csv')
