super — zrobiłem nową iterację zadania w duchu INF.04: część I to **inne** zadanie konsolowe niż w Twoich arkuszach, a część II to **aplikacja webowa w React.js**. Format, język poleceń, wymagania dot. dokumentacji, struktura katalogów i styl zrzutów nawiązują do opublikowanych arkuszy (np. 2024/2025), żeby pasowało do “egzaminowego” klimatu. W kilku miejscach wskazuję też szablony komentarzy/deliverables, które są zgodne z tym, co widzisz w arkuszach (nagłówki funkcji, struktura folderów, czas 180 min itd.).  &#x20;

# EGZAMIN ZAWODOWY — INF.04 (wersja autorska)

**Czas trwania:** 180 minut
**Rezultaty oceniane:** implementacja/kompilacja/uruchomienie, aplikacja konsolowa, aplikacja web (React.js), dokumentacja. (Układ i punkt ciężkości jak w arkuszach CKE. )

## Instrukcja dla zdającego (skrót)

Utwórz folder nazwany swoim numerem (PESEL lub numer paszportu). W nim podfoldery: `konsolowa`, `webowa`, `dokumentacja`. Po wykonaniu każdej aplikacji spakuj **cały projekt** do archiwum (`konsola.zip` / `web.zip`), a do podfolderu dołącz także **pliki źródłowe, które modyfikowałeś** oraz ewentualny plik wykonywalny. (Analogicznie do zapisów w arkuszach 2024/2025.  )

---

## Część I. Aplikacja konsolowa — **Operacje na macierzy kwadratowej**

### Opis zadania

Napisz program konsolowy, który tworzy i przetwarza **macierz kwadratową N×N** (N z przedziału 3..10). Program:

1. Wczytuje z klawiatury liczbę N i **waliduje zakres** (w razie błędu prosi ponownie).
2. Tworzy obiekt klasy `Matrix`, który:

   * ma **prywatne** pola: tablica/lica-lista 2D z liczbami całkowitymi oraz rozmiar `n`,
   * w konstruktorze ustawia `n` i **wypełnia** macierz wartościami pseudolosowymi z zakresu 1..99.
3. Udostępnia metody publiczne:

   * `print()` – wypisuje macierz w formie kolumn wyrównanych do szerokości 3 (np. `  7 23  1 ...`),
   * `sumMainDiagonal()` – zwraca sumę elementów **przekątnej głównej**,
   * `sumSecondaryDiagonal()` – zwraca sumę **przekątnej pobocznej**,
   * `rowWithMaxSum()` – zwraca **indeks wiersza** o największej sumie elementów (pierwszy w razie remisu),
   * `rotateClockwise()` – **obraca macierz o 90° w prawo** (in-place lub zwraca nową macierz) i nic nie zwraca,
   * (opcjonalnie) `randomize(min, max)` – ponownie losuje wartości z podanego zakresu.
4. Program główny:

   * tworzy obiekt `Matrix(N)`, wywołuje `print()`,
   * wypisuje: sumę przekątnej głównej i pobocznej, indeks wiersza o największej sumie,
   * wykonuje `rotateClockwise()`, po czym **ponownie** wyświetla macierz,
   * komunikaty są **zrozumiałe** dla użytkownika (np. „Suma przekątnej głównej: …”).
     (Wymóg czytelnej komunikacji i czystego formatowania — jak w dotychczasowych arkuszach.  )

### Założenia techniczne

* Język: **C++ / C# / Java / Python** (jeden z dostępnych na stanowisku).
* Tablica w Pythonie może być listą list.
* **Brak zmiennych globalnych** w wersji strukturalnej; preferowana wersja **obiektowa** (analogiczny rygor jak w 2024/2025).&#x20;
* **Czytelny kod**, znaczące nazwy, brak gotowców rozwiązujących całość „za Ciebie”.

### Dokumentacja w kodzie (konsola)

Nad implementacją **co najmniej jednej** metody klasy (`rotateClockwise` lub innej) wstaw komentarz–nagłówek wg wzoru używanego w arkuszach, np.:

```
/*********************************************
 nazwa: rotateClockwise
 opis: Obraca macierz N×N o 90 stopni w prawo (in-place).
 parametry: brak
 zwracany typ i opis: void – modyfikuje stan obiektu
 autor: <NUMER ZDAJĄCEGO>
*********************************************/
```

(Schemat komentarza odpowiada stylom z 2024/2025.  )

### Co oddajesz (konsola)

W `konsolowa/`: `konsola.zip` (cały projekt), **źródło** z klasą `Matrix`, plik wykonywalny (jeśli powstał). (Struktura jak w arkuszach. )

---

## Część II. Aplikacja webowa — **React.js „Katalog kursów” (filtry + zapisy)**

Zbuduj **jednokomponentową** aplikację front-end w **React.js**, która prezentuje listę kursów i umożliwia:

