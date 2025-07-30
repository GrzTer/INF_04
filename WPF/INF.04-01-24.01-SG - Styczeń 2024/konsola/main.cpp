#include <iostream>
#include <string>
#include <cctype>   // std::isdigit

class Pesel {
private:
    std::string numer;  // powinien miec dokladnie 11 cyfr

public:
    // Konstruktor przyjmujący numer PESEL jako string
    Pesel(const std::string& pesel) : numer(pesel) {}

    // Zwraca 'K' dla kobiety (parzysta 10. cyfra), 'M' dla mezczyzny (nieparzysta)
    char okreslPlec() const {
        if (numer.size() != 11 || !std::isdigit(numer[9]))
            return '?';  // bląd formatu
        int cyfra = numer[9] - '0';
        return (cyfra % 2 == 0) ? 'K' : 'M';
    }

    // Sprawdza sume kontrolną wg wag: {1,3,7,9,1,3,7,9,1,3}
    bool sprawdźSumaKontrolna() const {
        if (numer.size() != 11)
            return false;

        static const int wagi[10] = {1, 3, 7, 9, 1, 3, 7, 9, 1, 3};
        int suma = 0;

        // oblicz sume wazoną pierwszych 10 cyfr
        for (int i = 0; i < 10; ++i) {
            if (!std::isdigit(numer[i]))
                return false;  // niedozwolony znak
            int d = numer[i] - '0';
            suma += d * wagi[i];
        }

        int M = suma % 10;
        int R = (M == 0) ? 0 : (10 - M);

        // porównaj z 11. cyfrą
        int kontrolna = numer[10] - '0';
        return (R == kontrolna);
    }
};

int main() {
    std::cout << "=== Sprawdzenie poprawnosci numeru PESEL ===\n";

    std::cout << "Podaj numer PESEL (11 cyfr)\n"
              << "(lub wcisnij Enter, aby uzyc domyslnego 55030101193): ";

    std::string wejscie;
    std::getline(std::cin, wejscie);

    if (wejscie.empty()) {
        wejscie = "55030101193";
        std::cout << "Uzywam domyslnego numeru PESEL: " << wejscie << "\n";
    }

    Pesel p(wejscie);

    // 1) Plec
    char plec = p.okreslPlec();
    if (plec == 'K') std::cout << "Plec: Kobieta\n";
    else if (plec == 'M') std::cout << "Plec: Mezczyzna\n";
    else std::cout << "Plec: nie mozna okreslic (niepoprawny format PESEL)\n";

    // 2) Suma kontrolna
    bool sumaOk = p.sprawdźSumaKontrolna();
    if (sumaOk) std::cout << "Suma kontrolna jest zgodna.\n";
    else std::cout << "Suma kontrolna jest NIEZGODNA!\n";

    return 0;
}
