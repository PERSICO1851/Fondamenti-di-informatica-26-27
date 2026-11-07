# Fondamenti di Informatica (A.A. 2026/2027)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-In%20sviluppo-brightgreen.svg)]()
[![Repository](https://img.shields.io/badge/GitHub-PERSICO1851-181717?logo=github)](https://github.com/PERSICO1851/Fondamenti-di-informatica-26-27)

Repository contenente il materiale di studio, le soluzioni dei laboratori, gli esercizi di approfondimento, le simulazioni d'esame pratiche con correzione automatica e i cheatsheet per il corso di **Fondamenti di Informatica / Fondamenti di Programmazione** in **Python**.

---

## 📚 Indice

- [Descrizione del Corso](#-descrizione-del-corso)
- [Struttura del Repository](#-struttura-del-repository)
- [Dettaglio dei Moduli](#-dettaglio-dei-moduli)
  - [Laboratori](#laboratori)
  - [Esercizi Tematici](#esercizi-tematici)
  - [Simulazioni d'Esame](#simulazioni-desame)
  - [Esercizi Extra & Notebook](#esercizi-extra--notebook)
  - [Cheatsheet](#cheatsheet)
- [Requisiti e Configurazione](#-requisiti-e-configurazione)
- [Come Eseguire i File e i Test](#-come-eseguire-i-file-e-i-test)
  - [Esecuzione degli Script e Laboratori](#esecuzione-degli-script-e-laboratori)
  - [Esecuzione dei Test delle Simulazioni](#esecuzione-dei-test-delle-simulazioni)
  - [Apertura dei Notebook Jupyter](#apertura-dei-notebook-jupyter)
- [Autore](#-autore)

---

## 📖 Descrizione del Corso

Il corso introduce ai principi fondamentali dell'informatica e alla programmazione strutturata procedurale in Python. Il percorso didattico copre:
- Tipi di dato base (interi, float, booleani, stringhe) ed espressioni.
- Strutture di controllo condizionali (`if`/`elif`/`else`) e iterative (`for`, `while`).
- Funzioni, passaggio di parametri, visibilità delle variabili e ricorsione.
- Strutture dati sequenziali e associative: liste, tuple, insiemi (`set`) e dizionari (`dict`).
- Tecniche di List, Dict e Set Comprehension.
- Input/Output su file (`.txt`, `.csv`) con gestione delle codifiche.
- Algoritmi di ricerca, filtro e ordinamento personalizzato.
- Test-driven development, debugging e lettura dei traceback.

---

## 🗂️ Struttura del Repository

```text
Simulazione01-test/
│
├── laboratiorio 2/
│   └── lab2.py                     # Errori, traceback, if/else, cicli, funzioni e stringhe
│
├── laboratorio3/
│   ├── lab3.py                     # Test, debugging, manipolazione stringhe e liste
│   └── Laboratorio03_DOCENTE_FINALE.ipynb # Notebook di supporto del docente
│
├── Laboratorio 4/
│   └── lab4.py                     # Tuple, insiemi, liste, dizionari e algoritmi di ordinamento
│
├── 05-dizionari/
│   ├── esercizi_persico.py         # Soluzioni ed esercizi svolti sui dizionari con test colorati
│   ├── esercizi_raw.py             # Traccia iniziale degli esercizi sui dizionari
│   ├── soluzioni.py                # Soluzioni di riferimento
│   └── soluzioni_alt.py            # Implementazioni alternative e ottimizzazioni
│
├── Laboratorio5/
│   ├── Laboratorio05.py            # Comprehension, frequenze parole e parsing testo
│   └── *.txt                       # Dataset di testo (frequenti, parole, tabelle, ecc.)
│
├── 06-file/
│   ├── esercizi_persico.py         # Esercizi completi di lettura, elaborazione e scrittura file
│   ├── esercizi-raw.py             # Traccia di partenza per gli esercizi I/O su file
│   ├── soluzioni.py / soluzioni_alt.py # Soluzioni standard e varianti
│   ├── test.py                     # Script di collaudo rapido
│   ├── ripasso/                    # Approfondimenti ed esercizi riassuntivi
│   └── file0*.txt / file0*.csv     # File di input e test di formato testo e CSV
│
├── simulazione_1/
│   ├── program.py                  # Implementazione delle funzioni richieste (func1-func6)
│   ├── grade.py                    # Correttore automatico con punteggi su base 30
│   ├── testlib.py                  # Modulo di supporto per i test unitari
│   ├── grade.csv                   # Report dei punteggi assegnati dal correttore
│   └── README.md                   # Istruzioni e regolamento della simulazione 1
│
├── esercizi_prova_simulazione2/
│   ├── program.py                  # Risoluzione della seconda simulazione (esA, esB)
│   ├── grade.py                    # Correttore automatico per la simulazione 2
│   ├── testlib.py                  # Framework di test per esA ed esB
│   ├── esA/ e esB/                 # File di test e directory di input/output
│   └── grade.csv                   # Punteggio finale della simulazione 2
│
├── esercizi_prova_simulazione2_raw/ # Copia vergine per rieseguire la simulazione 2 da zero
│
├── Esercizi_Extra/
│   └── 1/
│       └── esercizi.ipynb          # Notebook interattivo su collezioni, cicli e input utente
│
├── cheetsheets/
│   └── Cheatsheet_Python_Fondamenti_Lezioni_0-4.docx # Dispensa riassuntiva di sintassi
│
├── grade.csv                       # Registro valutazioni dei test
└── README.md                       # Questo file
```

---

## 📌 Dettaglio dei Moduli

### Laboratori

I laboratori contengono esercizi pratici organizzati spesso a celle interattive (`# %%`) compatibili con l'estensione Python per **VS Code** o l'editor **Spyder**:

- **Laboratorio 2 (`laboratiorio 2/lab2.py`)**:
  - Analisi e lettura degli errori (*Traceback*).
  - Condizionali ed iterazioni (`somma_cifre`, `bin_str_to_dec`, `cubic_root`, `even_minus_odd`, `check_date`, `strip_spazi`).
- **Laboratorio 3 (`laboratorio3/`)**:
  - Tecniche di test e debug con asserzioni e funzioni di supporto (`check_test`, `print_test`).
  - Manipolazione avanzata di stringhe, liste, sottoliste e slicing.
- **Laboratorio 4 (`Laboratorio 4/lab4.py`)**:
  - Strutture dati: tuple, insiemi e dizionari (`dict`).
  - Funzioni di intersezione, aggregazione e conteggio frequenze.
  - Criteri di ordinamento senza l'uso di lambda o comprehension.
- **Laboratorio 5 (`Laboratorio5/`)**:
  - List & Dict Comprehension applicate a filtri e trasformazioni.
  - Pulizia del testo da caratteri non alfanumerici e calcolo di frequenze di parole (`word_frequency`).

### Esercizi Tematici

- **05 - Dizionari (`05-dizionari/`)**:
  - Manipolazione avanzata di mappe chiave-valore.
  - Raggruppamento per categorie, inversioni di dizionari, aggregazioni e conteggi.
- **06 - File e I/O (`06-file/`)**:
  - Apertura in modalità lettura (`r`) e scrittura (`w`, `a`) con blocco `with`.
  - Elaborazione riga per riga di file di testo (`.txt`) e file tabellari con separatori (`.csv`).
  - Parsing di record, conversioni di tipo e formattazione dell'output.

### Simulazioni d'Esame

Le cartelle di simulazione riproducono fedelmente l'ambiente d'esame universitario al calcolatore con valutazione automatizzata:

1. **Simulazione 1 (`simulazione_1/`)**:
   - 6 funzioni indipendenti (`func1` – `func6`) con vincoli su mutabilità delle strutture (modifiche *in-place*), casi limite (collezioni vuote, duplicati) e rispetto dei tipi di ritorno.
   - Punteggio calcolato da `grade.py` con soglia minima di 18/30.
2. **Simulazione 2 (`esercizi_prova_simulazione2/`)**:
   - Esercizi strutturati su file I/O e logica complessa:
     - **Es. A**: conteggio totale parole in file, estrazione parole uniche in ordine alfabetico e scrittura su file destinazione.
     - **Es. B**: elaborazione avanzata di matrici e strutture dati annidate.
   - Presenza della directory `esercizi_prova_simulazione2_raw/` per potersi ri-esercitare su un template pulito.

### Esercizi Extra & Notebook

- **`Esercizi_Extra/1/esercizi.ipynb`**:
  - Notebook Jupyter con problemi progressivi: liste di elementi, cicli con input da terminale, validazione dei dati e stampe tabellari formattate.

### Cheatsheet

- **`cheetsheets/Cheatsheet_Python_Fondamenti_Lezioni_0-4.docx`**:
  - Guida rapida di riferimento per la sintassi essenziale di Python, operatori logici e matematici, metodi delle stringhe e collezioni.

---

## 💻 Requisiti e Configurazione

- **Python 3.10 o superiore** (consigliato Python 3.11 / 3.12 / 3.13).
- **Editor consigliato**:
  - [Visual Studio Code](https://code.visualstudio.com/) con estensioni:
    - *Python* (`ms-python.python`)
    - *Jupyter* (`ms-toolsai.jupyter`)
  - Oppure [Spyder IDE](https://www.spyder-ide.org/) / [PyCharm](https://www.jetbrains.com/pycharm/).

Per clonare il repository:

```bash
git clone https://github.com/PERSICO1851/Fondamenti-di-informatica-26-27.git
cd Fondamenti-di-informatica-26-27
```

---

## 🚀 Come Eseguire i File e i Test

### Esecuzione degli Script e Laboratori

Tutti gli script possono essere eseguiti direttamente da terminale:

```bash
# Esempio per Laboratorio 2
python3 "laboratiorio 2/lab2.py"

# Esempio per Laboratorio 5
cd Laboratorio5
python3 Laboratorio05.py

# Esempio per il modulo Dizionari
python3 05-dizionari/esercizi_persico.py
```

Nei file con suddivisione a celle (`# %%`), è possibile aprire il file in VS Code o Spyder ed eseguire singole celle con la combinazione `Shift + Enter` o cliccando sul pulsante **Run Cell**.

### Esecuzione dei Test delle Simulazioni

Per verificare la correttezza del proprio codice tramite il correttore automatico:

```bash
# Simulazione 1
cd simulazione_1
python3 grade.py

# Simulazione 2
cd ../esercizi_prova_simulazione2
python3 grade.py
```

Il correttore assegnerà i punteggi per ogni test superato e aggiornerà il rispettivo file `grade.csv`.

### Apertura dei Notebook Jupyter

Per consultare o svolgere i notebook:

```bash
jupyter notebook Esercizi_Extra/1/esercizi.ipynb
```
*(In alternativa, aprire il file `.ipynb` direttamente all'interno dell'interfaccia di VS Code).*

---

## 👤 Autore

- **Vincenzo Persico** - [PERSICO1851](https://github.com/PERSICO1851)
