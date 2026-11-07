#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
1) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA
2) Completare le funzioni esA e esB e consegnare SOLO il file program.py

Il voto finale e' la somma dei punteggi dei problemi risolti.

Attenzione! DEBUG=True nel grade.py per visualizzare la stack trace degli errori.
"""

nome       = "LAZIO"
cognome    = "MERDA"
matricola  = "676767"

# ----------------------------------- EX.A ----------------------------------- #

"""EX. A: 5 punti

Si progetti una funzione che riceve come argomenti i path di due file,
file_in e file_out.  Il file file_in contiene testo libero, cioe' righe
di parole separate da spazi.

La funzione deve:
- contare quante parole ci sono in tutto il file file_in;
- scrivere in file_out, una per riga, tutte le parole di file_in
  diverse tra loro (senza ripetizioni), in ordine alfabetico;
- ritornare il numero totale di parole lette da file_in
  (contando anche le ripetizioni).

Esempio: se file_in contiene le righe
    gatto cane gatto
    pesce cane
allora file_out deve contenere (una parola per riga):
    cane
    gatto
    pesce
e la funzione deve ritornare 5.
"""

def esA(file_in: str, file_out: str) -> int:
    with open(file_in) as f:
        f_l = [parola for riga in f for parola in riga.split()]
    print(f_l)
    p_lette = len(f_l)
    f_l = list(set(f_l))
    f_l.sort()
    with open(file_out,'w') as f:
        for y in f_l:
            f.write(y+"\n")
        
    return p_lette
    # completa il codice della funzione
PATH = "/Users/persicovincenzo/Downloads/Simulazione01-test/esercizi_prova_simulazione2/"

print(esA(PATH +'esA/input_1.txt', PATH + 'esA/output_1.txt'))  # 5


# print(esA('esA/input_1.txt', 'esA/output_1.txt'))  # 5


# ----------------------------------- EX.B ----------------------------------- #

"""EX. B: 5 punti

Si scriva una funzione che riceve come argomento il percorso di un file
di testo contenente una matrice di interi NxM, con valori separati da spazi.

La funzione deve ritornare una lista contenente la somma degli elementi
di ciascuna riga della matrice, nello stesso ordine delle righe nel file.

Esempio: se il file contiene
    1 2 3
    4 5 6
    7 8 9
la funzione deve ritornare [6, 15, 24].
"""

def esB(input_filename: str) -> list[int]:
    with open(input_filename,'r') as f:
        lista = [sum([int(x) for x in riga.split()]) for riga in f]
    print(lista)
    return lista
    # completa il codice della funzione


print(esB('/Users/persicovincenzo/Downloads/Simulazione01-test/esercizi_prova_simulazione2/esB/input_1.txt'))  # [6, 15, 24]


# ---------------------------- EOF ---------------------------- #
