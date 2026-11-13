#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SECONDA SIMULAZIONE - 11 NOVEMBRE 2026 - CANALE M-Z
Prima di iniziare compilare nome, cognome e matricola.
Implementare SOLO le funzioni indicate, senza cambiarne firma o nome.
Eseguire python grade.py nella stessa cartella per verificare il punteggio.
Punteggio massimo 32; soglia ordinaria 18/32.
Consegnare soltanto program.py secondo le indicazioni pubblicate su Classroom.
I file di input sono forniti; le funzioni non devono modificarli.
"""
nome = "incenzo"
cognome = "persico"
matricola = "22445485"


# ------------------ FUNC1 ------------------
"""func1: 6 punti

Si definisca la funzione func1(input_file, output_file) che riceve come
argomenti due stringhe, corrispondenti ai percorsi di due file di testo.

Il file input_file contiene una matrice rettangolare non vuota di numeri
interi: ogni riga del file rappresenta una riga della matrice e i valori
sono separati da virgole, con eventuali spazi.

La funzione deve leggere la matrice e scriverla nel file output_file,
rappresentando ciascuna riga come una lista Python di interi. Ogni lista
deve occupare una riga del file di output. La funzione deve inoltre
restituire il numero totale di elementi della matrice.

Il file di input non deve essere modificato.

Esempio: se input_file contiene

    1,    2, 3,       25
    4, 5,      6, 17
    7,   8,    9,     42

il file output_file deve contenere

    [1, 2, 3, 25]
    [4, 5, 6, 17]
    [7, 8, 9, 42]

e la funzione deve restituire 12."""

def func1(input_file: str, output_file: str) -> int:
    with open(input_file) as f:
        letti = f.read()
        lista = [[int(y) for y in x.split(",")] for x in letti.splitlines()]
    with open(output_file,'w') as f:
        for y in lista:
            f.write(str(y) + "\n")
    return sum(len(x) for x in lista)
# ------------------ FUNC2 ------------------
"""func2: 6 punti

Si definisca la funzione func2(list_A) che riceve una lista di tuple.
Ogni tupla contiene una stringa e una lista di numeri interi.

La funzione deve restituire un dizionario le cui chiavi sono tutti gli
interi presenti nelle liste contenute nelle tuple di list_A. A ciascuna
chiave deve essere associata la lista delle stringhe che compaiono in
una tupla contenente quell'intero.

Le stringhe associate a una stessa chiave non devono essere ripetute
e devono essere ordinate alfabeticamente in senso crescente.
La lista originale non deve essere modificata.

Esempio: se

    list_A = [
        ('cat', [7, 3]),
        ('dog', [1, 4, 7]),
        ('cat', [2, 7])
    ]

la funzione deve restituire

    {
        1: ['dog'],
        2: ['cat'],
        3: ['cat'],
        4: ['dog'],
        7: ['cat', 'dog']
    }"""

def func2(list_A: list[tuple[str,list[int]]]) -> dict[int,list[str]]:
    diz = {key:[] for lista in list_A for key in lista[1]}
    for y in list_A:
        for i in y[1]:
            if y[0] not in diz[i]:
                diz[i].append(y[0])
    diz = dict(sorted(diz.items()))
    for y in diz.values():
        y.sort()
    
    return diz

# ------------------ FUNC3 ------------------
"""func3: 6 punti

Si definisca la funzione func3(studenti) che riceve una lista di tuple
(nome, voto, assenze), dove nome e' una stringa e voto e assenze sono
interi non negativi.

La funzione deve restituire una nuova lista contenente soltanto gli
studenti con voto almeno 18 e non piu' di 3 assenze. Ogni elemento
della lista restituita deve essere una tupla (nome, voto), senza il
numero delle assenze.

Gli studenti selezionati devono essere ordinati per voto decrescente;
a parita' di voto, per numero di assenze crescente; a ulteriore
parita', per nome in ordine alfabetico crescente.

Le eventuali ripetizioni devono essere mantenute. La lista originale
non deve essere modificata. Se nessuno studente soddisfa le condizioni,
la funzione deve restituire una lista vuota.

