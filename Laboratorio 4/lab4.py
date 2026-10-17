# Fondamenti di Programmazione - Laboratorio 04
# Esercizi su tuple, liste, dizionari, funzioni e ordinamenti
# Dopo la Lezione 6, prima della Lezione 7
#
# Il file è diviso in celle: ogni cella inizia con una riga "# %%".
# In Spyder o VS Code usate Run Cell per eseguire una cella alla volta.
# Potete anche eseguire tutto il file come un normale programma.
# Eseguite per prima la cella "Funzioni per i test".
#
# Completate i TODO. `pass` è un segnaposto.
# Non usate lambda o comprehension: le vedremo nella prossima lezione.

# %% Funzioni per i test (eseguire per prima)
def print_test(func, *args):
    try:
        print(f"{func.__name__}{args!r} => {func(*args)!r}")
    except Exception as error:
        print(f"[ERRORE] {func.__name__}{args!r}: {error!r}")

def check_test(func, expected, *args):
    try:
        result = func(*args)
        status = "OK" if result == expected else "FALLITO"
        print(f"[{status}] {func.__name__}{args!r}: {result!r}; atteso {expected!r}")
    except Exception as error:
        print(f"[ERRORE] {func.__name__}{args!r}: {error!r}")


# %% Esercizio 1 - tuple_ex
# Data una tupla (x, y, z), restituire (z+1, x-1, y+2).
def tuple_ex(t):
    x,y,z = t
    t = (z+1, x-1, y+2)
    return t

check_test(tuple_ex, (3, -2, 1), (-1, -1, 2))

# %% Esercizio 2 - intersect
# Date due liste, restituire una nuova lista degli elementi presenti in entrambe. Conservare l'ordine di a e le ripetizioni presenti in a (se presenti).
def intersect(a, b):
    c = []
    for y in a:
        if y in b:
            c.append(y)
    return c

check_test(intersect, [2, 3], [1, 2, 3], [2, 3, 4])
check_test(intersect, [], [1, 2, 3], [10, 11])
check_test(intersect, [2, 2], [2, 2, 3], [2, 4])

# %% Esercizio 3 - frequency
# Data una lista di interi fra 0 e 99, restituire una lista di tuple (valore, frequenza) ordinata per valore crescente. Esempio: [5,4,1,4] -> [(1,1),(4,2),(5,1)].
def frequency(a):
    b = []
    for y in a:
        if y not in [item[0] for item in b]:
            b.append((y,a.count(y)))
    b.sort()

    return b

check_test(frequency, [(1, 1), (4, 2), (5, 1)], [5, 4, 1, 4])
check_test(frequency, [(0, 1), (23, 3), (99, 1)], [23, 99, 0, 23, 23])
check_test(frequency, [], [])

# %% Esercizio 4 - is_sorted (De Sensi)
# Restituire True se la lista e' gia' ordinata in ordine crescente O
# decrescente (ammettendo valori uguali consecutivi), False altrimenti.
# Usare UN SOLO ciclo, senza sort() o sorted(). Non modificare la lista.
def is_sorted(a):
    value = False
    vac1,vac2 = 0,0
    for y in range(len(a)-1):
        if a[y] >= a[y+1]:
            None
        else:
            vac1 += 1
        if a[y+1] >= a[y]:
            None
        else:
            vac2 += 1
    if vac2 == 0 or vac1 == 0:
        return True
    return value
    

check_test(is_sorted, True, [])
check_test(is_sorted, True, [1])
check_test(is_sorted, True, [1, 1, 1])
check_test(is_sorted, True, [1, 2, 3, 4])
check_test(is_sorted, True, [4, 3, 2, 1])
check_test(is_sorted, True, [1, 1, 2, 3, 3, 4])
check_test(is_sorted, True, [4, 4, 3, 2, 2, 1])
check_test(is_sorted, False, [1, 1, 3, 3, 2])
check_test(is_sorted, False, [4, 4, 3, 3, 5])


