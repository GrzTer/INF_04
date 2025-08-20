def Zadanie_1():
    """*********************************** Walidator PESEL ***********************************"""

    def pobierz_pesel() -> str:
        while True:
            pesel = input("Podaj swój numer PESEL: ")
            
            if len(pesel) == 11 and pesel.isdigit():
                return pesel
            else:
                print("Pesel powinien się składać z 11 cyfr.")


    def sprawdz_plec(pesel: str) -> str:
        if int(pesel[9]) % 2 == 0:
            return "Kobieta"
        else:
            return "Mężczyzna"


    def sprawdz_pesel(pesel: str) -> str:
        if len(pesel) != 11 or not pesel.isdigit():
            return False
        wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        suma = sum(int(c) * w for c, w in zip(pesel[:10], wagi))
        M = suma % 10
        R = 0 if M == 0 else 10 - M
        if R == int(pesel[-1]):
            return "poprawny"
        else:
            return "niepoprawny"

    def main():
        pesel = pobierz_pesel()
        
        print(f"Płeć: {sprawdz_plec(pesel)}")

        print(f"Numer PESEL jest {sprawdz_pesel(pesel)}")

    if __name__ == "__main__":
        main()
if __name__ == "__main__":
    Zadanie_1()