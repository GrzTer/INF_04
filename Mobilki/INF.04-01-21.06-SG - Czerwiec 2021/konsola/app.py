class Tablica:
    ROZMIAR_TABLICY = 10

    def __init__(self) -> None:
        self.tablica: list[int] = []

    def przygotuj_tablice(self) -> None:
        self.tablica = []
        for i in range(self.ROZMIAR_TABLICY):
            while True:
                try:
                    self.tablica.append(int(input(f"Podaj liczbę {i + 1}/10: ")))
                    break
                except ValueError:
                    print("To nie jest liczba całkowita. Spróbuj ponownie.")

    # /********************************************************
    # * nazwa funkcji: sortuj_przez_wybieranie
    # * parametry wejściowe: brak
    # * wartość zwracana: brak - sortuje w miejscu tablicę self.tablica
    # * autor: Grzegorz Tereszkiewicz
    # * ****************************************************/
    def sortuj_przez_wybieranie(self) -> None:
        for i in range(len(self.tablica) - 1):
            indeks_max = self.__szukaj_maksimum(i)
            if indeks_max != i:
                self.tablica[i], self.tablica[indeks_max] = (
                    self.tablica[indeks_max],
                    self.tablica[i],
                )

    # /********************************************************
    # * nazwa funkcji: __szukaj_maksimum
    # * parametry wejściowe: start (int) - index początku zakresu przeszukiwania
    # * wartość zwracana: index_max (int) - index największego elementu w zakresie [start..n-1]
    # * autor: Grzegorz Tereszkiewicz
    # * ****************************************************/
    def __szukaj_maksimum(self, start: int) -> int:
        indeks_max = start
        for i in range(start + 1, len(self.tablica)):
            if self.tablica[indeks_max] < self.tablica[i]:
                indeks_max = i
        return indeks_max

    def wyswietl(self, naglowek: str = "Elementy tablicy: ") -> None:
        print(naglowek)
        print(" ".join(map(str, self.tablica)))


def main():

    tablica = Tablica()  # Inicjalizacja objektu

    tablica.przygotuj_tablice()  # Przygotuj tablice, pobierz z klawiatury

    tablica.wyswietl("Przed sortowaniem: ")  # Wyswietlenie elementów tablicy

    tablica.sortuj_przez_wybieranie()  # Sortuj tablice

    tablica.wyswietl("Po sortowaniu malejąco: ")  # Wyswietlenie elementów tablicy


if __name__ == "__main__":
    main()
