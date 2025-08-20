import random


def wypelnij_tablice(n: int = 50, min_val: int = 1, max_val: int = 100) -> list[int]:
    return [random.randint(min_val, max_val) for _ in range(n)]


# ******************************************************
#  nazwa funkcji: przeszukaj_tablice
#  argumenty: tab - (list[int]) Lista licz całkowitych pseudolosowych, w której prowadzone jest wyszukiwanie.
#               x - (int) Szukana wartość całkowita.
#  typ zwracany: (int), indeks pierwszego wystąpienia x (indeks 0-based) w przypadku braku `x` w `tab`, zwracane jest -1.
#  informacje: Algorytm liniowego przeszukiwania z wartownikiem (sentinel search). Na koniec listy tymczasowo jest dodawany wartownik równy `x`, pętla przechodzi kolejne elementy aż do trafienia `x`, po czym wartownik jest usuwany. Złożoność czasowa O(n).
#  autor: Grzegorz Tereszkiewicz
# *****************************************************
def przeszukaj_tablice(tab: list[int], x: int) -> int:
    n = len(tab)
    tab.append(x)
    i = 0
    while tab[i] != x:
        i += 1
    tab.pop()
    return -1 if i == n else i


def wyswietl_tablice(tab: list[int]) -> None:
    print(", ".join(map(str, tab)))


def main():
    try:
        x = int(input("Podaj szukaną liczbę (1-100): "))
    except ValueError:
        print("Błąd: wpisz liczbę całkowitą.")
        return

    if not (1 <= x <= 100):
        print("Błąd: liczba poza zakresu 1-100.")
        return

    tablica = wypelnij_tablice()
    index = przeszukaj_tablice(tablica, x)

    print("\nTablica:")
    wyswietl_tablice(tablica)

    if index == -1:
        print(f"\nNie znaleziono wartości {x} w tablicy.")
    else:
        print(f"\nZaleziono wartości {x} pod indeksem {index}.")


if __name__ == "__main__":
    main()
