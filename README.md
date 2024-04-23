# Python (zadaci)

1. [Kašnjenje](README.md#1-kasnjenje)
2. [Izbori](README.md#2-izbori)
3. [Znamenke (1)](README.md#3-znamenke-1)
4. [Sigma](README.md#4-sigma)
5. [Znamenke (2)](README.md#5-znamenke-2)

## *1. Kašnjenje*

Ana je zakasnila na sat. Napiši program koji će izračunati koliko je još Ani minuta ostalo do odmora.

Pretpostavit ćemo da je Ana zakasnila `n` minuta, gdje vrijedi `0 < n < 45`.

|         | **Primjer 1.** | **Primjer 2.** |
|---------|----------------|----------------|
| *Ulaz*  | `17`           | `34`           |
| *Izlaz* | `28`           | `11`           |

<details>
  <summary><em>Rješenje</em></summary>

Krenimo od onoga što nam je poznato i onog što još ne znamo.

**Poznat** nam je podatak da školski sat traje 45 minuta, pa će rješenje nedvojbeno biti `45 - n`, a kako nam program to mora ispisati, koristit ćemo funkciju `print()`.

```python
print(45 - n)
```

**Nepoznat** nam je podatak koliko uopće iznosi `n`, tj. koliko je Ana zakasnila na sat. Da bi to saznali, naprosto ćemo pitati Anu da nam ga upiše koristeći se funkcijom `input()`. Ne smijemo zaboraviti da se unos mora pretvoriti u broj pomoću funkcije `int()`, kako bi mogli s njim nešto i izračunati.

Unos, naravno moramo dodati u kod **prije** ispisa.
```python
n = int(input())
print(45 - n)
```

Kako znamo što se od nas traži, program u ovom obliku nam je jasan. No, kod mora biti čitljiv i nekome tko ne zna što se od nas traži. Usporedi kod iznad s kodom na poveznici ispod.

[kasnjenje.py](https://github.com/oskozala/python-zadaci/blob/main/rjesenja/kasnjenje.py)

Ova dva programa rade na potpuno isti način, jedina razlika je čitljivost koda. ***Čitljivije*** je uvijek ***bolje***, inače bismo mogli napisati program i ovako:

```python
print(45 - int(input()))
```
</details>

___


## *2. Izbori*

Ivan nije siguran može li glasovati na izborima. Nitko mu nije objasnio da to u Hrvatskoj mogu samo punoljetne osobe.

Napiši program koji će Ivanu ispisati poruku `GLASUJ` ukoliko je punoljetan, a u suprotnom neka mu se ispiše samo broj godina koliko još neće imati pravo glasa.

|         | **Primjer 1.** | **Primjer 2.** |
|---------|----------------|----------------|
| *Ulaz*  | `12`           | `22`           |
| *Izlaz* | `6`            | `GLASUJ`       |

<details>
  <summary><em>Rješenje</em></summary>

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

Usporedi kod iznad s kodom na poveznici ispod:

[izbori.py](https://github.com/oskozala/python-zadaci/blob/main/rjesenja/izbori.py)

*Jesmo li mogli umjesto `dob >= 18` koristiti `dob > 17`? Nije li to isto, ako govorimo o prirodnim brojevima?*

Je, isto je i program bi se isto i izvodio. Pitanje je jedino što je jasnije nekome tko pročita kod prvi put? Brojka `18` će nam već na prvi pogled jasnije odrediti da je netko punoljetan, nitko ni u svakodnevnom govoru ne kaže da je punoljetna osoba ona koja ima više od 17 godina. 🙂
  
</details>

___


## *3. Znamenke (1)*

Napiši program koji će zbrojiti znamenke bilo kojeg prirodnog troznamenkastog broja.

|         | **Primjer 1.** | **Primjer 2.** |
|---------|----------------|----------------|
| *Ulaz*  | `124`          | `942`          |
| *Izlaz* | `7`            | `15`           |

___


## *4. Sigma*

Napiši program koji će zbrojiti prvih `n` prirodnih brojeva.

|         | **Primjer 1.** | **Primjer 2.** | **Primjer 3.** |
|---------|----------------|----------------|----------------|
| *Ulaz*  | `3`            | `7`            | `10`           |
| *Izlaz* | `6`            | `28`           | `55`           |

___


## *5. Znamenke (2)*

Napiši program koji će zbrojiti znamenke bilo kojeg prirodnog broja.

|         | **Primjer 1.** | **Primjer 2.** | **Primjer 3.** |
|---------|----------------|----------------|----------------|
| *Ulaz*  | `124`          | `2795`         | `10`           |
| *Izlaz* | `7`            | `23`           | `1`            |

