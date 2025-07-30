"""
**************************************************
nazwa klasy: Film
pola: title - przechowuje tytul filmu
      num_of_rental - przechowuje liczbe wypozyczen filmu
metody: set_title(new_title) -> None -ustawia tytul filmu 
        get_title() -> str - zwraca tytul filmu
        get_num_of_rental() -> int - zwraca liczbe wypozyczen
        increment() -> None - inkrementuje liczbe wypozyczen
informacje: Klasa reprezentuje film w systemie wirtualnej wypozyczalni
autor: Grzegorz Tereszkiewicz
**************************************************
"""

class Film:
    MAX_LENGHT_TITLE: int = 20

    def __init__(self) -> None:
        self.__title: str = ""
        self.__num_of_rental: int = 0
    
    def set_title(self, new_title: str) -> None: 
        if len(new_title) <= film.MAX_LENGHT_TITLE: self.__title = new_title
        else: return "Błąd: Tytuł może mieć maksymalnie 20 znaków, a twój ma ich: "+ str(len(new_title))
    
    def get_title(self) -> str: return self.__title 

    def get_num_of_rental(self) -> int: return self.__num_of_rental

    def increment(self) -> None: self.__num_of_rental += 1

def main():
# Inicjalizacja obiektu film
    Film = Film("Hobbit")
    print(f"Tytuł: {Film.get_title()}")
    print(f"Ilość wypożyczeń: {Film.get_num_of_rental()}\n")

# Test ograniczenia długości tytulu
    print(f"Test ograniczenia długości tytulu{Film.set_title("Bardzo długi tytuł, który sprawdza działanie ograniczenia")}")
    print(f"Tytuł: {Film.get_title()}\n")

# Test inkrementacji ilości wypożyczeń
    print(f"Test ilości wypożyczeń{Film.increment()}")
    print(f"Ilość wypożyczeń: {Film.get_num_of_rental()}\n")
    
if __name__ == "__main__": main()