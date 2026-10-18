# Laboratorio 03 - Fondamenti di Programmazione
# Test, debug, stringhe e liste
#
# Il file è diviso in celle: ogni cella inizia con una riga "# %%".
# In Spyder (o VS Code) potete eseguire la cella in cui si trova il cursore
# con Ctrl+Invio, oppure con Maiusc+Invio per eseguirla e passare alla
# successiva. Potete anche eseguire tutto il file, come un normale programma.
# Eseguite per prima la cella "Funzioni per i test".
#
# Completate le funzioni indicate con TODO e usate i test per controllare
# il comportamento del vostro codice.


# %% Funzioni per i test
# Queste funzioni servono per eseguire i test.
# Per ora NON è necessario capire come sono implementate.

from typing import Any, Callable, List


def print_test(func: Callable, *args: List[Any]):
    func_str = func.__name__
    args_str = ", ".join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        print(f"{func_str}({args_str}) => {result_str}")
    except BaseException as error:
        error_str = repr(error)
        print(f"[ERRORE] {func_str}({args_str}) => {error_str}")


def check_test(func: Callable, expected: Any, *args: List[Any]):
    func_str = func.__name__
    args_str = ", ".join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        expected_str = repr(expected)

        if result == expected:
            print(f"[OK] {func_str}({args_str}) => {result_str}")
        else:
            print(
                f"[FALLITO] {func_str}({args_str}) "
                f"=> {result_str} | atteso: {expected_str}"
            )
    except BaseException as error:
        error_str = repr(error)
        print(f"[ERRORE] {func_str}({args_str}) => {error_str}")


# %% 1. Radice cubica
# Riprendiamo l'esercizio rimasto in sospeso.
#
# Scrivere una funzione che prende un numero e ne restituisce la radice cubica.
# Attenzione anche ai numeri negativi.

def cubic_root(n):
    # TODO
    value = n**(1/3) if n >= 0 else -(-n)**(1/3)
    return value


check_test(cubic_root, 2.0, 8)
print_test(cubic_root, -1)


# %% 2. Saluto
# Scrivere una funzione che restituisce:
#
#     Ciao <nome>. Buona giornata!
#
# Esempio:
# make_hello("Pippo") -> "Ciao Pippo. Buona giornata!"

def make_hello(name):
    phrase = f"Ciao {name}. Buona giornata!"
    return phrase


check_test(
    make_hello,
    "Ciao Pippo. Buona giornata!",
    "Pippo"
)


# %% 3. Stringhe: strip
# Scrivere una funzione che rimuove gli spazi all'inizio e alla fine
# della stringa.
#
# NON usare str.strip().
#
# Esempi:
# strip_whitespace("  Pippo  ") -> "Pippo"
# strip_whitespace("   ")       -> ""

def strip_whitespace(string):
    string = string.replace(" ","")
    return string


check_test(strip_whitespace, "Pippo", "  Pippo  ")
check_test(strip_whitespace, "", "   ")
check_test(strip_whitespace, "Pippo", "Pippo")


# %% 4. Liste: somma dei quadrati
# Restituire la somma dei quadrati degli elementi della lista.
#
# Esempio:
# sum_squares([1, 2, 3]) -> 14

def sum_squares(elements):
    
    return sum(x**2 for x in elements)


check_test(sum_squares, 14, [1, 2, 3])
check_test(sum_squares, 20, [2, 4])
check_test(sum_squares, 0, [])


# %% 5. Liste: massimo
# Restituire il massimo elemento della lista SENZA usare max().
#
# Se la lista è vuota, restituire None.

def max_element(elements):
    # TODO
    return sorted(elements)[-1] if elements != [] else None


check_test(max_element, 3, [1, 2, 3, -1, -2])
check_test(max_element, -1, [-1, -2])
check_test(max_element, None, [])


# %% 6. Liste: rimuovere i duplicati
# Restituire una NUOVA lista senza duplicati,
# mantenendo l'ordine della prima comparsa.
#
# Esempio:
# remove_duplicates([1, 2, 3, 2, 3]) -> [1, 2, 3]

def remove_duplicates(elements):
    g = []
    for y in elements:
        if y not in g:
            g.append(y)
    
    return g


check_test(
    remove_duplicates,
    [1, 2, 3],
    [1, 2, 3, 2, 3]
)

check_test(
    remove_duplicates,
    ["Harry", "Ron", "Luna"],
    ["Harry", "Ron", "Harry", "Luna"]
)


# %% 7. Liste: reverse
# Restituire una NUOVA lista con gli elementi in ordine inverso.
#
# NON usare reverse() o reversed().
#
# Esempio:
# reverse_list([1, 2, 3]) -> [3, 2, 1]

def reverse_list(elements):

    
    return elements[::-1]


check_test(reverse_list, [3, 2, 1], [1, 2, 3])


# %% 8. Challenge: split_string
# Affrontate questo esercizio dopo aver completato i precedenti.
#
# Scrivere una funzione che divide la stringa ogni volta che incontra
# uno dei caratteri contenuti in `characters`.
#
# NON usare str.split().
# NON restituire stringhe vuote.
#
# Esempi:
# split_string("Pippo Pluto", " ")   -> ["Pippo", "Pluto"]
# split_string("Pippo   Pluto", " ") -> ["Pippo", "Pluto"]
# split_string("uno,due;tre", ",;")  -> ["uno", "due", "tre"]

def split_string(string, characters):
    strings = []
    word = ""
    for i in string:
        if i in characters:
            if word != '':
                strings.append(word)
                word = ""
        else:
            word = word + i
    strings.append(word)
    return strings


check_test(
    split_string,
    ["Pippo", "Pluto"],
    "Pippo Pluto",
    " "
)

check_test(
    split_string,
    ["Pippo", "Pluto"],
    "Pippo   Pluto",
    " "
)

check_test(
    split_string,
    ["uno", "due", "tre"],
    "uno,due;tre",
    ",;"
)
# %%
