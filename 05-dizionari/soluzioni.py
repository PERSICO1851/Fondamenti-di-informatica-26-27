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
    cleaned = ''.join(c for c in string.lower() if c.isalnum() or c.isspace())
    words = cleaned.split()
    counts = {}
    # Soluzione lunga
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    # # Soluzione concisa
    # for word in words:
    #     counts[word] = counts.get(word, 0) + 1

    
    # Soluzione lunga
    # Ordiniamo tuple (frequenza, parola), così sorted ordina per frequenza
    # e, a parità di frequenza, per parola
    r = []
    for key, value in counts.items():
        r += [(value, key)]
    r = sorted(r)
    # Scambiamo gli elementi per ottenere tuple (parola, frequenza)
    result = []
    for value, key in r:
        result += [(key, value)]
    return result

    # Soluzione concisa
    # return sorted(counts.items(), key=lambda item: (item[1], item[0]))


# Scrivere una funzione che data una stringa di numeri interi separati da spazi,
# ritorna la lista ordinata dei numeri interi con frequenza massima.
def number_frequency(string: str) -> List[int]:
    numbers = [int(number) for number in string.split()]
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    max_count = max(counts.values())
    # Soluzione lunga
    r = []
    for number, count in counts.items():
        if count == max_count:
            r += [number]
    return sorted(r)    
    # Soluzione concisa
    #return sorted(number for number, count in counts.items() if count == max_count)

    # # Sfruttando la funzione implementata in precedenza
    # int_frequencies = word_frequency(string)
    # if not int_frequencies:
    #     return []
    # else:
    #     to_return = list()
    #     max_frequency = int_frequencies[-1][1]
    #     for integer, frequency in int_frequencies[::-1]:
    #         if frequency < max_frequency:
    #             break
    #         else:
    #             to_return.append(int(integer))
    # return sorted(to_return)


# Implementare una funzionalità equivalente a `dict.update()`, che data una
# lista di dizionari, ritorna un dizionario con tutte le chiavi presenti nei
# dizionari di input. Per valori, si usano i valori nei dizionari di input
# scegliendo quelli dei dizionari con indice superiore se presenti.
def update_dict(dictionaries: List[dict]) -> dict:
    result = {}
    for dictionary in dictionaries:
        for key, value in dictionary.items():
            result[key] = value
    return result

    # # Soluzione concisa
    # return {k: v for cur_dict in dictionaries for k, v in cur_dict.items()}


# Implementare una funzione che prende in input una lista di dizionari e ritorna
# un dizionario le cui chiavi sono le chiavi presenti nei due di input e come
# valori ritorna una lista con i valori presenti nei dizionari di input.
# Si possono usare i set.
def merge_dict(dictionaries: List[dict]) -> dict:
    keys = set()
    for dictionary in dictionaries:
        keys |= set(dictionary.keys())
    # Soluzione lunga
    r = {}
    for key in keys:
        for dictionary in dictionaries:
            if key in dictionary:
                if key in r:
                    r[key] += [dictionary[key]]
                else:
                    r[key] = [dictionary[key]]
    return r
    # Soluzione concisa
    #return {key: [dictionary[key] for dictionary in dictionaries if key in dictionary] for key in keys}

    # # Soluzione intermedia
    # to_return = dict()
    # for cur_dict in dictionaries:
    #     for k, v in cur_dict.items():
    #         to_return[k] = to_return.get(k, list()) + [v]
    # return to_return


# Implementare una funzione che prende in input una lista di dizionari e ritorna
# un dizionario le cui chiavi sono quelle presenti in tutti i dizionari e i cui
# valori sono la lista di valori delle relative chiavi. Si possono usare i set.
def intersect_dict(dictionaries: List[dict]) -> dict:
    keys = set(dictionaries[0].keys())
    for dictionary in dictionaries:
        keys &= set(dictionary.keys())
    # Soluzione lunga
    r = {}
    for key in keys:
        for dictionary in dictionaries:
            if key in r:
                r[key] += [dictionary[key]]
            else:
                r[key] = [dictionary[key]]
    return r
    # Soluzione concisa
    #return {key: [dictionary[key] for dictionary in dictionaries] for key in keys}

    # Usando la funzione implementata in precedenza
    # merged = merge_dict(dictionaries)
    # return {k: v for k, v in merged.items() if len(v) == len(dictionaries)}


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
