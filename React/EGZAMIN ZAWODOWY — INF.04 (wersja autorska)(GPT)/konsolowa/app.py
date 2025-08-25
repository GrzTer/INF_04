import random


class Matrix:
    def __init__(self, n: int) -> None:
        self.__n = n
        self.__tablica = [[random.randint(1, 99) for _ in range(n)] for _ in range(n)]

    def wypisz(self) -> None:
        for row in self.__tablica:
            print(" ".join(f"{val:3d}" for val in row))

    def suma_diagonali(self) -> int:
        return sum(self.__tablica[i][i] for i in range(self.__n))

    def suma_antydiagonali(self) -> int:
        return sum(self.__tablica[i][self.__n - 1 - i] for i in range(self.__n))

    def indeks_wiersza_max_sum(self) -> int:
        sums = [sum(row) for row in self.__tablica]
        return max(range(self.__n), key=lambda i: sums[i])

    # /*********************************************
    # nazwa: obroc_o_90stopni
    # opis: Obraca macierz N×N o 90 stopni w prawo (in-place).
    # parametry: brak
    # zwracany typ i opis: None – modyfikuje stan obiektu
    # autor: Grzegorz Tereszkiewicz
    # *********************************************/
    def obroc_o_90stopni(self) -> None:
        self.__tablica = [list(row) for row in zip(*self.__tablica[::-1])]

    def randomizuj(self, min_val: int, max_val: int) -> None:
        self.__tablica = [
            [random.randint(min_val, max_val) for _ in range(self.__n)]
            for _ in range(self.__n)
        ]


def czytaj_N() -> int:
    while True:
        try:
            n = int(input("Podaj rozmiar N (3..10): "))
            if 3 <= n <= 10:
                return n
            print("Błąd: N musi być w zakresie 3..10.")
        except ValueError:
            print("Błąd: podaj liczbę całkowitą.")


def main():
    N = czytaj_N()
    M = Matrix(N)

    print(f"\nMacierz początkowa ({N}x{N}):")
    M.wypisz()

    print("\nSuma przekątnej głównej:", M.suma_diagonali())
    print("Suma przekątnej pobocznej:", M.suma_antydiagonali())
    print(
        "Indeks wiersza o największej sumie (0-indeksowany):",
        M.indeks_wiersza_max_sum(),
    )

    M.obroc_o_90stopni()
    print("\nMacierz po obrocie o 90 stopni w prawo:")
    M.wypisz()


if __name__ == "__main__":
    main()

    # 1 2 3    7 4 1
    # 4 5 6 -> 8 5 2 (90^∘)
    # 7 8 9    9 6 3
    #   |
    #   V
    # 1 4 7
    # 2 5 8
    # 3 6 9
    # (transpozycja)