Esempio: se

    studenti = [
        ('Luna', 28, 2),
        ('Ron', 16, 0),
        ('Harry', 28, 1),
        ('Hermione', 30, 4),
        ('Neville', 28, 1)
    ]

la funzione deve restituire

    [
        ('Harry', 28),
        ('Neville', 28),
        ('Luna', 28)
    ]"""

def func3(studenti: list[tuple[str,int,int]]) -> list[tuple[str,int]]:
    # scrivi qui il tuo codice
    if studenti == []:
        return []
    lista = sorted([(x[0],x[1],x[2]) for x in studenti if x[1] >= 18 and 3 >= x[2]],key= lambda x: (x[1],x[2],x[0]))
    lista = [(x[0],x[1]) for x in lista]
    return lista

# ------------------ FUNC4 ------------------
"""func4: 6 punti

Si definisca la funzione func4(matrix) che riceve una matrice
rettangolare non vuota di numeri interi, rappresentata come lista di
liste. Tutte le righe hanno la stessa lunghezza e contengono almeno
un elemento.

La funzione deve restituire una nuova matrice ottenuta riflettendo
quella originale rispetto alla diagonale secondaria, cioe' quella
che va dall'angolo in alto a destra all'angolo in basso a sinistra.
La matrice originale non deve essere modificata.

Esempio: se la matrice in ingresso e' (3 righe e 4 colonne)

    matrix = [
  0   [1,  2,  3,  4], [0,3] -* [0,2], [0,2]-* [1,2]
  1   [5,  6,  7,  8], [1,3] -* [0,1], [1,2]   [1,1]
  2   [9, 10, 11, 12] [2,3] -* [0,0] , [2,2]   [1,0]   
    ]
       0  1   2   3
la funzione deve restituire la seguente matrice (4 righe e 3 colonne):

    [
        [12, 8, 4],
        [11, 7, 3],
        [10, 6, 2],
        [ 9, 5, 1]
    ]"""

def func4(matrix: list[list[int]]) -> list[list[int]]:
    # scrivi qui il tuo codice
    colonna = len(matrix[0])
    righe = len(matrix)
    matrice = [[[] for i in range(righe)] for i in range(colonna)]
    for i in range(righe):
        for y in range(colonna):
            matrice[colonna-1-y][righe-i-1] = matrix[i][y]



    return matrice

# ------------------ FUNC5 ------------------
"""func5: 8 punti

Si definisca la funzione func5(file_in, file_out, length, chars) che
riceve come argomenti i percorsi di due file di testo, un intero
non negativo length e una stringa chars, che puo' anche essere vuota.

Il file file_in contiene parole separate da spazi, tabulazioni o
caratteri di a capo. La funzione deve selezionare tutte le parole
che hanno lunghezza almeno length e contengono almeno uno dei
caratteri presenti nella stringa chars.

Le parole selezionate devono essere ordinate per lunghezza decrescente
e, a parita' di lunghezza, in ordine alfabetico crescente. Le eventuali
ripetizioni devono essere mantenute e il confronto deve distinguere
maiuscole e minuscole.

La funzione deve restituire la lista delle parole ordinate e scrivere
le stesse parole nel file file_out, separate da un solo spazio,
senza richiedere un a capo finale. Se non viene selezionata alcuna
parola, deve restituire [] e creare un file di output vuoto.

Esempio: se file_in contiene

    panda snake cobra horse tulip

e length = 5 e chars = 'as', la funzione deve restituire

    ['cobra', 'horse', 'panda', 'snake']

e scrivere in file_out il testo

    cobra horse panda snake"""

def func5(file_in: str, file_out: str, length: int, chars: str) -> list[str]:
    # scrivi qui il tuo codice
    with open(file_in) as f:
        lett = f.read()
        parole = lett.split()
        parole = sorted([x for x in parole if len(x) >= length and any(c in x for c in chars)],key= lambda x:(-len(x),x))
    with open(file_out,'w') as f:
        f.write(" ".join(parole))

        
    return parole
