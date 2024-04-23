# Rješenja zadataka

<details>
  <summary><em>1. Kašnjenje</em></summary>

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

Usporedi kod iznad s kodom na poveznici ispod:

[izbori.py](https://github.com/oskozala/python-zadaci/blob/main/rjesenja/izbori.py)

*Jesmo li mogli umjesto `dob >= 18` koristiti `dob > 17`? Nije li to isto, ako govorimo o prirodnim brojevima?*

Je, isto je i program bi se isto i izvodio. Pitanje je jedino što je jasnije nekome tko pročita kod prvi put? Brojka `18` će nam već na prvi pogled jasnije odrediti da je netko punoljetan, nitko ni u svakodnevnom govoru ne kaže da je punoljetna osoba ona koja ima više od 17 godina. 🙂
  
</details>
