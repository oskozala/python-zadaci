ime = input()
prezime = input()
godina_rodjenja = int(input())

inicijali = ime[0] + '.' + prezime[0] + '.'
dob = str(2024 - godina_rodjenja)

zasticeni_podaci = inicijali + ' (' + dob + ')'

print(zasticeni_podaci)
