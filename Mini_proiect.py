# Mini-proiect - IT-School
# Evidenta angajatilor intr-o companie


# Autor: Florian Trocan, 2025

# o lista unde vom salva angajatii
angajati = []

# Functii de verificare si cautare
# Verifica daca CNP are lungimea corespunzatoare, este format doar din cifre si incepe cu 1,2, 5 sau 6
def validare_cnp(cnp):
    return cnp.isdigit() and len(cnp) == 13 and cnp[0] in ("1", "2", "5", "6")

# Verifica daca varsta este un numar si este peste 18
def validare_varsta(varsta):
    return varsta.isdigit() and int(varsta) >= 18

# verifica daca salariul este un numar si este peste salariul minim de 4050
def validare_salariu(salariu):
    return salariu and float(salariu) >= 4050

# verifica daca departamentul introdus se afla in lista de departamente ale companiei
def validare_departament(departament):
    return departament.lower() in ["it", "hr", "contabilitate", "management", "juridic", "marketing", "logistica"]

# verifica daca nivelul de senioritate introdus se afla in lista de niveluri de senioritate
def validare_senioritate(senioritate):
    return senioritate.lower() in ["junior", "mid", "senior"]


# cauta angajat dupa CNP si returneaza angajat
def cauta_angajat(cnp):
    for angajat in angajati:
        if angajat["CNP"] == int(cnp):
            return angajat
    return None

# cauta departament dupa nume si returneaza departamentul
def cauta_departament(departament):
    for angajat in angajati:
        if angajat["Departament"] == departament:
            return angajat
    return None

# cauta nivel de senioritate si returneaza nivelul
def cauta_senioritate(senioritate):
    for angajat in angajati:
        if angajat["Senioritate"] == senioritate:
            return angajat
    return None


# 1. Adauga angajat nou
def adauga_angajat():
    cnp = input("Introdu CNP: ")
    if not validare_cnp(cnp):
        print("CNP invalid.")
        return

    if cauta_angajat(cnp):
        print("Angajatul exista deja.")
        return

    nume = input("Nume: ")
    prenume = input("Prenume: ")

    varsta = input("Varsta: ")
    if not validare_varsta(varsta):
        print("Varsta angajatului trebuie sa fie peste 18 ani.")
        return

    salariu = input("Salariu: ")
    if not validare_salariu(salariu):
        print("Salariul este sub minimum pe economie (4.050 RON).")
        return

    departament = input("Departament: ")
    if not validare_departament(departament):
        print("Departamentul ales nu exista.")
        return

    senioritate = input("Senioritate (junior/mid/senior): ")
    if not validare_senioritate(senioritate):
        print("Nivel de senioritate invalid.")
        return

# un dictionar pentru noul angajat pe care il vom salva intr-o lista
    angajat = {
        "CNP": int(cnp),
        "Nume": nume,
        "Prenume": prenume,
        "Varsta": int(varsta),
        "Salariu": float(salariu),
        "Departament": departament.lower(),
        "Senioritate": senioritate.lower()
    }

# Adauga noul angajat intr-o lista de angajati
    angajati.append(angajat)
    print("Angajat adaugat cu succes.")

# 2. Cauta angajat dupa CNP
def cautare_angajat():
    cnp = int(input("Introdu CNP-ul angajatului: "))
    angajat = cauta_angajat(cnp)
    if angajat:
        print(angajat)
    else:
        print("Angajatul nu exista.")


# 3. Modifica date angajat dupa CNP
def modifica_angajat():
    cnp = int(input("Introdu CNP-ul angajatului pe care doresti sa-l modifici: "))
    angajat = cauta_angajat(cnp)
    if not angajat:
        print("Angajatul nu exista.")
        return

    print("Lasati campul gol daca nu doriti modificari.")
    nume = input(f"Nume nou pentru {angajat['Nume']}: ")
    prenume = input(f"Prenume nou pentru {angajat['Prenume']}: ")
    varsta = input(f"Varsta noua ({angajat['Varsta']}): ")
    salariu = input(f"Salariu nou ({angajat['Salariu']}): ")
    departament = input(f"Departament nou ({angajat['Departament']}): ")
    senioritate = input(f"Senioritate noua ({angajat['Senioritate']}): ")

    if varsta and not validare_varsta(varsta):
        print("Varsta invalida.")
        return

    if salariu and not validare_salariu(salariu):
        print("Salariu invalid.")
        return

    if departament and not validare_departament(departament):
        print("Departament invalid.")
        return

    if senioritate and not validare_senioritate(senioritate):
        print("Senioritate invalida.")
        return

        # Aplicam modificarile doar daca s-a introdus ceva
    if nume:
        angajat["Nume"] = nume
    if prenume:
        angajat["Prenume"] = prenume
    if varsta:
        angajat["Varsta"] = int(varsta)
    if salariu:
        angajat["Salariu"] = float(salariu)
    if departament:
        angajat["Departament"] = departament.lower()
    if senioritate:
        angajat["Senioritate"] = senioritate.lower()

    print(f"Datele angajatului {angajat['Nume']} {angajat['Prenume']} au fost actualizate.")


