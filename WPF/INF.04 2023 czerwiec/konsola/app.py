import math

N = 100  # Stała zakresu


# ****************************************************
# nazwa funkcji: przygotuj_sito
# parametry wejściowe: sito (list[bool]) - indeks i oznacza liczbę i
#                         n (int) - górna granica zakresu
# wartość zwracana: brak
# informacje: Inicjalizuje tablicę długości n+1, ustawia True dla 2..n,
#             a 0 i 1 na False (przygotowanie do sita Eratostenesa). 
# autor: Grzegorz Tereszkiewicz
# ****************************************************
def przygotuj_sito(sito: list[bool], n: int) -> None:
    if n < 2:
        raise ValueError("Podaj odpowiedni zakres szukanych liczb pierwszych np. 2..100")
    sito.clear()

    sito.extend([True] * (n + 1))

    sito[0] = sito[1] = False



# ****************************************************
# nazwa funkcji: wykonaj_sito
# parametry wejściowe: sito (list[bool]) - lista bool przygotowana przez przygotuj sito
# wartość zwracana: brak
# informacje: Implementuje sito Erastotenesa: dla dzielników <= [√n]
#             wykreśla (ustawia False) ich wielokrotności od i*i do n.
# autor: Grzegorz Tereszkiewicz
# ****************************************************
def wykonaj_sito(sito: list[bool]) -> None:
    n = len(sito) - 1
    for dzielnik in range(2, math.isqrt(n) + 1):
        if sito[dzielnik]:
            for wielokrotnosc in range(dzielnik * dzielnik, n + 1, dzielnik):
                sito[wielokrotnosc] = False


# ****************************************************
# nazwa funkcji: wypisz_liczby_pierwsze
# parametry wejściowe: sito (list[bool]) - tablica liczb pierwszych
#                         separator (str) - separator wypisywanych liczb pierwszych, domyślnie ustawiony na `,` 
# wartość zwracana: brak
# informacje: Wypisuje komunikat i liczby pierwsze z zakresu 2..n, odzielone podanym separatorem.
# autor: Grzegorz Tereszkiewicz
# ****************************************************
def wypisz_liczby_pierwsze(sito: list[bool], separator: str = ", ") -> None:
    n = len(sito) - 1
    liczby_pierwsze = [str(i) for i, is_prime in enumerate(sito) if is_prime]
    print(f"Liczby pierwsze w 2..{n}:", separator.join(liczby_pierwsze))


def main() -> None:
    sito: list[bool] = []
    try:
        przygotuj_sito(sito, N)
    except ValueError as e:
        print(e)
        return
    wykonaj_sito(sito)

    wypisz_liczby_pierwsze(sito)


if __name__ == "__main__":
    main()
