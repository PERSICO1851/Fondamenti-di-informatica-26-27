#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fondamenti di Programmazione - Laboratorio 06, canale M-Z.

Usare VS Code: completare le funzioni e avviare questo file dalla cartella
che contiene images.py, studenti.csv, voti.csv, vuoto.csv e img_esercizi.png.
Dipendenza per il modulo didattico images.py: python -m pip install pypng

PARTE A: CSV e tabelle (L11)
PARTE B: immagini RGB dopo L12
PARTE C: trasformazioni geometriche dopo L13 (esercizi 6-9)
PARTE D: approfondimenti facoltativi (esercizi 10-11)

I test sono simili a quelli d'esame, ma non assegnano punteggi.
"""
import images


def verifica(nome, funzione, atteso, *argomenti):
    try:
        ottenuto = funzione(*argomenti)
        print('[OK]' if ottenuto == atteso else '[DA RIVEDERE]', nome,
              '| ottenuto:', repr(ottenuto))
    except Exception as errore:
        print('[ERRORE]', nome, type(errore).__name__, str(errore))


def verifica_png(nome, funzione, output, atteso):
    try:
        funzione('img_esercizi.png', output)
        ottenuto = images.load(output)
        print('[OK]' if ottenuto == atteso else '[DA RIVEDERE]', nome,
              '| output:', output)
    except Exception as errore:
        print('[ERRORE]', nome, type(errore).__name__, str(errore))



# === PARTE A - FILE CSV E TABELLE (DOPO LEZIONE 11) ===


# ESERCIZIO 1 - seleziona_studenti (6 punti)
# Il file input_file e' un CSV con intestazione nome,voto,corso.
# Scrivere in output_file un CSV con intestazione nome,voto contenente
# gli studenti del corso richiesto con voto almeno pari a soglia,
# ordinati per voto decrescente e, a parita', per nome crescente.
# Restituire il numero di studenti scritti. Ignorare le righe vuote.
# Se nessuno soddisfa i criteri, scrivere soltanto l'intestazione.
# Esempio: seleziona_studenti('studenti.csv', 'out.csv', 'Python', 25).
def seleziona_studenti(input_file: str, output_file: str, corso: str, soglia: int) -> int:
    with open(input_file) as f:
        st = [x.split(",") for x in f.read().splitlines() if x.split(",") != [""]]
        studenti_isc = len(st) - 1
        intestazione = st.pop(0)
        st = sorted([(x[0],int(x[1])) for x in st if int(x[1]) >= soglia and x[2] == corso ],key= lambda x: (-x[1],x[0]))
    with open(output_file,"w") as f:
        if st == [""]:
            f.write(f"{intestazione[0]},{intestazione[1]}")
            return 0
        f.write(f"{intestazione[0]},{intestazione[1]}")
        f.write("\n")
        for x in st:
            f.write(f"{x[0]},{x[1]}")
            f.write("\n")
            
    return len(st)


# ESERCIZIO 2 - report_quantita (6 punti)
# Il file input_file contiene righe nel formato nome,quantita, senza
# intestazione. La quantita' e' un intero, anche negativo, e uno stesso
# nome puo' comparire piu' volte.
# Creare output_file con intestazione nome,totale e, per ogni nome
# distinto, la somma delle quantita' associate, in ordine alfabetico.
# Restituire il numero di nomi distinti e ignorare le righe vuote.
# Se l'input e' vuoto, scrivere soltanto l'intestazione e restituire 0.
# Esempio: mele,5 / pere,3 / mele,-2 -> mele,3 / pere,3.
def report_quantita(input_file: str, output_file: str) -> int:
    with open(input_file) as f:
        dati = [x.split(",") for x in f.read().splitlines() if x.split(",") != [""]]
        diz = {}
        for x in dati:
            if x[0] in diz:
                diz[x[0]] += int(x[1])
            else:
                diz[x[0]] = int(x[1])
        diz = dict(sorted(diz.items()))
    with open(output_file, 'w') as f:
        if dati == []:
            f.write("nome,totale")
            f.write("\n")
            return 0
        f.write("nome,totale")
        f.write("\n")
        for x,y in diz.items():
            f.write(f"{x},{y}")
            f.write("\n")

    return len(diz)  


# === PARTE B - IMMAGINI RGB (DOPO LEZIONE 12) ===


# ESERCIZIO 3 - conta_colore (3 punti)
# Data un'immagine come lista di liste di tuple RGB, restituire
# il numero di pixel esattamente uguali a colore, senza modificare img.
# Esempio: [[rosso, nero], [rosso, rosso]], rosso -> 3.
def conta_colore(img: list[list[tuple]], colore: tuple) -> int:
    conteg = sum(1 if x == colore  else 0 for y in img for x in y)
    return conteg


# ESERCIZIO 4 - img_invert_channels (5 punti)
# Leggere l'immagine PNG img_in, scambiare il canale rosso con il blu
# di ogni pixel (R,G,B) -> (B,G,R) e salvare il risultato in img_out.
# Le dimensioni e le posizioni dei pixel non devono cambiare.
def img_invert_channels(img_in: str, img_out: str) -> None:
    img1 = images.load(img_in)
    img2 = [[(b,g,r) for (r,g,b) in x] for x in img1]
    images.save(img2,img_out)
    return None


# ESERCIZIO 5 - img_quantize (5 punti)
# Leggere l'immagine PNG img_in e salvare in img_out una nuova immagine
# in cui ogni pixel (R,G,B) diventa (R//2,G//2,B//2).
# Esempio: (21,126,3) -> (10,63,1).
def img_quantize(img_in: str, img_out: str) -> None:
    img1 = images.load(img_in)
    img2 = [[(r//2,g//2,b//2) for (r,g,b) in x] for x in img1]
    images.save(img2,img_out)
    pass


# === PARTE C - DOPO LEZIONE 13 / FACOLTATIVI DOMANI ===


# ESERCIZIO 6 - img_invert_half (6 punti)
# Leggere un PNG con larghezza pari e salvare una nuova immagine
# scambiando la meta' sinistra con la meta' destra di ogni riga.
# Esempio: [A,B,C,D] -> [C,D,A,B].
def img_invert_half(img_in: str, img_out: str) -> None:
    img1 = images.load(img_in)
    img2 = [[(c,d,a,b) for (a,b,c,d) in x] for x in img1]
    images.save(img2,img_out)
    pass


# ESERCIZIO 7 - img_reflect_horizontal (5 punti)
# Leggere un PNG e salvarne il riflesso rispetto all'asse verticale:
# in ogni riga, il primo pixel diventa l'ultimo e viceversa.
# Esempio: [A,B,C,D] -> [D,C,B,A].
def img_reflect_horizontal(img_in: str, img_out: str) -> None:
    pass


# ESERCIZIO 8 - transpose (facoltativo)
# Restituire la trasposta di una matrice rettangolare non vuota,
# senza modificare quella originale.
# Esempio: [[1,2,3],[4,5,6]] -> [[1,4],[2,5],[3,6]].
def transpose(matrice: list[list]) -> list[list]:
    pass


# ESERCIZIO 9 - img_rotate_right_and_flip_v (facoltativo)
# Leggere un PNG, ruotarlo di 90 gradi in senso orario e riflettere
# il risultato rispetto all'asse verticale. Salvare in img_out.
def img_rotate_right_and_flip_v(img_in: str, img_out: str) -> None:
    pass


# === PARTE D - APPROFONDIMENTI FACOLTATIVI ===
# Esercizi da svolgere dopo aver approfondito filtri e cerchi.

# ESERCIZIO 10 - img_grayscale (facoltativo)
# Leggere un PNG e salvarne una versione in scala di grigi.
# Per ciascun pixel (R,G,B), usare per tutti i canali il valore intero
# ottenuto da 0.2126*R + 0.7152*G + 0.0722*B.
def img_grayscale(img_in: str, img_out: str):
    pass


# ESERCIZIO 11 - img_circle (facoltativo)
# Leggere il PNG img_in e colorare con c i pixel interni al cerchio
# di centro (x,y) e raggio r; salvare il risultato in img_out.
# Considerare il centro del pixel (colonna,riga) in
# (colonna+0.5, riga+0.5).
def img_circle(img_in: str, x: float, y: float, r: float, c: tuple, img_out: str):
    pass





# === TEST AUTOMATICI ===
if __name__ == '__main__':
    print('\nPARTE A - CSV')
    verifica('seleziona Python >=25', seleziona_studenti, 4,
             'studenti.csv', 'out_studenti.csv', 'Python', 25)
    verifica('seleziona nessuno', seleziona_studenti, 0,
             'studenti.csv', 'out_nessuno.csv', 'Python', 31)
    verifica('report quantita', report_quantita, 3,
             'movimenti.csv', 'out_movimenti.csv')
    verifica('report quantita vuoto', report_quantita, 0,
             'vuoto.csv', 'out_movimenti_vuoto.csv')
    # Verifichiamo anche i FILE di output, non soltanto i return.
    def leggi_testo(percorso):
        with open(percorso, 'r', encoding='utf-8') as f:
            return f.read()
    atteso = ('nome,voto\nAnna,30\nSara,30\n'
              'Luca,28\nMarco,25\n')
    verifica('contenuto studenti', leggi_testo, atteso, 'out_studenti.csv')
    verifica('nessuno: solo intestazione', leggi_testo,
             'nome,voto\n', 'out_nessuno.csv')
    verifica('contenuto report quantita', leggi_testo,
             'nome,totale\nbanane,4\nmele,3\npere,5\n', 'out_movimenti.csv')
    verifica('report vuoto: intestazione', leggi_testo,
             'nome,totale\n', 'out_movimenti_vuoto.csv')

    print('\nPARTE B - IMMAGINI (DOPO L12)')
    img = images.load('img_esercizi.png')
    verifica('conta_colore su piccola matrice', conta_colore, 3,
             [[(255,0,0),(0,0,0)],[(255,0,0),(255,0,0)]], (255,0,0))
    verifica('conta_colore assente', conta_colore, 0,
             [[(0,0,0),(255,255,255)]], (255,0,0))
    verifica_png('scambia R e B', img_invert_channels, 'out_canali.png',
                [[(b,g,r) for r,g,b in riga] for riga in img])
    verifica_png('quantizza //2', img_quantize, 'out_quant.png',
                [[(r//2,g//2,b//2) for r,g,b in riga] for riga in img])

    print('\nPARTE C - DOPO L13 / FACOLTATIVI')
    verifica_png('scambia le meta', img_invert_half, 'out_meta.png',
                [riga[len(riga)//2:] + riga[:len(riga)//2] for riga in img])
    verifica_png('riflessione orizzontale', img_reflect_horizontal, 'out_specchio.png',
                [riga[::-1] for riga in img])
    verifica('trasposizione', transpose, [[1,4],[2,5],[3,6]], [[1,2,3],[4,5,6]])
    verifica_png('rotazione+riflessione', img_rotate_right_and_flip_v,
                'out_trasposta.png',
                [[img[y][x] for y in range(len(img))] for x in range(len(img[0]))])

    print('\nPARTE D - APPROFONDIMENTI (verifica visiva)')
    print('Per grayscale e circle completare le funzioni, poi provare:')
    print('  img_grayscale("img1.png", "out_grayscale.png")')
    print('  img_circle("img1.png", 100, 100, 25, (255,255,0), "out_circle.png")')
    print('Confrontare visivamente con img1_grayscale.png e img1_circle.png.')
