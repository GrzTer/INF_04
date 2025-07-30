"""**********************************************
nazwa funkcji: NWD
opis funkcji: Liczy Największy Wspólny Dzielnik
parametry: a – pierwsza liczba wprowadzana do funkcji
           b – druga liczba wprowadzana do funkcji
zwracany typ i opis: Zwraca liczbę całkowitą reprezentującą największy dzielnik wspólny dla obu liczb
autor: Grzegorz Tereszkiewicz
***********************************************
"""
def NWD(a: int, b: int) -> int: return (a if a == b else NWD(a - b, b) if a > b else NWD(a, b - a)) if b > 0 and a > 0 else -1

def main():
    a = 100
    b = 24
    print(f"Dla a = {a} i b = {b}\nNajwiększy Wspólny Dzielnik jest równy {NWD(a, b)}")

if __name__ == "__main__": main()