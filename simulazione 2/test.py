file = '/Users/persicovincenzo/Downloads/simulazione 2/txt/in_01.txt'
#lista = []
#with open(file) as f:
#    letto = f.read()
#    lista = [("".join(c if c.isalpha() else " " for c in y)).split() for y in letto.splitlines()]
#    print(lista)
#    lista = sorted(list(set([elemento.lower() for lista_annidata in lista for elemento in lista_annidata])))
#
#print(lista)
#lista = []
#file_in_a = "/Users/persicovincenzo/Downloads/simulazione 2/txt/in_01.txt"
#file_in_b =  "/Users/persicovincenzo/Downloads/simulazione 2/txt/in_03.txt"
#
#with open(file_in_a) as f:
#    lista_a = []
#    for y in f.read().splitlines():
#        for i in y:
#            if not i.isspace():
#                lista_a.append(i)
#    print(lista_a)
#with open(file_in_b) as f:
#    lista_b = []
#    for y in f.read().splitlines():
#        for i in y:
#            if not i.isspace():
#                lista_b.append(i)
#lista_a2 = sorted(list(set([x for x in lista_a if x not in lista_b])))
#lista_b2 = sorted(list(set([x for x in lista_b if x not in lista_a])))
#lista = [*lista_a2,*lista_b2]
#
#print(lista)
#lists = [["monkey", "cat",], 
#         ["panda", "alligator"], 
#         ["zoo", 'zuu','zotero']] 
#listi=  [[1, 0],	# prima la parola 1 e poi la 0
#         [0, 1],	# prima la 0 e poi la 1
#         [2, 1, 0]]	# prima la 2 poi la 1 poi la 0
#
#for i in range(len(lists)):
#    for y in listi[i]:
#        print(lists[i][y])
##    print('+')
#input_file = "func4/func4_test1.txt"
#output_file = "func4/func4_out1.txt"
#conteggio = 0
#with open(input_file) as f:
#    letto = f.read()
#    lista = [("".join(c if c.isalpha() else " " for c in y)).split() for y in letto.splitlines()]
#    lista = sorted([elemento for lista_annidata in lista for elemento in lista_annidata],key= lambda x:(len(x),x))
#with open(output_file,'w') as f:
#    for y in lista:
#        f.write(y)
#        print(y)
#        conteggio += 1
#print(conteggio)


input_filename = "/Users/persicovincenzo/Downloads/simulazione 2/func5/func5_test1.txt"
output_filename = "/Users/persicovincenzo/Downloads/simulazione 2/func5/func5_out1.txt"
length = 3
conteggio = 0

with open(input_filename, 'r', encoding='utf-8') as f:
    letto = f.read()

lista = [("".join(c if c.isalpha() else " " for c in y)).split() for y in letto.splitlines()]
lista = [elemento for lista_annidata in lista for elemento in lista_annidata]
lista = [x for x in lista if len(x) == length]
lista = sorted(lista)
print("Lista ordinata:", lista)

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

print("Conteggio totale:", conteggio)




print(conteggio)

"""
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

e ritornare il valore 7. """