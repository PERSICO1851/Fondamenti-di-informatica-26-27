#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare la simulazione e' necessario ottenere il punteggio 18 o più.
(15 per studenti con DSA)

Il voto finale e' la somma dei punteggi dei problemi risolti.
"""
nome       = "persico"
cognome    = "vincenzo"
matricola  = "ronaldo"

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# Per eseguire solo alcuni dei test, commentate le voci con cui viene assegnata
# la lista 'tests' alla fine di grade.py
################################################################################


#%% ---------------------------- FUNC 1 ---------------------------- #

'''
Func 1: 8 punti
Si definisca la funzione func1(png_input) che riceve come argomento:
- png_input:  il percorso di una immagine PNG

Il file png_input contiene una immagine a sfondo nero, contenente stelline.
Ogni stellina è una "crocetta" di dimensione 3x3 pixel, composta da 5 pixel:
i 4 angoli del quadrato 3x3 e il pixel centrale.
Esempio di stellina (x = pixel colorato, . = sfondo nero):
x.x
.x.
x.x

Le stelline non si toccano tra loro, né con lati né con angoli, e non si
sovrappongono, indipendentemente dal colore.

La funzione deve contare il numero di stelline presenti, per ciascun colore,
e tornare un dizionario che ha come chiavi i colori delle stelline presenti nell'immagine
e come valori il numero di stelline di quel colore.

Esempio:
Se l'immagine è 'func1/in_1.png' il risultato sarà il dizionario
{(217, 159, 157): 3, (166, 93, 67): 2}

'''

import images

def func1(png_input):
    img1 = images.load(png_input)
    listacol = []
    for riga in img1:
        for pixel in riga:
            listacol.append(pixel)
    diz = {key:(listacol.count(key)/5) for key in listacol if key != (0,0,0)}
    return diz
    # Inserisci qui il tuo codice

# print(func1('func1/in_1.png'))
# %% ----------------------------------- FUNC2 ------------------------- #
'''
Func 2: 10 punti
Si definisca la funzione func2(txt_input, width, height, png_output) che riceve come argomenti

- txt_input:  il percorso di un file che contiene un elenco di figure da disegnare
- width:      larghezza in pixel dell'immagine da creare
- height:     altezza in pixel dell'immagine da creare
- png_output: il percorso di una immagine PNG che dovete creare, contenente le figure

La funzione deve creare una immagine a sfondo nero e disegnarci sopra
tutte le figure indicate nel file 'txt_input', nell'ordine in cui
appaiono nel file. Una figura disegnata dopo ne sovrascrive i pixel.

Il file txt_input contiene, una per riga, separate da spazi:
- una parola che indica il tipo di figura da disegnare
- le tre componenti R G B del colore da usare
- le coordinate e gli altri parametri necessari a definire la figura

Possono essere presenti 2 tipi di figura:
- diagonale discendente (direzione -45°)
    diagonalDOWN R G B x y L
    La figura è formata dagli L pixel (x,y), (x+1,y+1), ..., (x+L-1,y+L-1)
- diagonale ascendente (direzione +45°)
    diagonalUP R G B x y L
    La figura è formata dagli L pixel (x,y), (x+1,y-1), ..., (x+L-1,y-(L-1))

Ogni figura è interamente contenuta nell'immagine.

Quindi deve salvare l'immagine ottenuta nel file 'png_output' usando la funzione images.save.
Inoltre deve ritornare il numero di diagonali disegnate dei due tipi
come tupla dei due valori (DIAGUP,DIAGDOWN)

Esempio: se il file func2/in_1.txt contiene le 3 righe
diagonalDOWN 0 255 0 2 3 10
diagonalUP 255 0 0 12 20 12
diagonalUP 0 0 255 5 25 8

l'esecuzione della funzione func2('func2/in_1.txt', 30, 30, 'func2/your_image_1.png')
produrrà una figura uguale al file 'func2/expected_1.png'
e tornerà la coppia (2, 1)
'''

def func2(txt_input, width, height, png_output): 
    img1 = [[(0,0,0) for _ in range(width)] for _ in range(height)]  #immagine vuota
    istruzioni = []
    DIAGUP = 0
    DIAGDOWN = 0
    with open(txt_input) as f:
        istruzioni = [riga.split() for riga in f]
    for inst in istruzioni:
        pixel = (int(inst[1]),int(inst[2]),int(inst[3]))
        x,y = int(inst[4]),int(inst[5])
        l = int(inst[6])
        match inst[0]:
            case "diagonalDOWN":
                DIAGDOWN += 1
                for i in range(l): 
                    img1[y+i][x+i] = pixel 

            case "diagonalUP":
                DIAGUP += 1
                for i in range(l): 
                    img1[y-i][x+i] = pixel
    images.save(img1,png_output)           
    return (DIAGUP,DIAGDOWN)
    # Inserisci qui il tuo codice


# print(func2('func2/in_1.txt', 30, 30, 'func2/out_1.png'))

# %% ----------------------------------- FUNC3 ------------------------- #
""" func3: 6 points
Si scriva una funzione func3(imagefile, output_imagefile, color) che prende
in ingresso due stringhe che rappresentano due nomi di file di immagini PNG
e una tupla color (R,G,B).
L'immagine nel file 'imagefile' contiene esclusivamente segmenti orizzontali
bianchi su uno sfondo nero. Ogni riga ha al più un segmento bianco.
Ogni segmento parte dal bordo sinistro dell'immagine (colonna 0), e la sua
lunghezza è il numero dei suoi pixel bianchi.
Esiste un unico segmento di lunghezza massima.