* filtrowanie po kategoriach **(Frontend / Backend / DevOps)** za pomocą **przełączników (switch)**,
* inkrementację licznika „Zapisanych” dla danego kursu po kliknięciu przycisku **„Zapisz się”**.

To nawiązuje do wymagań z web-owego zadania 2025 (filtry przez przełączniki, inkrementacja licznika), ale na **innym modelu danych** i bez galerii zdjęć. Dopuszcza się wykorzystanie **Bootstrap** (import w React: `import 'bootstrap/dist/css/bootstrap.css';`) oraz styl pracy ze **switchami** i **przyciskami** jak w tabeli z arkusza 2025.&#x20;

### Dane wejściowe

Utwórz w komponencie tablicę obiektów (możesz skopiować z `dane.txt` na wzór pracy z plikiem w arkuszu 2025 — tutaj jednak wpisujesz ją bezpośrednio w kodzie):
`[{ id, title, filename?, category, level, enrolled }]`

* `category`: `1`=Frontend, `2`=Backend, `3`=DevOps,
* `enrolled`: liczba zapisanych (startowa różna dla kursów).
  (Wzorowane na polach używanych w danych do galerii, ale dopasowane do „kursów”. )

> Jeśli chcesz, możesz dodać miniatury kursów i trzymać pliki w `public/assets` analogicznie do wymogu „assets” w arkuszu 2025 – nie jest to jednak obowiązkowe, bo tu sednem jest logika filtrów i liczników.&#x20;

### Widok i zachowanie

* Nagłówek `<h1>`: **„Katalog kursów”**.
* **Trzy przełączniki (switch/checkbox)** domyślnie **włączone**: *Frontend*, *Backend*, *DevOps* (w jednej linii, klasy `.form-check`, `.form-check-inline`, `.form-switch` z Bootstrap – patrz przykład w tabeli 2025).&#x20;
* Lista kart (siatka 2–3 w rzędzie, responsywnie). Każda karta:

  * tytuł kursu, poziom (np. „Beginner/Intermediate/Advanced”),
  * napis **„Zapisanych: X”**,
  * przycisk **„Zapisz się”** (np. `btn btn-success`).
* **Filtrowanie:** renderuj tylko kursy, których kategoria ma **włączony** przełącznik (jak w egzemplarzu z galerią).&#x20;
* **Zapis:** kliknięcie **„Zapisz się”** zwiększa `enrolled` tego kursu **o 1** (stan w React), a liczba **od razu** aktualizuje się na ekranie. (Tożsame semantycznie z liczbą „pobrań” w roku 2025, ale w innym kontekście. )
* **Styl:** użyj Bootstrap (import jak wyżej). Zaokrąglone rogi, niewielkie marginesy (na wzór formatowania z galerii).&#x20;
* **Kod:** jedna zgrabna struktura komponentu (np. `App.jsx`), pętle/warunki do renderowania kart (wymóg uniwersalności jak w 2025 — nie zakładaj stałej liczby pozycji).&#x20;

### Co oddajesz (web)

W `webowa/`: `web.zip` (cały projekt React), **pliki źródłowe** komponentu (`App.jsx`/`App.tsx`, ewentualnie `App.css`) i inne modyfikowane pliki. (Zgodnie z sekcją “Kod aplikacji przygotuj do nagrania…” w arkuszu 2025. )

---

## Część III. Dokumentacja (obie aplikacje)

1. **Zrzuty ekranu** obejmujące cały ekran z paskiem zadań:

   * `konsola1, konsola2, ...` – uruchomienie, po obrocie macierzy, itp.
   * `web1, web2, ...` – stan początkowy (wszystkie filtry on), różne kombinacje filtrów, po wielokrotnym „Zapisz się”.
     (Format i nazewnictwo jak w 2024/2025.  )
2. W **kodzie konsolowym** — nagłówek funkcji/metody wg wzorca (por. listingi z arkuszy).&#x20;
3. Dokument **`egzamin`** (edytor tekstu) z informacjami:

   * system operacyjny, IDE, języki, (dla web) użyta biblioteka (React),
   * krótkie komentarze do wykonanej pracy,
   * wklejone i podpisane zrzuty.
     (Zgodnie z wymaganiami dokumentacji w arkuszach.  )

---

## Kryteria techniczne i organizacyjne (podsumowanie)

* **Czytelny kod**, znaczące nazwy, logiczna komunikacja z użytkownikiem. (Stały wymóg we wszystkich arkuszach. )
* **Struktura katalogów** i **archiwa projektów** w odpowiednich podfolderach. (Jak w 2024/2025.  )
* **Bootstrap w React** — sposób włączenia i przykładowe klasy switch/przycisków dokładnie tak, jak w tabeli w zadaniu 2025 (import w React, markup switchy, klasy `btn-*`).&#x20;

Chcesz, żebym dopisał gotowy **starter `App.jsx`** z logiką filtrów/zapisów oraz szkieletem klasy `Matrix` w Twoim wybranym języku (C++/C#/Java/Python)? Mogę od razu wkleić kod.
