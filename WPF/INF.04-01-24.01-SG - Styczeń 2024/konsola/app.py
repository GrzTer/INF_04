"""Złe podejście
from operator import add

class Pesel:
    def __init__(self, numPesel: list[int] = [55030101193]):
        self.__numPesel = numPesel

    def getPesel(self): return self.__numPesel

    # Sprawdzenie poprawności PESEL'a
    def sprawdzPesel(self):
        waga = [1]*11
        # 1
        for i in range(len(self.__numPesel)):
            if i == 0 or i == 4 or i == 8: waga[i] = i * 1
            if i == 3 or i == 5 or i == 9: waga[i] = i * 3
            if i == 2 or i == 6: waga[i] = i * 7
            if i == 3 or i == 7: waga[i] = i * 9
        # 2
        S = operator.add(waga)
        # 3
        M = S % 10
        # 4
        R = 0 if M == 0 else 10 - M
        # 5
        return self.__numPesel[-1] == R

    # Sprawdzenie płci
    def sprawdzPlec(self):
        if self.__numPesel[-2] % 2 == 0: return "K"
        else: return "M"


def main():
    pesel = Pesel(input("Podaj swój PESEL: "))

    # Test poprawności PESEL'a
    print(f"Podany PESEL to: {pesel.getPesel}, jest on: {"True: Poprawny" if pesel.sprawdzPesel == True else "False: Niepoprawny"}")

    # Test płci podanego PESEL'a
    print(f"Płeć podanego PESEL'a to: {pesel.sprawdzPlec()}")

if __name__ == "__main__": main()
"""


class Pesel:
    """
    Klasa reprezentująca numer PESEL i udostępniająca metody do:
        - określenia płci (sprawdz_plec)
        - weryfikacji sumy kontrolnej (sprawdz_sume_kontrolna)
    """

    def __init__(self, pesel: str):
        """
        Inicjalizacja obiektu PESEL:
        :param pesel: 11-cyfrowy numer jako string
        """
        self.pesel = pesel

    def sprawdz_plec(self) -> str:
        """
        Zwraca:
            - 'K' dla żęskiej (10. cyfra parzysta)
            - 'M' dla męskiej (10. cyfra nieparzysta)
            - '?' w przypadku nieprawidłowego formatu PESEL
        """
        if len(self.pesel) != 11 or not self.pesel.isdigit():
            return "?"
        dziesiata = int(self.pesel[-2])
        return "K" if dziesiata % 2 == 0 else "M"

    def sprawdz_sume_kontrolna(self) -> bool:
        """
        Weryfikuje sumę kontrolną zgodnie z wagami:
        [1,3,7,9,1,3,7,9,1,3]
        Algorytm:
            1) suma = ∑ (cyfra_i * waga_i) dla i = 0..9
            2) M = suma % 10
            3) R = (0 jeśli M == 0, w przeciwnym wypadku 10 - M)
            4) porównanie R z ostatnią (11.) cyfrą PESEL
        Zwraca True gdy się zgadza, False w przeciwnym razie lub przy błędnym formacie PESEL.
        """
        if len(self.pesel) != 11 or not self.pesel.isdigit():
            return False
        wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        suma = sum(int(d) * w for d, w in zip(self.pesel[:10], wagi))
        M = suma % 10
        R = 0 if M == 0 else 10 - M
        return R == int(self.pesel[-1])


def main():
    print("=== Walidator numeru PESEL ===")
    surowy = input(
        "Podaj numer PESEL (11 cyfr),\n"
        "lub wciśnij `ENTER`, aby użyć domyślnego [55030101193]: "
    ).strip()

    if not surowy:
        surowy = "55030101193"
        print(f"Używam domyślnego PESEL: {surowy}\n")

    pesel = Pesel(surowy)

    # 1) Płeć
    plec = pesel.sprawdz_plec()
    if plec == "K":
        print("Płeć: Kobieta")
    elif plec == "M":
        print("Płeć: Mężczyzna")
    else:
        print("Płeć: nie można określić (nieprawidłowy format PESEL)")

    # 2) Suma kontrolna
    if pesel.sprawdz_sume_kontrolna():
        print("Suma kontrolna: jest poprawna ⩗")
    else:
        print("Suma kontrolna jest: NIEPOPRAWNA ⨉")


if __name__ == "__main__":
    main()