# 4. Sterge angajat
def sterge_angajat():
    cnp = input("Introdu CNP-ul angajatului pentru stergere: ")
    angajat = cauta_angajat(cnp)
    if angajat:
        angajati.remove(angajat)
        print("Angajat sters.")
    else:
        print("Angajatul nu a fost gasit.")

# 5. Afisare angajati
def afisare_angajati():
    if not angajati:
        print("Nu exista angajati.")
        return
    for angajat in angajati:
        print(angajat)

# 6. Calculator cost total salarii
def cost_salarii():
    total = sum(angajat["Salariu"] for angajat in angajati)
    print(f"Cost total salarii: {total:.2f} RON")

# 7. Calculator salarii dupa departament
def cost_salarii_dept():
    departament = input("Departament: ").lower()
    total = sum(angajat["Salariu"] for angajat in angajati if angajat["Departament"] == departament)
    print(f"Cost total în departamentul {departament}: {total:.2f} RON")

# 8. Calculator fluturas salariu angajat
def fluturas_salariu():
    cnp = input("Introdu CNP: ")
    angajat = cauta_angajat(cnp)
    if not angajat:
        print("Angajat inexistent.")
        return
    brut = angajat["Salariu"]
    cas = brut * 0.10
    cass = brut * 0.25
    net = brut - cas - cass
    impozit = net * 0.10
    salariu_final = net - impozit
    print(f"""
    Flutura de salariu pentru {angajat['Nume']} {angajat['Prenume']}: 
    Salariu brut: {brut:.2f} RON
    CAS (10%): {cas:.2f} RON
    CASS (25%): {cass:.2f} RON
    Impozit (10%): {impozit:.2f} RON
    -> Salariu net: {salariu_final:.2f} RON
    """)

# 9. Afisarea angajatilor (dupa senioritate)
def sortare_senioritate():
    senioritate = input("Introdu nivelul de senioritate: ").lower()
    sort = [angajat for angajat in angajati if angajat["Senioritate"] == senioritate]
    if sort:
        for angajat in sort:
            print(angajat)
    else:
        print(f"Nu exista angajati cu senioritate {senioritate}.")

# 10. Afisarea angajatilor (dupa departament)
def sortare_departament():
    departament = input("Introdu departamentul: ").lower()
    sort = [angajat for angajat in angajati if angajat["Departament"] == departament]
    if sort:
        for angajat in sort:
            print(angajat)
    else:
        print(f"Nu exista angajati in departamentul {departament}")


# MENIU
def meniu():
    while True:
        print("""
    === Meniu Principal ===
    1. Adaugare angajat
    2. Cautare angajat
    3. Modificare date angajat
    4. Stergere angajat
    5. Afisare angajati
    6. Cost total salarii
    7. Cost salarii departament
    8. Fluturas salariu
    9. Afisare dupa senioritate
    10. Afisare dupa departament
    11. Iesire
            """)
        optiune = input("Alege o opțiune: ")

        if optiune == "1":
            adauga_angajat()
        elif optiune == "2":
            cautare_angajat()
        elif optiune == "3":
            modifica_angajat()
        elif optiune == "4":
            sterge_angajat()
        elif optiune == "5":
            afisare_angajati()
        elif optiune == "6":
            cost_salarii()
        elif optiune == "7":
            cost_salarii_dept()
        elif optiune == "8":
            fluturas_salariu()
        elif optiune == "9":
            sortare_senioritate()
        elif optiune == "10":
            sortare_departament()
        elif optiune == "11":
            print("La revedere!")
            break
        else:
            print("Optiune invalida.")

meniu()