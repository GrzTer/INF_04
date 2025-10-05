"""
Część I. Aplikacja konsolowa
Napisz program sortujący tablicę metodą przez wybieranie według zamieszczonej dokumentacji:

---
Sortowanie przez wybieranie - jedna z prostszych metod sortowania o złożoności O(n2
). Polega na
wyszukaniu elementu mającego się znaleźć na żądanej pozycji i zamianie miejscami z tym, który jest tam
obecnie. Operacja jest wykonywana dla wszystkich indeksów sortowanej tablicy.
Algorytm przedstawia się następująco:
1. wyszukaj minimalną wartość z tablicy spośród elementów od i do końca tablicy
2. zamień wartość minimalną, z elementem na pozycji i
Gdy zamiast wartości minimalnej wybierana będzie maksymalna, wówczas tablica będzie posortowana
od największego do najmniejszego elementu.

---
Założenia do programu
‒ Program wykonywany w konsoli.
‒ Obiektowy język programowania zgodny z zainstalowanym na stanowisku egzaminacyjnym: C++ lub
C# lub Java lub Python.
‒ Sortowanie odbywa się malejąco, nie wykorzystuje gotowych funkcji do sortowania oraz do szukania
maksimum.
‒ Sortowana jest tablica 10 liczb całkowitych. Tablica jest polem klasy.
‒ Tablica jest wczytywana z klawiatury po uprzednim wypisaniu odpowiedniego komunikatu.
‒ Wszystkie elementy posortowanej tablicy są wyświetlane na ekranie.
‒ Klasa zawiera co najmniej dwie metody: sortującą i szukającą wartość najwyższą. Widzialność
metody szukającej ogranicza się jedynie do klasy.
‒ Metoda szukająca zwraca wartość, w zależności od przyjętej taktyki może być to wartość
maksymalna lub index wartości maksymalnej.
‒ Program powinien być zapisany czytelnie, z zasadami czystego formatowania kodu, należy stosować
znaczące nazwy zmiennych i funkcji.
‒ Dokumentacja do programu wykonana zgodnie z wytycznymi z części III zadania egzaminacyjnego.

---
Część III. Dokumentacja utworzonych aplikacji
Wykonaj dokumentację aplikacji utworzonych podczas egzaminu. W kodzie źródłowym aplikacji konsolowej
utwórz nagłówek metody sortującej i szukającej, według wzoru umieszczonego w listingu 1. Nagłówek
powinien znaleźć się w kodzie źródłowym nad metodą. W miejscu nawiasów <> należy podać nazwę funkcji,
nazwy parametrów (lub słowo „brak”) oraz zwięzłe informacje (kilka słów) – zgodnie ze wzorcem. W miejscu
autor należy podać swój numer PESEL
Listing 1. Wzór dokumentacji funkcji
/********************************************************
* nazwa funkcji: <tu wstaw nazwę funkcji>
* parametry wejściowe: <nazwa parametru> - <co przechowuje>
* wartość zwracana: <co zwraca funkcja – opis>
* autor: <numer PESEL zdającego>
* ****************************************************/
"""

# class SortowaniePrzezWybieranie:
#     def __init__(self, tablica: list[int]) -> None:
#         self.tablica = tablica

#     # /********************************************************
#     # * nazwa funkcji: sortuj_malejaco
#     # * parametry wejściowe: brak
#     # * wartość zwracana: brak (sortuje tablicę w miejscu)
#     # * autor: Grzegorz Tereszkiewicz
#     # * ****************************************************/
#     def sortuj_malejaco(self) -> None:
#         n = len(self.tablica)
#         for i in range(n):
#             max_index = self.__znajdz_indeks_maksymalnej(i, n)
#             self.tablica[i], self.tablica[max_index] = self.tablica[max_index], self.tablica[i]

#     # /********************************************************
#     # * nazwa funkcji: __znajdz_indeks_maksymalnej
#     # * parametry wejściowe: start - początkowy indeks zakresu, end - końcowy indeks zakresu
#     # * wartość zwracana: indeks największego elementu w podanym zakresie
#     # * autor: Grzegorz Tereszkiewicz
#     # * ****************************************************/
#     def __znajdz_indeks_maksymalnej(self, start: int, end: int) -> int:
#         max_index = start
#         for j in range(start + 1, end):
#             if self.tablica[j] > self.tablica[max_index]:
#                 max_index = j
#         return max_index

#     def waliduj(self) -> bool:
#         return len(self.tablica) == 10 and all(isinstance(x, int) for x in self.tablica)


# def main() -> None:
#     print("Podaj 10 liczb całkowitych do posortowania malejąco.")
#     tablica = []
#     while len(tablica) < 10:
#         try:
#             liczba = int(input(f"Podaj liczbę całkowitą ({len(tablica)+1}/10): "))
#             tablica.append(liczba)
#         except ValueError:
#             print("To nie jest liczba całkowita. Spróbuj ponownie.")

#     sorter = SortowaniePrzezWybieranie(tablica)
#     if not sorter.waliduj():
#         print("Błędne dane wejściowe. Program zakończy działanie.")
#         return

#     print("Tablica przed sortowaniem:", sorter.tablica)
#     sorter.sortuj_malejaco()
#     print("Tablica po sortowaniu malejąco:", sorter.tablica)


# if __name__ == "__main__":
#     main()


class SortowaniePrzezWybieranie:
    def __init__(self, tablica: list[int]) -> None:
        self.tablica = tablica

    # /********************************************************
    # * nazwa funkcji: sortuj_malejaco
    # * parametry wejściowe: brak
    # * wartość zwracana: brak (sortuje tablicę w miejscu)
    # * autor: Grzegorz Tereszkiewicz
    # * ****************************************************/
    def sortuj_malejąco(self) -> None:
        n = len(self.tablica)
        for i in range(n):
            max_index = self.__znajdz_index_maksymalnej(i, n)
            self.tablica[i], self.tablica[max_index] = (
                self.tablica[max_index],
                self.tablica[i],
            )

    # /********************************************************
    # * nazwa funkcji: __znajdz_index_maksymalnej
    # * parametry wejściowe: start - początkowy index zakresu, end - końcowy index zakresu
    # * wartość zwracana: index największego elementu w podanym zakresie
    # * autor: Grzegorz Tereszkiewicz
    # * ****************************************************/
    def __znajdz_index_maksymalnej(self, start: int, end: int) -> int:
        max_index = start
        for j in range(start + 1, end):
            if self.tablica[j] > self.tablica[max_index]:
                max_index = j
        return max_index

    def waliduj(self) -> bool:
        return len(self.tablica) == 10 and all(isinstance(x, int) for x in self.tablica)


def main() -> None:
    print("Podaj 10 liczb całkowitych do posortowania malejąco.")
    tablica = []
    while len(tablica) < 10:
        try:
            liczba = int(input(f"Podaj liczbę całkowitą ({len(tablica)+1}/10): "))
            tablica.append(liczba)
        except ValueError:
            print("To nie jest liczba całkowita. Spróbuj ponownie.")
    sorter = SortowaniePrzezWybieranie(tablica)
    if not sorter.waliduj():
        print("Błędne dane wejściowe. Program zakończy działanie.")
        return

    print("Tablica przed sortowaniem:", sorter.tablica)
    sorter.sortuj_malejąco()
    print("Tablica po sortowaniu malejąco:", sorter.tablica)


if __name__ == "__main__":
    main()
