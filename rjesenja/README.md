# Rješenja zadataka



<!--                                                                                                    KAŠNJENJE -->

<details>
  <summary><em>1. Kašnjenje</em></summary>
  <hr />
  
Krenimo od onoga što nam je poznato i onog što još ne znamo.

**Poznat** nam je podatak da školski sat traje 45 minuta, pa će rješenje nedvojbeno biti `45 - n`, a kako nam program to mora ispisati, koristit ćemo funkciju `print()`.

```python
print(45 - n)
```

**Nepoznat** nam je podatak koliko uopće iznosi `n`, tj. koliko je Ana zakasnila na sat. Da bi to saznali, naprosto ćemo pitati Anu da nam ga upiše koristeći se funkcijom `input()`.

Ne smijemo zaboraviti da se unos mora pretvoriti u broj pomoću funkcije `int()` (najbolje istovremeno), kako bi mogli s njim nešto i izračunati.

Unos, naravno moramo dodati u kod **prije** ispisa.
```python
n = int(input())
print(45 - n)
```

Kako znamo što se od nas traži, program u ovom obliku nam je jasan. No, kod mora biti čitljiv i nekome tko ne zna što se od nas traži. Usporedi kod iznad s kodom u datoteci [kasnjenje.py](https://github.com/oskozala/python-zadaci/blob/main/rjesenja/kasnjenje.py).

Ova dva programa rade na potpuno isti način, jedina razlika je čitljivost koda. ***Čitljivije*** je uvijek ***bolje***, inače bismo mogli napisati program i ovako:

```python
print(45 - int(input()))
```

  <hr />
</details>



<!--                                                                                                                        IZBORI -->

<details>
  <summary><em>2. Izbori</em></summary>

Pitajmo za početak korisnika da nam upiše koliko ima godina:

```python
dob = int(input())
```

Znamo da je u Hrvatskoj punoljetna osoba svatko tko je napunio 18. godinu, pa možemo to postaviti kao *granicu* između glasača i neglasača.

| *Ne glasuju*             | *Glasuju*           |
|--------------------------|---------------------|
| 1, 2, 3, ..., 15, 16, 17 | **18**, 19, 20, ... |

Matematički se možemo izraziti tako da prvi stupac odgovara broju godina `dob < 18`, a drugi `dob >= 18` (veće ili jednako, pošto ne smijemo zaboraviti uključiti i broj 18).

U prvom stupcu su osobe kojima moramo ispisati samo koliko godina još neće moći glasati te, kao u prvom zadatku, ispisat ćemo jednostavnu računicu:

```python
print(18 - dob)
```

Svima ostalima ćemo naprosto reći:

```python
print('GLASUJ')
```

A kako će program odlučiti spada li netko u prvi ili u drugi stupac gornje tablice? Koristeći se, naravno naredbom `if` i uvjetima koje smo već postavili iznad:

```python
dob = int(input())

if dob < 18:
    print(18 - dob)
else:
    print(`GLASUJ`)
```

U ovom smo primjeru krenuli od prvog stupca. Kako bi postavili uvjet ako smo prvo htjeli "riješiti" ove iz drugog stupca?

Usporedi kod iznad s kodom u datoteci [izbori.py](https://github.com/oskozala/python-zadaci/blob/main/rjesenja/izbori.py).

*Jesmo li mogli umjesto `dob >= 18` koristiti `dob > 17`? Nije li to isto, ako govorimo o prirodnim brojevima?*

Je, isto je i program bi se isto i izvodio. Pitanje je jedino što je jasnije nekome tko pročita kod prvi put? Brojka `18` će nam već na prvi pogled jasnije odrediti da je netko punoljetan, nitko ni u svakodnevnom govoru ne kaže da je punoljetna osoba ona koja ima više od 17 godina. 🙂
  
  <hr />
</details>



<!--                                                                                                                        INICIJALI -->

<details>
  <summary><em>3. Inicijali</em></summary>
  <hr />

Kao što vidimo iz primjera, program nas mora pitati da unesemo tri podatka, jedan po jedan.

Kako bi pojednostavili ovaj zadatak, godina rođenja unijet ćemo bez točke.

```python
ime = input()
prezime = input()
godina_rodjenja = int(input())
```

Svaki veći problem se može podijeliti na više manjih pa ćemo i mi to ovdje napraviti, primjerice ovako:
1. naći ćemo inicijale (s točkama),
2. izračunat ćemo godine starosti,
3. spojit ćemo te podatke s potrebnim znakovima (zagrade) i na kraju ispisati.


***1. Inicijali***

Kako bismo dobili inicijale (s točkama) moramo napraviti nekoliko stvari:
- "izvući" ćemo samo prva slova iz varijabli `ime` i `prezime` (koristeći se uglatim zagradama kao prethodnom zadatku) i
- umetnuti točke nakon oba slova.

```python
inicijali = ime[0] + "." + prezime[0] + "."
```

*Prisjetimo se da operator `+` spaja sve podatke tipa `str`, tj. one koje sadrže tekst.*


***2. Dob***

Godine starosti ćemo jednostavno izračunati.

```python
dob = 2024 - godina_rodjenja
```

**3. Spajanje i formatiranje teksta**

Zasad imamo varijablu `inicijali` u kojoj je primjerice `L.M.` i imamo varijablu `dob` gdje je pohranjen broj `39`.

Spajajući to s ostalim znakovima, niz može izgledati ovako:

`L.M.` ` (` `39` `)` 👈 *Zagrade su spojene s brojem, a prije prve zagrade je razmak*

Već znamo kako se spajaju *stringovi* u Pythonu:

```python
  zasticeni_podaci = inicijali + " (" + dob + ")"
```

Izvrsno smo to zamislili, zar ne? Problem je jedino što Python neće biti zadovoljan, a reći će nam i zašto:

```pycon
TypeError: can only concatenate str (not "int") to str
```

*U prijevodu to znači da se u niz mogu spajati `str` i `str`, ali ne i `str` i `int`.*

Srećom, kao što možemo pretvoriti tekst u broj, možemo učiniti i obrnuto:

```pycon
>>> int('5')
5
>>> str(5)
'5'
```

Stoga ćemo varijablu `dob` pretvoriti u tekstni zapis pomoću funkcije `str()` te nas Python više neće opominjati. 😌

```diff
-  zasticeni_podaci = inicijali + " (" + dob + ")"
+  zasticeni_podaci = inicijali + " (" + str(dob) + ")"
```

Preostaje nam samo ispisati ovako skrojeni *string*:

```python
print(zasticeni_podaci)
```

*Funkciju `str` mogli smo upotrijebiti i pri samom računanju varijable `dob`, kao što se to vidi u datoteci [inicijali.py](https://github.com/oskozala/python-zadaci/blob/main/rjesenja/inicijali.py).*

  <hr />
</details>



<!--                                                                                                                        ZNAMENKE 1 -->

<details>
  <summary><em>4. Znamenke (1)</em></summary>
  <hr />

Program nas pita da unesemo neki troznamenkasti broj, a naučili smo da se u Pythonu to radi ovako, zar ne?

```python
broj = int(input())
```

Istina, ali zadatak nas ne pita da računamo nešto s tim brojem, nego da obavimo nekakvo računanje *unutar* samog broja.

Moguće je riješiti program i na taj način, nizom matematičkih operacija, ali moguće je doći i do jednostavnijeg rješenja. 😉

Kad bi rješavali problem olovkom na papiru, vrijednost samog broja ne bi nam puno značila. Naprotiv bilo kakvoj matematičkoj logici, rastavili bi broj na tri zasebne brojke i sveli problem na algebarsku operaciju iz 1. razreda osnovne škole. 🙂

Stoga ćemo upravo tako napraviti i naš program: nećemo broj unositi kao broj, nego ćemo ga pustiti za početak u izvornom obliku kakvog nam funkcija `input()` vraća, a to je `str` *(string)*.

```python
broj = input()
```

Dakle, primjer unesenog broja neće biti `123`, već `'123'`.

*(Razlika je u navodnicima, nismo koristili funkciju `int()`).*

Sada možemo varijablu `broj` smatrati običnim nizom znakova, i kao takvog je i "zloupotrijebiti". 🙈

Pretpostavljamo da je varijabla niz od tri znaka, a znamo da se pojedini znakovi mogu "izvući" iz niza ako znamo njihovu poziciju (broj mjesta, prva pozicija je `0` 👈), primjerice:

```python
ime = 'Marko'
prezime = 'Wilsdorf'

inicijali = ime[0] + prezime[0]  # u ovom slučaju 'MW'
```

Da bi program bio čitljiviji, stvorit ćemo tri nove varijable (besplatne su!) i u njih pohraniti svaki od znakova:

```python
znamenka_1 = broj[0]
znamenka_2 = broj[1]
znamenka_3 = broj[2]

zbroj = znamenka_1 + znamenka_2 + znamenka_3
```

No, ako ih zbrojimo u ovom obliku, Python će nam opet vratiti troznamenkasti broj. Zašto? 🤔

*Odgovor slijedi, ali se krije i u prethodnom zadatku.* 😉

Razlog je što Python operator `+` koristi na nekoliko načina. Ukucajmo nekoliko operacija u Pythonovu konzolu pa će nam biti jasnije:

```pycon
>>> 7 + 8
15
>>> '7' + '8'
'78'
>>> 'O' + 'Š'
'OŠ'
```

Kao u primjeru s inicijalima Marka Wilsdorfa, ako između dva komada teksta stavimo znak `+`, Python (i mnogi drugi) će ih jednostavno zalijepiti skupa.

Zato je za naš zadatak najbolje da naše znamenke pretvorimo u cijele brojeve na istom mjestu gdje smo ih izvukli iz originalnog (troznamenkastog) broja.

```python
znamenka_1 = int(broj[0])
znamenka_2 = int(broj[1])
znamenka_3 = int(broj[2])

zbroj = znamenka_1 + znamenka_2 + znamenka_3
```

Cijeli kod pogledaj [ovdje](https://github.com/oskozala/python-zadaci/blob/main/rjesenja/znamenke-1.py).

  <hr />
</details>



<!--                                                                                                                        SIGMA -->

<details>
  <summary><em>5. Sigma</em></summary>
  <hr />

Kako bismo riješili ovaj zadatak napamet ili na papiru?

Krenuli bi od početka, zbrajali broj po broj i pamtili (ili zapisivali) svaki rezultat, a zadnji rezultat je ujedno i konačno rješenje.

Ako, primjerice, moramo zbrojiti prvih pet prirodnih brojeva (1 + 2 + 3 + 4 + 5), postupak bi bio sličan ovome:

1 + 2 = 3, 3 + 3 = 6, 6 + 4 = 10, 10 + 5 = 15.

Rasporedimo ove brojeve u tablicu da postupak bude pregledniji:

| | | | |
|----|-----:|----:|-----:|
| 1. |  ***`1`*** | `2` |        `3` |
| 2. |        `3` | `3` |        `6` |
| 3. |        `6` | `4` |       `10` |
| 4. |       `10` | `5` | ***`15`*** |

Ako postavimo rješenje na ovaj način, krećemo od broja `1` te nam ostaje još **četiri** broja za zbrajanje.

Započnimo program unosom nekog prirodnog broja:

```python
n = int(input())
```

Nadalje, kao što vidimo iz tablice, zbroj jednog reda (3. stupac) početna je vrijednost sljedećeg (1. stupac).

Dakle, potrebna nam je varijabla koja će prenositi vrijednosti iz kruga u krug. Nazovimo je `zbroj`, a početna vrijednost je `1`.

```python
zbroj = 1
```

Iz tablice također vidimo da će nam biti potrebna četiri kruga, a vrijednosti s kojima zbrajamo idu redom (2. stupac).

Petlju s tim vrijednostima je lako složiti: početna vrijednost je `2`, a krajnja za jedan više od broja koji smo unijeli na početku, u ovom slučaju `6`.

```python
for i in range(2, n + 1):
```

No što će se događati u svakom krugu?

Vidimo da se 3. stupac prenosi u 1., dakle potrebno je varijablu `zbroj` zbrojiti sa sljedećim brojem u nizu (u ovom slučaju naći ćemo ga u brojaču `i`) i to spremiti nazad u istu varijablu:

```python
  zbroj = zbroj + i
```

Iako ovo nikako nije netočno, Python (kao i mnogi drugi programski jezici) nudi nam kraći način pisanja iste ove operacije.

Na hrvatskom možemo, umjesto "zbroji s" `i` i spremi rezultat u istu varijablu, reći naprosto ***uvećaj za*** `i`:

```python
  zbroj += i
```

Kad petlja završi, kao i na papiru, rezultat zadnjeg zbrajanja je ujedno i rješenje:

```python
print(zbroj)
```

*Jedno od mogućih rješenja je i krenuti od nule. Ne mijenja nam rezultat, ali nam mijenja broj krugova. Usporedi objašnjenje ovog zadatka s kodom u datoteci [sigma.py](https://github.com/oskozala/python-zadaci/blob/main/rjesenja/sigma.py).*

  <hr />
</details>



<!--                                                                                                                        NAĐI SLOVO -->

<details>
  <summary><em>6. Nađi slovo</em></summary>
  <hr />

Kad bi morali izbrojati koliko se na jednoj stranici teksta ponavlja slovo "a", kako bi to napravili?

Najjednostavnije bi bilo krenuti čitati ispočetka i svaki put kad naiđemo na slovo "a", napravimo recku olovkom na komad papira pa ih na kraju zbrojimo.

Ovo je primjer tzv.  _sekvencijalnog pretraživanja_, što znači da rečenicu provjeravamo slovo po slovo (točnije, znak po znak) i bilježimo koliko se određeno slovo ponavlja.

Za početak nam trebaju tekst koji pretražujemo i slovo koje želimo naći u tom tekstu:

```python
tekst = input()
slovo_za_pretrazivanje = input()
```

Kao što smo to radili na papiru, tako ćemo i u kodu. Jedino što će nam recke brojiti jedna dobra stara varijabla, možemo je nazvati _nađeno_.

Koliko smo slova dosad izbrojali? Koliki je rezultat na počeku utakmice?

```python
nadjeno = 0
```

Kako ćemo natjerati program da tekst čita znak po znak?

Moramo se, naravno, poslužiti petljom.

Koliko će krugova imati ta petlja? Onoliko koliko uneseni tekst ima znakova, očito. 😏

Ukoliko tekst ima `6` znakova, onda su oni raspoređeni na pozicijama `0`, `1`, `2`, `3`, `4` i `5` pa nam treba jedna petlja koja će i "brojiti" po tim vrijednostima, npr:

```python
for i in range(6):
```

Varijabla `i` će tako krenuti od nule (pozicija prvog znaka) do pet (pozicija zadnjeg znaka) pa će nam samo "čitanje" teksta znak po znak biti jednostavno. Primjerice:

```pycon
>>> tekst = 'Kozala'
>>> for i in range(6):
...     print('Na poziciji', i, 'nalazi se slovo', tekst[i])
...    
Na poziciji 0 nalazi se slovo K
Na poziciji 1 nalazi se slovo o
Na poziciji 2 nalazi se slovo z
Na poziciji 3 nalazi se slovo a
Na poziciji 4 nalazi se slovo l
Na poziciji 5 nalazi se slovo a
>>>
```

Zasad odlično, no što ako ne znamo koliko će znakova tekst imati?

Tu nam može pomoći funkcija `len()` (skraćeno od *length* - duljina).

```pycon
>>> len("12345")
5
>>> skola = 'O.Š. Kozala'
>>> len(skola)
11
```

Da ponovimo, onoliko koliko nam vrati funkcija `len()`, toliko će petlja imati krugova pa je možemo koristiti u postavljanju `for` petlje.

```python
for i in range(len(tekst)):
```

U nastavku moramo u svakom krugu provjeriti je li trenutni znak isti kao onaj koji smo unijeli na početku.

Ako (`if`) je isti (`==`), stavimo recku (`nadjeno` se povećava za 1).

Ako nije, nikom ništa (nije nam potreban `else`). 😃

```python
    if tekst[i] == slovo_za_pretrazivanje:
        nadjeno += 1
```

Preostaje nam ispisati koliko je puta znak nađen ili poruku da nije (u formatu kao u primjerima):

1. Dodajmo slovu navodnike:

```python
znak = '"' + slovo_za_pretrazivanje + '"'
```

2. Provjerimo je li slovo nađeno i ispišimo poruku:

```python
if nadjeno > 0:
    print(znak, '-', nadjeno)
else:
    print(znak, '- nije nađeno')
```

_Usporedi ovaj način ispisivanja poruke s kodom u datoteci [nadji-slovo.py](https://github.com/oskozala/python-zadaci/blob/main/rjesenja/nadji-slovo.py)._


### **_Alternativno rješenje_**

Sad kad znamo sekvencijalno pretraživati, vrijeme je da se kaže da postoji i jednostavniji način "čitanja" teksta petljom, a da pritom ne moramo niti znati koliko tekst ima znakova.

Uzmimo primjer od maloprije i usporedimo sa sljedećim:

```pycon
>>> tekst = 'Kozala'
>>> for znak in tekst:
...     print(znak)
...    
K
o
z
a
l
a
>>>
```

U tom smo slučaju izgubili brojčani brojač `i`, ali smo dobili znakovni brojač `znak`.

Funkcija `len()` nam ovdje nije potrebna jer nakon kruga gdje `znak` postaje zadnji znak u varijabli `tekst`, petlja se sama prekida.

```python
for znak in tekst:
    if znak == slovo_za_pretrazivanje:
        nadjeno += 1
```

Jednostavno, zar ne?

  <hr />
</details>



<!--                                                                                                                        ZNAMENKE 2 -->

<details>
  <summary><em>7. Znamenke (2)</em></summary>
  <hr />

U prijašnjem zadatku sa znamenkama imali smo zgodno ograničenje da uneseni broj mora imati točno tri znamenke.

Što se događa kad se to ograničenje ukloni? Kad uneseni broj može imati jednu ili šest ili pak tisuću znamenki?

Rješenje slijedi naknadno... 😉

  <hr />
</details>




