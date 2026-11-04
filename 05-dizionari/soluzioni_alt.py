# Ignorare le righe fino alla 31 (servono per eseguire i test)
from typing import Any, Callable, List, Tuple
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


# Scrivere una funzione che data una stringa, ritorna una lista di tuple
# (parola, frequenza), ordinata per frequenza crescente e, a parità di
# frequenza, in ordine alfabetico. La frequenza è il numero di volte in cui
# la parola appare nel testo.
# Per evitare problemi nel trovare le parole, togliere tutti i caratteri
# non alfanumerici, a parte gli spazi, e convertire le parole in minuscolo.
# Usare la funzione `isalnum()` per testare i caratteri.
def word_frequency(string: str) -> List[Tuple[str, int]]:
    string = ''.join(character for character in string if character.isalnum() or character == ' ').lower()
    tokens = string.split()
    token_counts = dict()
    for token in tokens:
        token_counts[token] = token_counts.get(token, 0) + 1
    return sorted(token_counts.items(), key=lambda x: (x[1], x[0]))


# Scrivere una funzione che data una stringa di numeri interi separati da spazi,
# ritorna la lista ordinata dei numeri interi con frequenza massima.
def number_frequency(string: str) -> List[int]:
    int_frequencies = word_frequency(string)
    if not int_frequencies:
        return []
    else:
        to_return = list()
        max_frequency = int_frequencies[-1][1]
        for integer, frequency in int_frequencies[::-1]:
            if frequency < max_frequency:
                break
            else:
                to_return.append(int(integer))
    return sorted(to_return)


# Implementare una funzionalità equivalente a `dict.update()`, che data una
# lista di dizionari, ritorna un dizionario con tutte le chiavi presenti nei
# dizionari di input. Per valori, si usano i valori nei dizionari di input
# scegliendo quelli dei dizionari con indice superiore se presenti.
def update_dict(dictionaries: List[dict]) -> dict:
    return {k: v for cur_dict in dictionaries for k, v in cur_dict.items()}


# Implementare una funzione che prende in input una lista di dizionari e ritorna
# un dizionario le cui chiavi sono le chiavi presenti nei due di input e come
# valori ritorna una lista con i valori presenti nei dizionari di input.
# Si possono usare i set.
def merge_dict(dictionaries: List[dict]) -> dict:
    to_return = dict()
    for cur_dict in dictionaries:
        for k, v in cur_dict.items():
            to_return[k] = to_return.get(k, list()) + [v]
    return to_return


# Implementare una funzione che prende in input una lista di dizionari e ritorna
# un dizionario le cui chiavi sono quelle presenti in tutti i dizionari e i cui
# valori sono la lista di valori delle relative chiavi. Si possono usare i set.
def intersect_dict(dictionaries: List[dict]) -> dict:
    merged = merge_dict(dictionaries)
    return {k: v for k, v in merged.items() if len(v) == len(dictionaries)}


# Test funzioni
check_test(word_frequency, [("ciao", 1), ("pippo", 1)], "Ciao Pippo")
check_test(word_frequency, [("pluto", 1), ("pippo", 2)], "Pippo Pluto Pippo")
check_test(word_frequency, [('pippo', 1), ('pluto', 1),
                            ('ciao', 2)], "Ciao Pippo! Ciao Pluto!")
check_test(word_frequency, [('pippo', 1), ('pluto', 1)], "Pluto Pippo")
check_test(number_frequency, [10], "1 2 2 3 10 10 10")
check_test(number_frequency, [2, 5], "1 1 5 5 5 2 2 2")
check_test(update_dict, {'Ciao': 1, 'Pippo': 2, 'Pluto': 3},
           [{"Ciao": 1, "Pippo": 2}, {"Pluto": 3}])
check_test(update_dict, {'Ciao': 1, 'Pippo': 4, 'Pluto': 3}, [{
    "Ciao": 1, "Pippo": 2}, {"Pluto": 3, "Pippo": 4}])
check_test(merge_dict, {'Ciao': [1], 'Pippo': [2], 'Pluto': [3]},
           [{"Ciao": 1, "Pippo": 2}, {"Pluto": 3}])
check_test(merge_dict, {'Ciao': [1], 'Pippo': [2, 4], 'Pluto': [3]}, [{
    "Ciao": 1, "Pippo": 2}, {"Pluto": 3, "Pippo": 4}])
check_test(intersect_dict, {'Pippo': [2, 3]},
           [{"Ciao": 1, "Pippo": 2}, {"Pippo": 3, "Pluto": 4}])
check_test(intersect_dict, {'Pippo': [2, 3], 'Pluto': [5, 4]},
           [{"Ciao": 1, "Pippo": 2, "Pluto": 5}, {"Pippo": 3, "Pluto": 4}])