La funzione deve creare una nuova immagine in cui sono presenti gli stessi
segmenti dell'immagine in ingresso, e colorare con il colore color il segmento
di lunghezza massima.

L'immagine così ottenuta deve essere salvata in formato PNG nel file con
percorso output_imagefile.

La funzione ritorna la lunghezza massima dei segmenti.
"""
import images

def func3(imagefile, output_imagefile, color):
    img1 = images.load(imagefile)
    lug = [riga.count((255,255,255)) for riga in img1]
    print(lug)
    mas = max(lug)
    print(mas)
    for i,x in enumerate(img1[lug.index(mas)]):
        if x == (255,255,255):
            img1[lug.index(mas)][i] = color
    images.save(img1,output_imagefile)
    return mas

    # Inserisci qui il tuo codice


# print(func3('func3/image01.png', 'func3/your_image01.png', (255,0,0)))

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 points
Si definisca la funzione func4(L, A, sfondo, file_rettangoli, imagefile_out)
che riceve come argomenti:                              
    - la larghezza L, altezza A e colore di sfondo di una immagine da creare
    - il path di un file che contiene, su ciascuna riga, i parametri di un rettangolo
    - il path imagefile_out in cui salvere l'immagine ottenuta
Il file dei rettangoli contiene su ciascuna riga 7 valori
    - x, y, larghezza, altezza, R, G, B
    dove x, y sono le coordinate dell'angolo in alto a sinistra del rettangolo.
    Il rettangolo pieno occupa i pixel (x..x+larghezza-1, y..y+altezza-1).
    Ogni rettangolo è interamente contenuto nell'immagine.
La funzione deve:
    - disegnare nell'ordine i rettangoli pieni nell'immagine
    - sommare il numero di pixel di tutti i rettangoli (anche se successivamente
        sovrascritti da un rettangolo disegnato dopo)
    - restituire tale somma
"""
import images

def func4(L : int, A : int, sfondo : tuple[int,int,int], file_rettangoli : str, imagefile_out : str) -> int:
    img = [[sfondo for _ in range(L)] for _ in range(A)]
    somma = 0
    with open(file_rettangoli) as f:
        istruzioni = [riga.split() for riga in f]
        for inst in istruzioni:
            x,y = int(inst[0]),int(inst[1])
            larghezza = int(inst[2])
            altezza = int(inst[3])
            color = (int(inst[4]),int(inst[5]),int(inst[6]))
            somma += larghezza*altezza
            for alt in range(altezza):
                for larg in range(larghezza):
                    img[y+alt][x+larg] = color
            

    images.save(img,imagefile_out)
    return somma
    # Inserisci qui il tuo codice

# print(func4(40,40,(0,255,0),'func4/rect_01.txt', 'func4/out_01.png'))    # 85
