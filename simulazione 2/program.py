#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# type: ignore

"""
#####################    ISTRUZIONI PER LA SIMULAZIONE.  ####################

PRIMA DI TUTTO: Assegna le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Aggiungi le tue implementazioni delle funzioni descritte sotto.
Per ottenere il punteggio esegui il file grade.py contenuto nella cartella.
Per superare la simulazione e' sufficiente ottenere un punteggio maggiore o uguale a 18.

Per commentare/decommentare il codice velocemente usate Control + 1 !
"""

nome       = "Ronaldo"
cognome    = "borrello"
matricola  = "24542555"

################################################################################
################################################################################
################################################################################

################################################################################
# %% ----------------------------------- FUNC.1 ------------------------------ #
################################################################################
'''func1: 6 punti

Si definisca la funzione func1(file_in : str) -> list[str] che prende
in ingresso una stringa che indica il percorso ad un file di testo e
restituisce una lista di stringhe.  


La funzione apre il file di testo da cui si estraggono tutte le parole 
portandole tutte a minuscole. 


La funzione restituisce una lista delle parole uniche trovate nel file di
testo, ordinate in **ordine alfabetico**.

Esempio:
se file_in punta a 'txt/in_01.txt' la funzione restituisce 
expected = ['bat', 'car', 'cat', 'condor', 'rat']

N.B. per estrarre le parole considerate solo i caratteri alfabetici; 
esempi: 
- la stringa '7od842m3m\t7gbe' diventa 4 parole ['od', 'm', 'm', 'gbe']
- la stringa 'E io a lui: "Poeta, io ti richeggio'
  diventa ['e', 'io', 'a', 'lui', 'poeta', 'io', 'ti', 'richeggio']
'''

def func1(file_in : str) -> list[str]:
    with open(file_in) as f:
        letto = f.read()
        lista = [("".join(c if c.isalpha() else " " for c in y)).split() for y in letto.splitlines()]
        lista = sorted(list(set([elemento.lower() for lista_annidata in lista for elemento in lista_annidata])))
    return lista





    



################################################################################
# %% -------------------------------- FUNC.2 --------------------------------- #
################################################################################
''' func2: 6 punti
Si definisca la funzione func2(file_in_a : str, file_in_b : str) ->
list[str] che riceve come argomenti 2 stringhe che puntano a due file di
testo e restituisce una lista di stringhe.  
La funzione apre i due file di testo e trova tutti i caratteri unici contenuti 
in ciascuno dei due file tranne a capo, tabulazioni e spazi.  
La funzione restituisce una lista di stringhe dove nella prima parte della lista 
sono inseriti i caratteri unici del primo file che non appaiono nel secondo, 
ordinati in ordine alfabetico; mentre nella seconda parte sono inseriti i caratteri 
unici del secondo file che non compaiono nel primo sempre ordinati alfabeticamente.

Esempio:
come input 'txt/in_01.txt' e 'txt/in_03.txt'
la funzione restituisce

['B', 'D', 'E', 'G', 'H', 'I', 'L', 'M', 'N', 'O', 'P',
'S', 'U', 'V', 'Y', 'e', 'g', 'h', 'i', 'l', 'm', 'p', 's', 'u',
'v', 'w', 'y', '😌']
'''


def func2(file_in_a : str, file_in_b : str) -> list[str]:
    with open(file_in_a) as f:
        lista_a = []
        for y in f.read().splitlines():
            for i in y:
                if not i.isspace():
                    lista_a.append(i)
    with open(file_in_b) as f:
        lista_b = []
        for y in f.read().splitlines():
            for i in y:
                if not i.isspace():
                    lista_b.append(i)
    lista_a2 = sorted(list(set([x for x in lista_a if x not in lista_b])))
    lista_b2 = sorted(list(set([x for x in lista_b if x not in lista_a])))
    lista = [*lista_a2,*lista_b2]
    return lista 
    



################################################################################
# %% -------------------------------- FUNC.3 --------------------------------- #
################################################################################
'''func3: 6 punti
Implementare la func3(lists : list[list[str]], listi :
list[list[int]], out : str) -> int: 
che riceve come argomenti: 
- una lista di liste di stringhe, di nome lists 
- una lista di liste di interi di nome listi 
- una stringa out, che indica a che percorso la funzione
deve scrivere un file di testo 


La funzione ritorna un intero.

Per ogni lista di parole contenuta in lists si scrive una riga del file
in out.  


L'ordine di scrittura delle parole su ciascuna riga e' pero' specificato 
dalla lista degli interi corrispondenti in listi, che vanno considerati
come posizioni delle parole da leggere dalle liste per scriverle nel file.


La funzione ritorna il numero totale di parole scritte nel file out.

Esempio se:
lists = [["monkey", "cat",], 
         ["panda", "alligator"], 
         ["zoo", 'zuu','zotero']] 
listi=  [[1, 0],	# prima la parola 1 e poi la 0
         [0, 1],	# prima la 0 e poi la 1
         [2, 1, 0]]	# prima la 2 poi la 1 poi la 0
valore di ritorno e' 7 e nel file out viene scritto:

cat monkey
panda alligator
zotero zuu zoo
'''

