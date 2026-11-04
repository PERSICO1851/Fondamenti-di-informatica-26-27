#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fondamenti di Programmazione — Laboratorio 05, canale M-Z.

La prima parte del laboratorio e' dedicata alla correzione guidata
della simulazione: le soluzioni vengono discusse in aula.

Completare le funzioni seguenti al posto di pass.
Eseguire: python3 Laboratorio05_STUDENTI.py
I test mostrano OK o DA RIVEDERE, ma non attribuiscono voti.
File di input da tenere nella stessa directory di lavoro dello script.
"""

def verifica(nome, funzione, atteso, *argomenti):
    try:
        ottenuto = funzione(*argomenti)
        esito = 'OK' if ottenuto == atteso else 'DA RIVEDERE'
        print(f'[{esito}] {nome}: ottenuto={ottenuto!r}, atteso={atteso!r}')
    except Exception as errore:
        print(f'[ERRORE] {nome}: {type(errore).__name__}: {errore}')

# ESERCIZIO COMPREHENSION (da svolgere senza definire funzioni):
# numeri = [3, 4, 7, 8, 10, 11]
# A) Con for/if e poi con list comprehension, ottenere [16, 64, 100].
# parole = ['Harry', 'Ron', 'Hermione', 'Luna', 'Hagrid']
# B) Con for/if e poi con dict comprehension, ottenere il dizionario
#    delle lunghezze per le sole parole con almeno 5 caratteri.
# C) Challenge: dal dizionario voti {'Harry':25,'Hermione':30,
#    'Ron':16,'Luna':28} tenere solo i promossi, con valore 'superato'.


# ======================================================================
# word_frequency
# Riceve una stringa e restituisce un dizionario parola -> frequenza.
# Ignorare maiuscole/minuscole. Ogni carattere NON alfanumerico e'
# un separatore: per esempio "Ciao,mondo!" contiene due parole.
# Testo senza parole -> {}. Non modificare l'input.
def word_frequency(testo: str) -> dict[str, int]:
    pass

# ======================================================================
# number_frequency
# Riceve una stringa con interi separati da spazi. Restituisce una
# lista crescente dei numeri con frequenza massima (tutti in caso
# di parita'). Stringa vuota -> [].
def number_frequency(testo: str) -> list[int]:
    pass

# ======================================================================
# update_dict
# Riceve una lista di dizionari e restituisce un nuovo dizionario.
# Se una chiave appare piu' volte, prevale il valore dell'ultimo
# dizionario. Non modificare gli input. Lista vuota -> {}.
def update_dict(dizionari: list[dict]) -> dict:
    pass

# ======================================================================
# merge_dict
# Riceve una lista di dizionari. Per ogni chiave, costruire una lista
# con tutti i valori incontrati, nell'ordine dei dizionari.
# Lista vuota -> {}. Non modificare gli input.
def merge_dict(dizionari: list[dict]) -> dict:
    pass

# ======================================================================
# conta_righe_non_vuote
# Riceve il percorso di un file UTF-8 esistente. Restituisce il numero
# di righe che contengono almeno un carattere diverso dagli spazi.
# Ignorare righe vuote e righe composte solo da spazi/tab.
# File vuoto -> 0.
def conta_righe_non_vuote(percorso: str) -> int:
    pass

# FACOLTATIVI / PER CASA
# salva_parole_frequenti(percorso_in, percorso_out, soglia):
#   leggere parole come in file_frequency, scrivere in ordine alfabetico
#   le parole con frequenza >= soglia, una per riga nel formato
#   parola,frequenza; restituire il numero di parole scritte.

def salva_parole_frequenti(percorso_in: str, percorso_out: str, soglia: int) -> int:
    pass

# intersect_dict(dizionari): assumere una lista NON vuota di dizionari;
#   tenere solo le chiavi comuni a tutti, associando la lista dei valori
#   nell'ordine dei dizionari. Non modificare gli input.
def intersect_dict(dizionari: list[dict]) -> dict:
    pass

# ======================================================================
# file_frequency
# Riceve il percorso di un file UTF-8 esistente contenente UNA parola
# non vuota per riga. Restituisce le frequenze senza distinguere
# maiuscole/minuscole. Usare strip() e lower(). File vuoto -> {}.
# Precondizione: tutte le righe sono parole non vuote.
def file_frequency(percorso: str) -> dict[str, int]:
    pass


# ======================================================================
# FACOLTATIVO DOPO LA LEZIONE 10 — load_table
# Il file UTF-8 contiene un'intestazione con nomi di colonne separati
# da virgole, poi righe con lo stesso numero di valori separati da virgole.
# Restituire una lista di dizionari (chiave = nome colonna, valore = testo).
# Non convertire i numeri. File con sola intestazione -> [].
# Esempio: nome,voto / Harry,25 -> [{'nome':'Harry','voto':'25'}].
def load_table(percorso: str) -> list[dict[str, str]]:
    pass

if __name__ == '__main__':
    verifica('word_frequency', word_frequency, {'harry': 2, 'e': 2, 'ron': 1, 'hermione': 1}, 'Harry e Ron, Harry e Hermione!')
    verifica('word_frequency', word_frequency, {'ciao': 1, 'mondo': 1}, 'Ciao,mondo!')
    verifica('word_frequency', word_frequency, {}, '...')
    verifica('number_frequency', number_frequency, [10], '1 2 2 3 10 10 10')
    verifica('number_frequency', number_frequency, [2, 5], '1 1 5 5 5 2 2 2')
    verifica('number_frequency', number_frequency, [], '')
    verifica('number_frequency', number_frequency, [-2, 3], '-2 3 -2 3')
    verifica('update_dict', update_dict, {'a':3,'b':2,'c':4}, [{'a':1,'b':2},{'a':3,'c':4}])
    verifica('update_dict', update_dict, {}, [])
    verifica('merge_dict', merge_dict, {'a':[1,3],'b':[2],'c':[4]}, [{'a':1,'b':2},{'a':3,'c':4}])
    verifica('merge_dict', merge_dict, {}, [])
    verifica('file_frequency', file_frequency, {'harry':2,'ron':2,'luna':1}, 'parole_l05.txt')
    verifica('file_frequency', file_frequency, {}, 'parole_vuote_l05.txt')
    verifica('conta_righe_non_vuote', conta_righe_non_vuote, 4, 'righe_l05.txt')
    verifica('conta_righe_non_vuote', conta_righe_non_vuote, 0, 'parole_vuote_l05.txt')
    # Esempio di output facoltativo da verificare dopo l'implementazione:
    # salva_parole_frequenti('parole_l05.txt', 'frequenti_l05.txt', 2)
    # Facoltativo dopo L10:
    # verifica('load_table', load_table, [{'nome':'Harry','voto':'25'}, {'nome':'Hermione','voto':'30'}], 'tabella_l05.txt')
