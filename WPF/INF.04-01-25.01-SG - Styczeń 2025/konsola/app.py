"""
**********************************************
nazwa klasy: Tablica
opis klasy: Klasa reprezentująca tablicę liczb całkowitych, której rozmiar jest podawany przez użytkownika.
            Klasa zawiera metody do manipulacji danymi w tablicy: wyświetlanie elementów, wyszukiwanie,
            filtrowanie liczb nieparzystych oraz obliczanie średniej arytmetycznej wartości w tablicy.

nazwa metody: __init__
opis metody: Konstruktor klasy Tablica. Przyjmuje rozmiar tablicy jako argument, generuje tablicę liczb całkowitych 
             w zakresie od 1 do 1000 oraz ustawia rozmiar tablicy.
parametry: rozmiarTablicy (int) - liczba elementów w tablicy
zwracany typ i opis: brak

nazwa metody: get_elementy_tablicy
opis metody: Zwraca listę wszystkich elementów znajdujących się w tablicy.
parametry: brak
zwracany typ i opis: list[int] - lista liczb całkowitych zawierająca elementy tablicy

nazwa metody: znajdz
opis metody: Szuka podanego przez użytkownika argumentu w tablicy i zwraca indeks pierwszego wystąpienia tego elementu.
             Jeśli element nie zostanie znaleziony, zwraca -1.
parametry: x (int) - wartość do wyszukania w tablicy
zwracany typ i opis: int - indeks elementu w tablicy, lub -1, jeśli element nie został znaleziony

nazwa metody: nieparzyste
opis metody: Zwraca listę liczb nieparzystych znajdujących się w tablicy.
parametry: brak
zwracany typ i opis: list[int] - lista liczb nieparzystych z tablicy

nazwa metody: licz_srednia
opis metody: Oblicza i zwraca średnią arytmetyczną wszystkich elementów w tablicy.
parametry: brak
zwracany typ i opis: float - średnia arytmetyczna wartości w tablicy

autor: Grzegorz Tereszkiewicz
***********************************************
"""

import random

class Tablica:
    def __init__(self, rozmiarTablicy: int):
        # Inicjalizacja tablicy o podanym jako argument rozmiarze
        self.__rozmiarTablicy = rozmiarTablicy
        self.__tablica: list[int] = [random.randint(1, 1000) for i in range(self.__rozmiarTablicy)]

    def get_elementy_tablicy(self) -> list[int]:
        # Zwraca listę elementów tablicy
        return self.__tablica

    def znajdz(self, x) -> int:
        # Szuka wartości `x` w tablicy i zwraca jej index lub -1, jeśli jej nie znaleziono
        return self.__tablica.index(x) if x in self.__tablica else -1

    def nieparzyste(self) -> list[int]:
        # Zwraca listę liczb nieparzystych z tablicy
        return list(filter(lambda x: x % 2 != 0, self.__tablica))

    def licz_srednia(self) -> int:
        # oblicza i zwraca średnią arytmetyczną wartości w tablicy
        return sum(self.__tablica) // self.__rozmiarTablicy




def main():
    # Główna funkcja programu, która testuje metody klasy Tablica
    rozmiarTablicy = int(input("================\nPodaj oczekiwany rozmiar tablicy: "))
    T = Tablica(rozmiarTablicy)

    # Wyświetlanie wszystkich elementów tablicy
    for i in range (rozmiarTablicy):
        print(f"{i}: {T.get_elementy_tablicy()[i]}")

    # Wyszukiwanie liczby w tablicy
    x = int(input("================\nPodaj szukaną liczbę w tablicy: "))
    index = T.znajdz(x)
    if index != -1:
        print(f"Jej index to: {index}")
    else:
        print("")

    # Wyświetlanie liczb nieparzystych i ich liczby
    print(f"================\nLiczby nieparzyste:")
    nieparzyste_liczby = T.nieparzyste()
    for nieparzysta in nieparzyste_liczby:
        print(nieparzysta)
    print(f"Razem nieparzystych: {len(nieparzyste_liczby)}")

    # Obliczanie średniej arytmetycznej
    print(f"================\nŚrednia wszystkich elementów: {T.licz_srednia()}")



if __name__ == "__main__": main()