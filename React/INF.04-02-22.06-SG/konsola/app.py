"""Klasa reprezentująca osoby"""


class Osoba:
    liczba_instancji = 0  # Statyczne pole zliczające instacje

    def __init__(
        self, id=0, imie=""
    ):  # Konstruktor. Przyjmuje `id` i `imie` z domyślnymi wartościami `0` i `(Pusty napis)`
        self.__id = id
        self.__imie = imie
        Osoba.liczba_instancji += 1

    def wypisz_powitanie(
        self, argument
    ):  # Wypisuje powitanie z `imie`niem lub 'Brak danych' jeżeli nie ma `imie` w objekcie nie jest wypełnione
        if self.__imie:
            print(f"Cześć {argument}, mam na imię {self.__imie}")
        else:
            print("Brak danych")

    def kopiuj(
        self, inna_osoba
    ):  # Kopiuje `id` i `imie` z `innej_osoby` "inną instancje objektu tej klasy"
        self.__id = inna_osoba.__id
        self.__imie = inna_osoba.__imie
        Osoba.liczba_instancji += 1

    def __str__(self):
        return f"Osoba(id={self.__id}, imie='{self.__imie}')"
