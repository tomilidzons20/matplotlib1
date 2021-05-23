import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

# Zad1
# Na wykresie wyświetl wykres liniowy funkcji
# f(x) = 1/x dla x ϵ [20, 40].
# Dodaj etykietę do linii wykresu i wyświetl legendę.
# Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’)
# oraz ustaw zakres osi na (0.02, 0.05) oraz (20, długość wektora x).

print("Zad1,2")
funkcja = [1 / x for x in range(20, 41)]
plt.plot(range(20, 41), funkcja, "bo--", label="1/x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axis([20, 40, 0.02, 0.05])
plt.legend()

# Zad2
# Zmodyfikuj wykres z zadania 1 tak,
# żeby styl wykresu wyglądał tak jak na poniższym zrzucie ekranu.

plt.title("Wykres funkcji f(x) dla x[20,40]")
plt.show()

# Zad3
# Na jednym wykresie wygeneruj wykresy funkcji
# sin(x) oraz cos(x) dla x ϵ [0, 45] z krokiem 0.1.
# Dodaj etykiety i legendę do wykresu.

print("\nZad3")
zakres = np.arange(0, 45, 0.1)
funkcjas = np.sin(zakres)
funkcjac = np.cos(zakres)
plt.plot(zakres, funkcjas, label="sin(x)")
plt.plot(zakres, funkcjac, label="cos(x)")
plt.legend()
plt.show()

# Zad4
# Dodaj drugi wykres funkcji sinus do zadania 3 i zmodyfikuj
# parametry funkcji, tak aby osiągnąć efekt podobny do tego
# na poniższym zrzucie ekranu.

print("\nZad4")
funkcjas1 = np.sin(zakres) + 2
funkcjas2 = np.sin(zakres) * -1
plt.plot(zakres, funkcjas1, label="sin(x)")
plt.plot(zakres, funkcjas2, label="sin(x)")
plt.title("Wykres sin(x), sin(x)")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend(loc="center left")
plt.show()

# Zad5
# Korzystając ze zbioru danych Iris
# (https://archive.ics.uci.edu/ml/datasets/iris)
# wygeneruj wykres punktowy, gdzie wektor x to wartość ‘sepal length’
# a y to ‘sepal width’, dodaj paletę kolorów c na przykładzie
# listingu 6 a parametr s niech będzie wartością absolutną z
# różnicy wartości poszczególnych elementów wektorów x oraz y.

print("\nZad5")
df = pd.read_csv("iris.data", sep=",")
data = {"sl": df.iloc[:, 0],
        "sw": df.iloc[:, 1],
        "c": np.random.randint(0, 50, 149),
        "skala": []}
data["skala"] = np.abs(data["sl"] - data["sw"]) * 20
plt.scatter("sl", "sw", c="c", s="skala", data=data)
plt.show()

# Zad6
# Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci przedstawiony w lekcji 8.
# Następnie na jednym płótnie wyświetl 3 wykresy (jeden wiersz i 3 kolumny).
# Dodaj do wykresów stosowne etykiety. Poustawiaj różne kolory dla wykresów.
# - 1 wykres – wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w całym okresie.
# - 2 wykres – wykres liniowy, gdzie będą dwie linie, jedna dla ilości urodzonych kobiet,
# druga dla mężczyzn dla każdego roku z osobna.
# Czyli y to ilość narodzonych kobiet lub mężczyzn (dwie linie), x to rok.
# - 3 wykres – wykres słupkowy przedstawiający sumę urodzonych dzieci w każdym roku.

print("\nZad6")
df = pd.read_excel("imiona.xlsx", header=0)
# wykres1
wykres1 = df.groupby(["Plec"]).sum("Liczba")
# wykres2
wykres2a = df.where(df["Plec"] == "K").groupby(["Rok"]).agg({"Liczba": ["sum"]})
wykres2b = df.where(df["Plec"] == "M").groupby(["Rok"]).agg({"Liczba": ["sum"]})
lata = df["Rok"].unique()
plci = df["Plec"].unique()
# wykres3
wykres3 = df.groupby(["Rok"]).sum("Liczba")

plt.subplots(1, 3, figsize=(16, 9))
plt.subplot(1, 3, 1)
plt.bar(plci, wykres1["Liczba"], color="y")
plt.title("Liczba urodzonych dzieci danej plci")
plt.xlabel("Plec")
plt.ylabel("MLN")
plt.subplot(1, 3, 2)
plt.plot(lata, wykres2a, label="K", color="pink")
plt.plot(lata, wykres2b, label="M", color="blue")
plt.title("Liczba urodzonych dzieci w danym roku i danej plci")
plt.xlabel("Urodzonych w danym roku")
plt.ylabel("Ilośc urodzonych")
plt.xticks(lata, rotation=60)
plt.legend()
plt.subplot(1, 3, 3)
plt.bar(lata, wykres3["Liczba"], color="g")
plt.title("Liczba urodzonych dzieci w danym roku")
plt.xlabel("Rok")
plt.ylabel("Ilosc urodzonych")
plt.xticks(lata, rotation=60)
plt.tight_layout()
plt.show()

# Zad7
# Korzystając z pliku zamówienia.csv (Pandas) policz sumy zamówień
# dla każdego sprzedawcy i wyświetl wykres kołowy z procentowym
# udziałem każdego sprzedawcy w ogólnej sumie zamówień.
# Poszukaj w Internecie jak dodać cień do takiego wykresu
# i jak działa atrybut ‘explode’ tego wykresu.
# Przetestuj ten atrybut na wykresie.

df = pd.read_csv("zamowienia.csv", header=0, sep=";", decimal=".")
sz = df.groupby("Sprzedawca")["idZamowienia"].nunique()
sp = df["Sprzedawca"].unique()
eksplozja = (0, 0, 0.1, 0.1, 0.1, 0.1, 0, 0, 0)


def pl(pct, br):
    absolute = int(np.ceil(pct / 100. * np.sum(br)))
    return "{:.1f}% \n({}/{})".format(pct, absolute, sum(sz))


wedges, texts, autotexts = plt.pie(sz, labels=sp, autopct=lambda pct:
                                   pl(pct, sz), textprops=dict(color="black"),
                                   radius=1.2, labeldistance=1.02, startangle=70, shadow=True, explode=eksplozja)
plt.setp(autotexts, size=14, weight="bold")
plt.title("Suma zamowien dla sprzedawcow")
plt.legend(title="Sprzedawcy", loc="lower left", bbox_to_anchor=(-0.2, -0.1))
plt.show()
