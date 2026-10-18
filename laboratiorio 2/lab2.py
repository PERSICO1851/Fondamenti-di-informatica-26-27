################################################################################
# Fondamenti di Programmazione - Laboratorio 2
# FILE STUDENTI
#
# Argomenti: errori, if, for, while, funzioni, stringhe
################################################################################

# COME LAVORARE
# 1. Aprite questo file nella VM con VS Code.
# 2. Completate una funzione alla volta.
# 3. Eseguite il file con "Run Python File" oppure da terminale:
#       python3 esercizi_lab02_studenti_FINALE.py
# 4. Provate anche casi diversi da quelli forniti.
#
# NOTA:
# Il file contiene semplici test con print().
# Non serve ancora capire come costruire un framework di test.


################################################################################
# ESERCIZI DA SVOLGERE DURANTE IL LABORATORIO
################################################################################
#
# Il file contiene più esercizi di quelli che riusciremo a svolgere insieme.
#
# Durante le 2 ore di laboratorio concentratevi, nell'ordine, su:
#
#   0.1  Caccia all'errore
#   0.2  Leggere un traceback
#   1.1  check_grade
#   1.2  check_date
#   2.1  somma_cifre
#   3.2  even_minus_odd
#   4.1  chiedi_voto
#
# Se terminate questi esercizi, continuate con:
#
#   2.2  bin_str_to_dec
#   3.1  cubic_root
#   4.2  strip_spazi
#
# In fondo al file trovate inoltre una sezione di ESERCIZI OPTIONAL,
# tratti anche dai laboratori degli anni precedenti.
#
# Non è necessario completare tutti gli esercizi durante il laboratorio.
#
# Per ogni esercizio:
#   1. leggete attentamente la consegna;
#   2. completate la funzione al posto di TODO/pass;
#   3. decommentate i test corrispondenti in fondo al file;
#   4. eseguite il programma;
#   5. provate almeno un caso diverso da quelli forniti.
################################################################################


################################################################################
# RECAP VELOCE - da fare insieme
################################################################################

# Esempio: funzione + if + return
def voto_valido(voto):
    return 0 <= voto <= 30

print("Recap voto_valido:", voto_valido(27), voto_valido(35))


# Esempio: for + contatore
def conta_a(parola):
    contatore = 0

    for carattere in parola.lower():
        if carattere == "a":
            contatore += 1

    return contatore

print("Recap conta_a:", conta_a("Azkaban"))


################################################################################
# TEMA 0 - CAPIRE E CORREGGERE GLI ERRORI
################################################################################

# In Python possiamo incontrare soprattutto tre tipi di errore:
#
# 1. ERRORE DI SINTASSI (SyntaxError)
#    Python non riesce a comprendere il codice e il programma non parte.
#
# 2. ERRORE DURANTE L'ESECUZIONE (runtime error)
#    Il programma parte, ma si interrompe durante l'esecuzione.
#
# 3. ERRORE LOGICO
#    Il programma viene eseguito senza messaggi di errore,
#    ma produce un risultato sbagliato.


# ------------------------------------------------------------------------------
# ESERCIZIO 0.1 - CACCIA ALL'ERRORE
# ------------------------------------------------------------------------------

# Per ciascun frammento:
# - indicate il tipo di errore;
# - individuate la riga che lo causa;
# - correggete il codice e provatelo.

# A)
# def saluta(nome):
#     print("Ciao " + nome)
#
# saluta()                    # Che cosa manca?


# B)
# def maggiore(a, b):
#     if a > b:
#         return b
#     else:
#         return a            # Il programma parte, ma il risultato è corretto?


# C)
# eta = int(input("Inserisci la tua età: "))
# if eta >= 18                # Osservate attentamente questa riga
#     print("Maggiorenne")


# ------------------------------------------------------------------------------
# ESERCIZIO 0.2 - LEGGERE UN TRACEBACK
# ------------------------------------------------------------------------------

# Eseguite, una alla volta, le istruzioni seguenti togliendo il simbolo #.
# Leggete il messaggio dal basso verso l'alto e individuate:
# - il tipo di errore;
# - la riga in cui si è verificato;
# - la possibile correzione.

# print(numero_non_definito)  # NameError
# print(int("ciao"))          # ValueError
# print("età: " + 20)         # TypeError
# print(10 / 0)               # ZeroDivisionError


################################################################################
# TEMA 1 - CONDIZIONI
################################################################################

# ------------------------------------------------------------------------------
# ESERCIZIO 1.1 - check_grade
# ------------------------------------------------------------------------------

# Scrivere una funzione check_grade(a, b, c) che:
# - ritorna la somma dei tre voti se TUTTI sono compresi tra 0 e 30;
# - ritorna -1 altrimenti.
#
# Esempi:
# check_grade(21, 18, 2)  -> 41
# check_grade(21, 32, 2)  -> -1

