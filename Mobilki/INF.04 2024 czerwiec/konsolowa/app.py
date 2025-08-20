import random


def pobierz_liczbe_rzutow() -> int:
    """
    ************************************************
    nazwa: pobierz_liczbe_rzutow
    opis: Funkcja pobiera od użytkownika liczbę kostek do rzucenia w przedziale od 3 do 10.
    parametry: brak
    zwracany typ i opis: int - Liczba kostek, którą gracz chce rzucić.
    autor: Grzegorz Tereszkiewicz
    ************************************************
    """
    # Pobiera liczbę kostek dopóki liczba będzie z wymaganego zakresu
    while True:
        liczbaRzutow = int(input("Ile kostek chcesz rzucić?(3 - 10)\n"))
        if 3 <= liczbaRzutow <= 10:  # Przedział 3 - 10
            return liczbaRzutow


def rzuc_kostka(liczbaRzutow: int) -> list[int]:
    """
    ************************************************
    nazwa: rzuc_kostka
    opis: Funkcja losuje wyniki rzutów kostką dla określonej liczby kostek.
    parametry: liczbaRzutow (int) - Liczba kostek do rzucania.
    zwracany typ i opis: list[int] - Liczba wyników rzutów kostkami.
    autor: Grzegorz Tereszkiewicz
    ************************************************
    """
    listaRzutow = []  # inicjacja tablicy
    # Losuje wyniki rzutów kostką tyle razy ile podał gracz
    for rzut in range(liczbaRzutow):
        listaRzutow.append(random.randint(1, 6))  # Dodajemy wynik rzutu do listy
    return listaRzutow


def wypisz_rzuty(listaRzutow: list) -> None:
    """
    ************************************************
    nazwa: wypisz_rzuty
    opis: Funkcja wypisuje wyniki rzutów kostkami.
    parametry: liczbaRzutow (int) - Liczba wyników rzutów kostkami
    zwracany typ i opis: brak
    autor: Grzegorz Tereszkiewicz
    ************************************************
    """
    # Wypisuje tyle wyników rzutów ile jest w tablicy
    for rzut in range(len(listaRzutow)):
        print(f"Kostka {rzut + 1}: {listaRzutow[rzut]}")


def licz_punkty(listaRzutow: list) -> int:
    """
    ************************************************
    nazwa: licz_punkty
    opis: Funkcja losuje wyniki rzutów kostką dla określonej liczby kostek.
    parametry: liczbaRzutow (int) - Liczba wyników rzutów kostkami
    zwracany typ i opis: list[int] - Liczba punktów obliczonych na podstawie powtórzonych wyników.
    autor: Grzegorz Tereszkiewicz
    ************************************************
    """
    liczba_punktow = 0
    # Sumujemy liczby, które powtarzają się co najmniej dwa razy
    for liczba in set(listaRzutow):
        if listaRzutow.count(liczba) >= 2:
            liczba_punktow += liczba * listaRzutow.count(liczba)
    return liczba_punktow


def czy_kontynuowac() -> bool:
    """
    ************************************************
    nazwa: czy_kontynuowac
    opis: Funkcja pyta gracza, czy chce kontynuować.
    parametry: brak
    zwracany typ i opis: bool - Zwraca True, jeśli gracz chce kontynuować, False jeśli chce zakończyć.
    autor: Grzegorz Tereszkiewicz
    ************************************************
    """
    while True:
        wyborGracza = input("Jeszcze raz? (t/n)\n")
        if wyborGracza.lower() == "n":
            return False
        elif wyborGracza.lower() == "t":
            return True


def main():
    kontynuowac = True
    while kontynuowac:
        # 1. Pobiera liczbę kostek
        liczbaRzutow = pobierz_liczbe_rzutow()

        # 2. Losuje rzuty kostek
        rzuty = rzuc_kostka(liczbaRzutow)

        # 3. Wypisz wylosowane rzuty
        wypisz_rzuty(rzuty)

        # 4. Zlicz punkty
        wynik = licz_punkty(rzuty)
        print(f"Zdobyte punkty: {wynik}")

        # 5. Kontynuować?
        kontynuowac = czy_kontynuowac()


if __name__ == "__main__":
    main()