# %% Esercizio 5 - ordina_studenti
# Data una lista di tuple (nome, voto), restituire una NUOVA lista ordinata
# per voto decrescente e, a parita' di voto, nome crescente.
# Usare sorted() con una funzione criterio, SENZA lambda.
def fun(studenti):
    return -studenti[1],studenti[0]

def ordina_studenti(studenti):
    return sorted(studenti,key=fun)
    

    

check_test(ordina_studenti, [('Hermione', 30), ('Luna', 30), ('Harry', 27), ('Ron', 25)], [('Harry', 27), ('Luna', 30), ('Ron', 25), ('Hermione', 30)])
check_test(ordina_studenti, [], [])


# %% Esercizio 6 - is_palindrome (De Sensi)
# Restituire True se la lista si legge uguale nei due sensi.
# Anche la lista vuota e' palindroma.
def is_palindrome(a):
    if a == a[::-1]:
        return True
    else:
        return False

check_test(is_palindrome, True, [])
check_test(is_palindrome, True, [1])
check_test(is_palindrome, True, [1, 2, 8, 2, 1])
check_test(is_palindrome, True, [1, 2, 8, 8, 2, 1])
check_test(is_palindrome, False, [1, 3, 8, 8, 2, 1])


# %% CHALLENGE - check_pwd
# CHALLENGE (De Sensi): password lunga da 6 a 16 caratteri; almeno una minuscola, una maiuscola, una cifra e un carattere fra $#@; vietati altri caratteri.
def check_pwd(pwd):
    ch = '$#@;'
    ch_nt = '!?%*_-+=<>()[]{}.,:&^~|\\/'
    if not 6 <= len(pwd) <= 16:
        return False
    count1 = 0
    count2 = 0
    count3 = 0
    for y in pwd:
        if y.islower():
            count1 += 1
        if y.isupper():
            count2 += 1
        if y in ch:
            count3 += 1
        if y in ch_nt:
            return False
    if count1 == 0 or count2 == 0 or count3 == 0:
        return False
    return True
    
            


check_test(check_pwd, False, 'a')
check_test(check_pwd, False, 'Aa@09asng2/')
check_test(check_pwd, True, 'Aa@09asng2')

# ============================================================================
# ESERCIZI EXTRA PER CAS
# Da svolgere dopo gli esercizi del laboratorio.  I test sono forniti per verificare le soluzioni.
# ============================================================================

# %% EXTRA 1 - remove_avg (medio)
# Data una lista a di numeri >= 0, costruire una nuova lista con gli elementi
# a[i] che sono STRETTAMENTE maggiori del doppio della media degli elementi
# precedenti a[0:i]. Il primo elemento non va mai inserito.
# Esempio: [5, 3, 10, 0] -> [10], perche' 10 > 2 * media([5, 3]).
# Attenzione: la media e' calcolata sulla lista ORIGINALE, non sul risultato.
def remove_avg(a):
    b = []
    if a != []:
        for i in range(1,len(a)):
            media = sum(x for x in a[0:i])/len(a[0:i])
            if a[i] > media:
                b.append(a[i])
        return b
    else:
        return []

check_test(remove_avg, [10], [5, 3, 10, 0])
check_test(remove_avg, [20, 1000], [5, 20, 10, 1000])
check_test(remove_avg, [], [])


# %% EXTRA 2 - is_sorted_half (difficile)
# Restituire True se una lista di almeno 3 interi ha una prima parte
# strettamente crescente e una seconda strettamente decrescente,
# O viceversa, con un vero cambio di direzione interno.
# Le due parti non devono avere la stessa lunghezza.
# Usare UN SOLO ciclo; non usare sorted(), sort() o is_sorted().
# Esempi: [1, 3, 2]  ->True; [1, 2, 3] -> False.
def is_sorted_half(a):
    
    return

check_test(is_sorted_half, False, [1, 2, 3])
check_test(is_sorted_half, False, [3, 2, 1])
check_test(is_sorted_half, True, [1, 3, 2])
check_test(is_sorted_half, True, [3, 1, 2])
check_test(is_sorted_half, True, [1, 2, 5, 6, 8, 9, 3])
# %%