def func3(lists : list[list[str]], listi : list[list[int]], out : str) -> int:
    conteggio = 0
    with open(out,'w') as f:
        for i in range(len(lists)):
            for y in listi[i]:
                f.write(lists[i][y] + " ")
                conteggio += 1
            f.write('\n')
    return conteggio
    
    
    
    
    
    

    


################################################################################
# %% ----------------------------------- FUNC.4 ------------------------------ #
################################################################################
""" func4: 6 punti

Si scriva una funzione func4(input_file, output_file) che prende in
ingresso due stringhe, 'input_file' e 'output_file' che rappresentano
i percorsi a due file.  All'interno del file indicato da 'input_file'
sono presenti su una sola riga una serie di parole (composte da
caratteri alfabetici) separate da ****virgole, spazi, punti e virgole e da
punti.****

La funzione deve individuare tutte le parole contenute nel file
indicate da 'input_file' e scriverle all'interno di un nuovo file
indicato da 'output_file'.  

Le parole devono essere scritte
all'interno del file su una sola riga terminata dal carattere di
a capo, separate da uno spazio e con il seguente ordine:
    - numero di caratteri crescente,
    - in caso di parità, in ordine alfabetico, indipendentemente da
      maiuscole e minuscole
    - in caso di parole identiche, in ordine lessicografico

La funzione deve restituire il numero di parole scritte nel file in
output.

Esempio: se il contenuto del file 'input_file' è il seguente
Dog,cat,dog;Cat.bird car

l'invocazione di func4('input_file', 'output_file') dovrà scrivere nel
file 'output_file' la seguente riga
car Cat cat Dog dog bird

e ritornare il valore 6.
"""


def func4(input_file : str, output_file : str) -> int:
    conteggio = 0
    with open(input_file) as f:
        letto = f.read()
        lista = [("".join(c if c.isalpha() else " " for c in y)).split() for y in letto.splitlines()]
        lista = sorted([elemento for lista_annidata in lista for elemento in lista_annidata],key= lambda x:(len(x),x.lower(),x))
    with open(output_file,'w') as f:
        for y in lista:
            f.write(y+" ")
            conteggio += 1
    return conteggio



################################################################################
# %% -------------------------------- FUNC.5 --------------------------------- #
################################################################################

""" func5: 6 punti
Si definisca una funzione func4(input_filename, output_filename, length) 
che riceve come argomenti due stringhe che rappresentano due nomi di file 
e un intero.

Il file input_filename contiene una serie di stringhe separate da spazi,
tabulazioni o a capo.


La funzione deve creare un nuovo file di testo con nome output_filename
contenente tutte le stringhe di ***lunghezza length*** presenti nel file
input_filename organizzate per righe.

Le righe devono essere in ordine alfabetico.

Le parole di ogni riga:
    - hanno la stessa lettera iniziale, senza distinzione fra maiuscole e
      minuscole
    - sono separate da uno spazio
    - sono ordinate in base all'ordine alfabetico, senza distinzione fra
      maiuscole e minuscole. In caso di parole uguali, in ordine alfabetico.

La funzione deve ritornare il numero di stringhe della lunghezza
richiesta trovate nel file in input.

Esempio
Se nel file 'func4_test1.txt' sono presenti le seguenti tre righe
cat bat    rat
Condor baT
Cat cAr CAR

la funzione func5('func5_test1.txt', '  ', 3) dovrà scrivere
nel file 'func5_out1.txt' le seguenti 3 righe:
baT bat
CAR cAr Cat cat
rat

e ritornare il valore 7.

"""


def func5(input_filename, output_filename, length):
    conteggio = 0
    
    with open(input_filename, 'r', encoding='utf-8') as f:
        letto = f.read()
    
    lista = [("".join(c if c.isalpha() else " " for c in y)).split() for y in letto.splitlines()]
    lista = [elemento for lista_annidata in lista for elemento in lista_annidata]
    

    lista = [x for x in lista if len(x) == length]
    
    lista = sorted(lista, key=lambda x: (x.lower(), x))
    with open(output_filename, 'w', encoding='utf-8') as f:
        if lista:
            current = [lista[0]]
            conteggio += 1
            
            for word in lista[1:]:
                if word[0].lower() == current[0][0].lower():
                    current.append(word)
                else:
                    f.write(" ".join(current) + "\n")
                    current = [word]
                conteggio += 1
                
            f.write(" ".join(current) + "\n")
            
    return conteggio




################################################################################
################################################################################
################################################################################
