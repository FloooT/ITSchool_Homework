'''Problema 1.
Creeaza un catalog scolar care:
-Primeste de la utilizator numele elevilor si notele acestora
-Salveaza aceste informatii intr-o lista de forma catalog = [['Ana', [9, 10, 8], ['Mihai', [6, 7, 9]] etc
-Afiseaza: - media fiecarui elev
            - elevii care au media >= 5 -> promovat
            - elevii cu media < 5 -> corigenti ***(am facut la curs partea asta)***
-Functie adaugare elev
-Functie afisare rezultate
-Modificare note elev
-Stergere elev din catalog
-Exit
'''

catalog = []
note = []
# elev = input("Introdu numele elevului: ")
# nota1 = float(input("Introdu prima nota: "))
# nota2 = float(input("Introdu a 2a nota: "))
# nota3 = float(input("Introdu a 3a nota: "))
# catalog.append(elev)
# note.append(nota1)
# note.append(nota2)
# note.append(nota3)
# catalog.append(note)
# print(catalog)

def adauga_elev(catalog):
    elev = input("Introdu numele elevului: ")
    nota1 = float(input("Introdu prima nota: "))
    nota2 = float(input("Introdu a 2a nota: "))
    nota3 = float(input("Introdu a 3a nota: "))
    catalog.append(elev)
    note.append(nota1)
    note.append(nota2)
    note.append(nota3)
    catalog.append(note)

adauga_elev(catalog)
print(catalog)








'''Problema 2. Detecteaza operatorul de telefonie mobila din Romania folosind liste si prefixe.
Accepta formate : -0xxxxxxxxx
                  -+40xxxxxxxxx
                  -0040xxxxxxxxx
vodafone: 72, 73
orange: 74, 75
telekom: 76, 78
digi: 77

Hints: -curatare spatii si liniute(folositi replace() )
        -Standardizare in format local 0xxxxxxxxx
        -Validare basic: 10 cifre, toate digits, incepe cu 0
        -Extrage prefixul
        -Defineste liste pentru prefixe operator
        -Lista generala operatori ( fiecare element este [nume, lista prefixe]
        -Cauta in liste
        -Afiseaza rezultatul'''