def check_grade(a, b, c):
    # TODO
    pass


# ------------------------------------------------------------------------------
# ESERCIZIO 1.2 - check_date
# ------------------------------------------------------------------------------

# Scrivere una funzione check_date(d, m, y) che ritorna True se la data è valida,
# False altrimenti.
#
# Possiamo ignorare gli anni bisestili.
#
# Esempi:
# check_date(30, 2, 2017) -> False
# check_date(1, 1, 1111)  -> True
# check_date(31, 4, 2011) -> False

def check_date(d, m, y):
    # TODO
    pass


################################################################################
# TEMA 2 - FOR E STRINGHE
################################################################################

# ------------------------------------------------------------------------------
# ESERCIZIO 2.1 - somma_cifre
# ------------------------------------------------------------------------------

# Scrivere una funzione somma_cifre(s) che riceve una stringa composta da cifre
# decimali e ritorna la somma delle cifre.
#
# Esempio:
# somma_cifre("85721") -> 23

def somma_cifre(s):
    # TODO
    pass


# ------------------------------------------------------------------------------
# ESERCIZIO 2.2 - bin_str_to_dec
# ESERCIZIO AGGIUNTIVO / SE FINITE PRIMA
# ------------------------------------------------------------------------------

# Scrivere una funzione bin_str_to_dec(s) che riceve una stringa binaria
# e ritorna il corrispondente numero decimale.
#
# Esempio:
# bin_str_to_dec("00101") -> 5
#
# Suggerimento:
# nuovo_valore = vecchio_valore * 2 + nuova_cifra

def bin_str_to_dec(s):
    # TODO
    pass


################################################################################
# TEMA 3 - FUNZIONI
################################################################################

# ------------------------------------------------------------------------------
# ESERCIZIO 3.1 - cubic_root
# ESERCIZIO AGGIUNTIVO / SE FINITE PRIMA
# ------------------------------------------------------------------------------

# Scrivere una funzione cubic_root(n) che prende un numero e ritorna
# la sua radice cubica.
#
# Deve funzionare anche per numeri negativi.
#
# Esempi:
# cubic_root(8)  -> 2.0
# cubic_root(-8) -> -2.0

def cubic_root(n):
    # TODO
    pass


# ------------------------------------------------------------------------------
# ESERCIZIO 3.2 - even_minus_odd
# ------------------------------------------------------------------------------

# Scrivere una funzione even_minus_odd(a, b, c, d, e) che ritorna:
#
# somma dei numeri pari - somma dei numeri dispari
#
# Esempio:
# even_minus_odd(1, 2, 3, 4, 5) -> -3
#
# Provate a risolverlo SENZA usare liste.

def even_minus_odd(a, b, c, d, e):
    # TODO
    pass


################################################################################
# TEMA 4 - WHILE E INPUT
################################################################################

# ------------------------------------------------------------------------------
# ESERCIZIO 4.1 - chiedi_voto
# ------------------------------------------------------------------------------

# Scrivere una funzione chiedi_voto() che:
# - legge un voto da input;
# - continua a chiederlo finché non è compreso tra 0 e 30;
# - ritorna il voto valido.
#
# Per semplicità assumiamo che l'utente inserisca sempre un intero.

def chiedi_voto():
    # TODO
    pass


# ------------------------------------------------------------------------------
# ESERCIZIO 4.2 - strip_spazi
# ESERCIZIO AGGIUNTIVO / SE FINITE PRIMA
# ------------------------------------------------------------------------------

# Scrivere una funzione strip_spazi(s) che elimina gli spazi " "
# all'inizio e alla fine della stringa SENZA usare str.strip().
#
# Esempi:
# strip_spazi("   ciao mondo   ") -> "ciao mondo"
# strip_spazi("ciao")             -> "ciao"
# strip_spazi("     ")            -> ""

def strip_spazi(s):
    # TODO
    pass


################################################################################
# TEST DEGLI ESERCIZI PRINCIPALI
################################################################################
# Decommentate progressivamente i test quando avete completato le funzioni.

# print("\ncheck_grade")
# print(check_grade(21, 18, 2))      # 41
# print(check_grade(21, 32, 2))      # -1
# print(check_grade(21, 18, -2))     # -1

# print("\ncheck_date")
# print(check_date(30, 2, 2017))     # False
# print(check_date(1, 1, 1111))      # True
# print(check_date(31, 4, 2011))     # False
# print(check_date(30, 4, 2011))     # True

# print("\nsomma_cifre")
# print(somma_cifre("85721"))         # 23
# print(somma_cifre("00000"))         # 0

