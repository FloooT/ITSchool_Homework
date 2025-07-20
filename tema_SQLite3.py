'''
Creeaza un script care executa urmatoarele operatii:

1. Creeaza tabelul studenti cu coloanele:
    -id
    -nume
    -varsta
2. Adauga cel putin 5 studenti cu valori diferite pentru nume si varsta
    - Foloseste parametrizare si inserari multiple
3. Afiseaza toti studentii
4. Afiseaza studentii cu varsta > 20
5. Afiseaza studentii al caror nume incepe cu litera A
6. Creste varsta cu 1 pentru un student
    -Afiseaza dupa aceea randul modificat pentru a verifica schimbarea
7. Sterge toti studentii cu varsta < 19
    -Afiseaza toti studentii pentru a verifica rezultatul
8. Daca exista deja tabela studenti, sterge-o pentru a nu face append cu datele precedente
9. Adauga o coloana email
    - Pentru studentul cu id = 1 seteaza un mail si verifica comanda
Spor
'''

import sqlite3

# 1. Creare baza de date studenti.db
conn = sqlite3.connect('studenti.db')
cursor = conn.cursor()

# Creare tabel studenti
cursor.execute('DROP TABLE IF EXISTS studenti') # 8. sterge tabelul studenti pentru a nu face append cu datele precedente
cursor.execute('''
    CREATE TABLE IF NOT EXISTS studenti(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nume TEXT,
    varsta INTEGER
    )
''')

# 2. Adaugam 5 studenti
studenti = [('Andrei Popescu', 21), ('Maria Ionescu', 22), ('Robert Stan', 20), ('Ioana Dobre', 23), ('Alexandru Mihai', 18)]
cursor.executemany('INSERT INTO studenti (nume, varsta) VALUES (?, ?)', studenti)

# 3. Afisam toti studentii
cursor.execute('SELECT * FROM studenti')
rezultate = cursor.fetchall()

for rand in rezultate:
    print(rand)

# 4. Afisam studentii cu varsta > 20 ani
cursor.execute('SELECT nume, varsta FROM studenti WHERE varsta > ?', (20, ))
print('Studentii care au peste 20 ani sunt:')
for nume, varsta in cursor.fetchall():
    print(f"{nume}: {varsta} ani")

# 5. Afisam studentii al caror nume incepe cu litera A
cursor.execute("SELECT nume, varsta FROM studenti WHERE nume LIKE 'A%'")
print("Studentii al caror nume incepe cu litera 'A'")
for nume, varsta in cursor.fetchall():
    print(f"{nume}")

# 6. Crestem varsta cu 1 an pentru un student si afisam
cursor.execute('UPDATE studenti SET varsta = varsta + 1 WHERE id = ?', (3,))
cursor.execute('SELECT nume, varsta FROM studenti WHERE id = ?', (3,))
for nume, varsta in cursor.fetchall():
    print(f"{nume} a mai crescut 1 an -> {varsta}")

# 7. Stergem toti studentii cu varsta sub 19 ani
cursor.execute('DELETE FROM studenti WHERE varsta < ?', (19,))
cursor.execute('SELECT * FROM studenti')
rezultate2 = cursor.fetchall()

for rand in rezultate2:
    print(rand)

# 9. Adaugam coloana email. Pentru studentul cu id = 1 setam un mail si verificam comanda
cursor.execute('ALTER TABLE studenti ADD COLUMN email TEXT')
cursor.execute('UPDATE studenti SET email = ? WHERE id = ?', ('andreip@abc.com', 1))
cursor.execute('SELECT nume, email FROM studenti WHERE id = ?', (1,))
for nume, email in cursor.fetchall():
    print(f"{nume} are emailul: {email}")


