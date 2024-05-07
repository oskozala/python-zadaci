tekst = input()
slovo_za_pretrazivanje = input()

nadjeno = 0

for i in range(len(tekst)):
    if tekst[i] == slovo_za_pretrazivanje:
        nadjeno += 1

print('"' + slovo_za_pretrazivanje + '" - ', end='')

if nadjeno:
    print(nadjeno)
else:
    print('nije nađeno')