# print("\nbin_str_to_dec")
# print(bin_str_to_dec("00101"))      # 5
# print(bin_str_to_dec("1111"))       # 15

# print("\ncubic_root")
# print(cubic_root(8))                # circa 2.0
# print(cubic_root(-8))               # circa -2.0

# print("\neven_minus_odd")
# print(even_minus_odd(1, 2, 3, 4, 5))   # -3
# print(even_minus_odd(2, 2, 2, 2, 2))   # 10
# print(even_minus_odd(1, 1, 1, 1, 1))   # -5

# print("\nchiedi_voto")
# print("Voto accettato:", chiedi_voto())

# print("\nstrip_spazi")
# print(repr(strip_spazi("   ciao mondo   ")))  # 'ciao mondo'
# print(repr(strip_spazi("ciao")))               # 'ciao'
# print(repr(strip_spazi("     ")))              # ''


################################################################################
# OPTIONAL - ESERCIZI AGGIUNTIVI
# Tratti anche dai laboratori degli anni precedenti.
################################################################################

# ------------------------------------------------------------------------------
# OPTIONAL A - PICCOLI ESPERIMENTI CON GLI ERRORI
# ------------------------------------------------------------------------------

# A.1 Cosa succede se dimenticate gli apici alla fine di una stringa?
# A.2 Cosa succede se dividete un numero per 0?
# A.3 Cosa succede se in print dimenticate una o entrambe le parentesi?
# A.4 Cosa succede con +2? E con 2++2?
# A.5 Cosa succede se scrivete 02?
# A.6 In Python possiamo scrivere xy al posto di x*y?
# A.7 Cosa succede se facciamo 42 = n?
# A.8 Cosa succede con x = y = 1?
# A.9 Cosa succede se mettete ; alla fine di un'istruzione? E un punto?


# ------------------------------------------------------------------------------
# OPTIONAL B - CALCOLI
# ------------------------------------------------------------------------------

# B.1 Scrivere una espressione che calcoli il numero di secondi
#     che ci sono in 42 minuti e 42 secondi.

# B.2 Scrivere una espressione che calcoli il numero di miglia
#     che ci sono in 10 chilometri. (1 miglio = 1.61 km).

# B.3 Calcolare la velocità media e la cadenza media
#     (tempo per miglio, in minuti e secondi) di un corridore
#     che corre 10 km in 42 minuti e 42 secondi.

# B.4 Il volume di una sfera di raggio r è:
#     4/3 * PI * r^3
#     Calcolare il volume di una sfera di raggio 5.

# B.5 Il prezzo di copertina di un libro è 24.95 euro.
#     Una libreria ottiene il 40% di sconto.
#     La spedizione costa 3 euro per la prima copia e 0.75 euro
#     per ogni copia aggiuntiva.
#     Calcolare il costo totale di 60 copie.

# B.6 Si esce di casa alle 6:52.
#     Primo miglio: 8 min 15 sec
#     Tre miglia: 7 min 12 sec per miglio
#     Ultimo miglio: 9 min 45 sec
#     A che ora si torna a casa?


# ------------------------------------------------------------------------------
# OPTIONAL C - STRINGHE
# ------------------------------------------------------------------------------

# C.1 Avete una stringa di 5 caratteri. Il carattere centrale è il punto.
#     Ad esempio:
#         s = "52.29"
#     Stampare il numero decimale rappresentato dalla stringa
#     come numero, non come stringa.

def dec_frac_str_to_dec(s):
    # TODO
    pass


# ------------------------------------------------------------------------------
# OPTIONAL D - FUNZIONI
# ------------------------------------------------------------------------------

# D.1 Scrivere una funzione root_max(a, b, c) che calcola le radici
#     dell'equazione:
#         a*x^2 + b*x + c
#     e ritorna la maggiore.
#     Se le radici sono complesse, restituisce una qualsiasi delle due.

def root_max(a, b, c):
    # TODO
    pass


# D.2 Scrivere una funzione roots(a, b, c) che calcola le radici
#     dell'equazione:
#         a*x^2 + b*x + c
#     e le ritorna entrambe.

def roots(a, b, c):
    # TODO
    pass


# D.3 Scrivere una funzione print_hello() che legge un nome da input
#     e ritorna una stringa formata da:
#     "Ciao " + nome + ". Buona giornata!"

def print_hello():
    # TODO
    pass


################################################################################
# TEST OPTIONAL
################################################################################

# print("\ndec_frac_str_to_dec")
# print(dec_frac_str_to_dec("52.29"))

# print("\nroot_max")
# print(root_max(1, -5, 6))

# print("\nroots")
# print(roots(1, -5, 6))

# print("\nprint_hello")
# print(print_hello())