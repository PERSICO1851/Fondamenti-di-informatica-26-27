#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
#####################    ISTRUZIONI PER LA SIMULAZIONE.  ####################

PRIMA DI TUTTO: Assegna le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Aggiungi le tue implementazioni delle funzioni descritte sotto.
Per ottenere il punteggio esegui il file grade.py contenuto nella cartella.
Per superare la simulazione e' sufficiente ottenere un punteggio maggiore o uguale a 18.
"""

nome = "VINCENZO"
cognome = "PERSICOE"
matricola = "2235357"

################################################################################
################################################################################
################################################################################


################################################################################
# %% ----------------------------------- FUNC.1 ------------------------------ #
################################################################################
'''func1: 4 punti

Si definisca la funzione func1(a_dict, word) che prende in ingresso un
dizionario 'a_dict' e una parola 'word'. Ogni chiave del dizionario è
una stringa che ha una lista di stringhe come valore. La funzione deve
rimuovere da CIASCUNA lista di valori tutte le stringhe che hanno lo
stesso PRIMO e ULTIMO carattere della 'word' data, convertito in minuscolo.
La funzione restituisce il numero TOTALE di elementi rimossi da tutte
le liste del dizionario. Il dizionario 'a_dict' viene modificato.

Esempio:
a_dict = {'a':['alpha','beta','gamma'], 'b':['axle','zeta']}
word = 'aura'
a_dict_exp = {'a':['beta','gamma'], 'b':['axle','zeta']}
expected = 1
'''
def func1(a_dict: dict[str, list[str]], word: str) -> int:
    a = word[0].lower()
    b = word[-1].lower()
    counter = 0
    for v in a_dict.values():
        for y in v:
            if y[0].lower() == a and y[-1].lower() == b:
                v[v.index(y)] = 0
                counter += 1
        while 0 in v:
            v.remove(0)
            
    return counter

            


a_dict = {'a':['alpha','beta','gamma'], 'b':['axle','zeta']}
word = 'aura'
a_dict_exp = {'a':['beta','gamma'], 'b':['axle','zeta']}
expected = 1
print(func1(a_dict, 'aura')) # 1
print(a_dict) # {'a':['beta','gamma'], 'b':['axle','zeta']}

################################################################################
# %% -------------------------------- FUNC.2 --------------------------------- #
################################################################################
''' func2: 4 punti
Un dizionario D e' fornito come input. Le chiavi di D sono interi mentre
i valori sono liste di stringhe.

Scrivi la funzione func2(D) che costruisce e ritorna la lista W contenente
tutte le stringhe associate a ciascuna chiave K in D, tali che la lunghezza
della stringa sia STRETTAMENTE MINORE di K.

La lista W risultante deve essere ordinata per lunghezza DECRESCENTE.
In caso di parità di lunghezza, l'ordinamento è ALFABETICO DECRESCENTE.

Esempio:
dictionary = {4: ["a", "b", "c", "de", "fgh"], 2: ["a", "z", "b", "w"], 0: ["a", "b"]}
expected = ['fgh', 'de', 'z', 'w', 'c', 'b', 'b', 'a', 'a']
'''
def func2(D: dict[int, list[str]]) -> list[str]:
    W = []
    for key,values in D.items():
        print(key)
        for element in values:
            print(element)
            if len(element) < key:
                W.append(element)
    W.sort(key=lambda x: (len(x),x.lower()),reverse=True)
    return W



D = {4: ["a", "b", "c", "de", "fgh"], 2: ["a", "z", "b", "w"], 0: ["a", "b"]}
print(func2(D)) # ['fgh', 'de', 'z', 'w', 'c', 'b', 'b', 'a', 'a']

################################################################################
# %% -------------------------------- FUNC.3 --------------------------------- #
################################################################################
'''func3: 4 punti
Implementare la func3(strList) che:
- prende in input una lista di stringhe
- per ogni stringa, conta il numero di VOCALI (a, e, i, o, u, case-insensitive).
- restituisce una lista dei conteggi ottenuti, ordinati in base al loro
  valore, in ordine DECRESCENTE.
  
Esempio:
a_list = ["monkey", "cat", "panda", "alligator"]
expected = [4, 2, 2, 1]
'''
def func3(strList: list[str]) -> list[int]:
    W = []
    vocali = "aeiou"
    for y in strList:
        cont = 0
        for i in y.lower():
            if i in vocali:
                cont += 1
        W.append(cont)


    W.sort(reverse=True)
    return W

a_list = ["monkey", "cat", "panda", "alligator"]
print(func3(a_list)) # [4, 2, 2, 1]

################################################################################
# %% ----------------------------------- FUNC.4 ------------------------------ #
################################################################################
'''  func4: 6 punti

Si definisca una funzione func4(string_list1, string_list2) che prende
in ingresso due liste di stringhe e restituisce una nuova lista di
stringhe.
La nuova lista è costituita da tutte quelle stringhe presenti in
string_list1 ma NON in string_list2. (Differenza tra insiemi)

La lista risultante deve essere ordinata per numero di CARATTERI UNICI
(presenti nella stringa) CRESCENTE, in caso di parità, in ordine ALFABETICO CRESCENTE.

Esempio:
    string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant']
    string_list2=['ark', 'contact', 'hop', 'mark', 'shop', 'cat']
    expected = ['park', 'elephant', 'elichopter']

'''
def func4(string_list1: list[str], string_list2: list[str]) -> list[str]:
    expected = []
    for y in string_list1:
        if y not in string_list2:
            expected.append(y)
    expected.sort(key = lambda x:(len(set(x)),x))
    return expected

string_list1 = ['shop', 'park', 'elichopter', 'cat', 'elephant']
string_list2 = ['ark', 'contact', 'hop', 'mark', 'shop', 'cat']
print(func4(string_list1, string_list2)) # ['park', 'elephant', 'elichopter']

################################################################################
# %% -------------------------------- FUNC.5 --------------------------------- #
################################################################################
'''
func5: 8 punti

Scrivere una funzione func5(points) che prende in ingresso una lista
di coordinate (x,y) di N punti nel piano cartesiano (N >= 3).
Ogni punto è una coppia di numeri interi.

La funzione deve:
1. Trovare i TRE punti con la coordinata Y MASSIMA. Se ci sono più
   di tre punti con la Y massima, prendere i primi tre in ordine di 
   apparizione nella lista in input.
2. Calcolare il PUNTO MEDIANO (Mx, My) di questi tre punti.
   (Mx è la mediana delle 3 coordinate X, My è la mediana delle 3
    coordinate Y).
    
NOTA: la mediana tra più valori è il valore centrale tra i valori, ordinati (se dispari)
ovvero la media tra i due valori centrali (se pari)

La funzione restituisce una tupla (Mx, My) dove entrambi i valori
devono essere riportati con una precisione di 3 cifre decimali
(per farlo si può usare la funzione round).

Esempio:
    points = [(1, 5), (3, 2), (4, 5), (5, 1), (2, 4)]
    expected = (2, 5)
'''
def func5(points: list[tuple[int, int]]) -> tuple[float, float]:
    points.sort(key=lambda x:(x[1],points.count(x[1])),reverse=True)
    expected = points[:3]
    Mx = round(sum(x[0] for x in expected)/3)
    My = round(sum(x[1] for x in expected)/3)
    tpl = (Mx,My)
    



    return tpl

points = [(1, 5), (3, 2), (4, 5), (5, 1), (2, 4)]
print(func5(points)) # (2, 5)

################################################################################
# #%% ---------------------------- FUNC.6 ------------------------------------ #
################################################################################
'''
Func 6: 4 punti

Si definisca la funzione func6(text) che riceve come argomento:
- text: una stringa formata da parole separate da spazi e punteggiatura
e che ritorna un dizionario che ha:
  - come chiavi le CONSONANTI uniche presenti nel testo (minuscole)
  - come valore la FREQUENZA TOTALE di quella consonante nell'intero testo
    (case-insensitive).

Consonanti da considerare: b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z.

Esempio:
text = 'sOtto lA panca La caPra Canta Sopra LA Panca La CaPra crepa'
expected   = {'s': 2, 't': 3, 'l': 4, 'p': 6, 'n': 3, 'c': 6, 'r': 4}
'''
def func6(text: str) -> dict[str, int]:
    expected = {}
    consonanti = 'bcdfghjklmnpqrstvwxyz'
    text = text.lower().replace(' ', '')
    print(text)
    for y in text:
        if y in consonanti:
            expected[y] = text.count(y)
    return expected


text = 'sOtto lA panca La caPra Canta Sopra LA Panca La CaPra crepa'
print(func6(text)) # {'s': 2, 't': 3, 'l': 4, 'p': 6, 'n': 3, 'c': 6, 'r': 4}

# %%
