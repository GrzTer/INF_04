"""
********************************************************************

********************************************************************
"""

import random


# Zwraca listę wielkości `size` wypełnioną pseudolosowymi liczbami z przedziału [`low`, `high`].
def pseudolos_lista(size: int = 50, low: int = 1, high=100) -> list[int]:
    return [random.randint(low, high) for _ in range(size)]


def szukanie_wartownik(arr: list[int], x: int) -> int:

    arr.append(x)  # Wstawianie wartownika `x`
    i = 0
    while arr[i] != x:
        i += 1  # Pętla sprawdzająca pierwsze wystąpienie wartownika `x`
    arr.pop()  # Usuwanie wartownika `x`

    return i if i < len(arr) else -1  # Zwracanie wyniku


def main() -> None:
    arr = pseudolos_lista()

    try:
        x = int(input("Podaj liczbę, której mam szukać (1-100): "))
    except ValueError:
        print("To nie jest poprawna liczba całkowita")
        return

    index = szukanie_wartownik(arr, x)

    print("\nTablica:")
    print(*arr)
    if index != -1:
        print(f"\nZnalazłem {x} pod indeksem {index}")
    else:
        print(f"\nW tablicy nie ma liczby {x}.")


if __name__ == "__main__":
    main()
