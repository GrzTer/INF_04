To doskonały moment na wprowadzenie **kontrolek wyboru** (CheckBox i RadioButton). Na egzaminie INF.04 często pojawia się wymóg: „dolicz usługę dodatkową” (CheckBox) lub „wybierz jeden typ” (RadioButton).

Zrefaktoryzujmy zadanie. Zamiast Kina, zrobimy **"Kalkulator Kosztów Podróży"**.

-----

# ZADANIE: Kalkulator Podróży

**Cel:** Aplikacja obliczająca koszt paliwa na trasie.

**Wymagania:**

1.  **Wygląd:** Tło `LightBlue`, tytuł "Podróż - [PESEL]".
2.  **Suwak (Slider):** Spalanie samochodu (od 4.0 do 20.0 l/100km).
3.  **Pole tekstowe:** Dystans w kilometrach.
4.  **NOWOŚĆ – RadioButton (Typ paliwa):**
      * Benzyna (6.50 zł/l)
      * Diesel (7.20 zł/l)
      * LPG (3.00 zł/l)
5.  **NOWOŚĆ – CheckBox (Opcja):** "W obie strony" (podwaja dystans).
6.  **Lista (ListView):** Wyświetla historię obliczeń (Rodzaj paliwa, Dystans, Koszt).
7.  **Alert:** Jeśli koszt podróży przekroczy **500 zł**, wyświetl ostrzeżenie: *"Droga podróż\!"*.

-----

# LEKCJA: CheckBox i RadioButton

Zanim przejdziesz do kodu, musisz wiedzieć, jak „pytać” te kontrolki o ich stan.

### 1\. CheckBox (Ptaszek)

W WPF CheckBox ma dziwną właściwość. Jego `IsChecked` nie jest zwykłym `bool` (prawda/fałsz), tylko `bool?` (prawda/fałsz/**null**).
Dlatego w `if` musisz pisać to w specyficzny sposób:

```csharp
// ŹLE (błąd kompilacji w niektórych wersjach C#):
if (mojCheckBox.IsChecked) { ... } 

// DOBRZE (bezpiecznie):
if (mojCheckBox.IsChecked == true) 
{
    // Zaznaczone
}
```

### 2\. RadioButton (Kropka wyboru)

Radiobuttony działają stadnie. Jeśli wrzucisz je do jednego `StackPanelu`, WPF sam zadba o to, że tylko jeden może być zaznaczony.
W kodzie C\# sprawdzamy je serią `if-ów`:

```csharp
double cena = 0;
if (rbBenzyna.IsChecked == true) cena = 6.50;
else if (rbDiesel.IsChecked == true) cena = 7.20;
else cena = 3.00; // LPG
```

-----

# ROZWIĄZANIE KROK PO KROKU

### Krok 1: XAML (Widok)

Zwróć uwagę na grupowanie RadioButtonów w `StackPanel` oraz Binding suwaka.

```xml
<Window x:Class="Podroz.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="Podróż - 00000000000" Height="500" Width="600"
        Background="LightBlue">

    <Grid Margin="15">
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto"/> <RowDefinition Height="*"/>    </Grid.RowDefinitions>

        <StackPanel Grid.Row="0" Margin="0,0,0,20">
            
            <TextBlock Text="Dystans (km):"/>
            <TextBox Name="txtDystans" Margin="0,0,0,10"/>

            <CheckBox Name="chkObieStrony" Content="Podróż w obie strony" 
                      FontWeight="Bold" Margin="0,0,0,15"/>

            <TextBlock Text="Rodzaj paliwa:"/>
            <StackPanel Orientation="Horizontal" Margin="0,0,0,15">
                <RadioButton Name="rbBenzyna" Content="Benzyna" IsChecked="True" Margin="0,0,15,0"/>
                <RadioButton Name="rbDiesel" Content="Diesel" Margin="0,0,15,0"/>
                <RadioButton Name="rbLPG" Content="LPG"/>
            </StackPanel>

            <TextBlock Text="Spalanie (l/100km):"/>
            <StackPanel Orientation="Horizontal">
                <Slider Name="sliderSpalanie" Minimum="4" Maximum="20" Width="200" 
                        IsSnapToTickEnabled="True" TickFrequency="0.5"/>
                
                <TextBlock Text="{Binding ElementName=sliderSpalanie, Path=Value}" 
                           FontWeight="Bold" Margin="10,0,0,0"/>
                <TextBlock Text=" l" FontWeight="Bold"/>
            </StackPanel>

            <Button Content="OBLICZ KOSZT" Background="Navy" Foreground="White" 
                    Height="40" Margin="0,20,0,0" Click="Button_Click"/>
        </StackPanel>

        <ListView Name="lvHistoria" Grid.Row="1">
            <ListView.View>
                <GridView>
                    <GridViewColumn Header="Paliwo" Width="100" DisplayMemberBinding="{Binding Paliwo}"/>
                    <GridViewColumn Header="Dystans (km)" Width="100" DisplayMemberBinding="{Binding Dystans}"/>
                    <GridViewColumn Header="Spalanie" Width="80" DisplayMemberBinding="{Binding Spalanie}"/>
                    <GridViewColumn Header="KOSZT (zł)" Width="100" DisplayMemberBinding="{Binding Koszt}"/>
                </GridView>
            </ListView.View>
        </ListView>
    </Grid>
</Window>
```

-----

### Krok 2: C\# (Logika)

Tutaj łączymy wszystko: pobieranie liczb, sprawdzanie „ptaszka” (CheckBox) i kropki (RadioButton).

```csharp
using System.Windows;

namespace Podroz
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        // 1. KLASA DANYCH (Musi być public + get/set)
        public class Trasa
        {
            public string Paliwo { get; set; }
            public double Dystans { get; set; } // double, bo może być 150.5 km
            public double Spalanie { get; set; }
            public string Koszt { get; set; } // string, żeby dodać "zł" ładnie
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            // WALIDACJA: Czy wpisano dystans?
            if (double.TryParse(txtDystans.Text, out double dystans))
            {
                // A. Sprawdzamy CheckBox (W obie strony)
                if (chkObieStrony.IsChecked == true)
                {
                    dystans = dystans * 2;
                }

                // B. Sprawdzamy RadioButton (Cena paliwa)
                double cenaPaliwa = 0;
                string nazwaPaliwa = "";

                if (rbBenzyna.IsChecked == true)
                {
                    cenaPaliwa = 6.50;
                    nazwaPaliwa = "Benzyna";
                }
                else if (rbDiesel.IsChecked == true)
                {
                    cenaPaliwa = 7.20;
                    nazwaPaliwa = "Diesel";
                }
                else // LPG
                {
                    cenaPaliwa = 3.00;
                    nazwaPaliwa = "LPG";
                }

                // C. Obliczenia
                // Wzór: (Dystans / 100) * Spalanie * Cena
                double spalanie = sliderSpalanie.Value;
                double kosztCalkowity = (dystans / 100) * spalanie * cenaPaliwa;

                // Zaokrąglenie do 2 miejsc po przecinku (dla ładnego wyglądu)
                kosztCalkowity = System.Math.Round(kosztCalkowity, 2);

                // D. Dodanie do tabeli
                Trasa nowaTrasa = new Trasa();
                nowaTrasa.Paliwo = nazwaPaliwa;
                nowaTrasa.Dystans = dystans;
                nowaTrasa.Spalanie = spalanie;
                nowaTrasa.Koszt = kosztCalkowity + " zł"; // Triki ze stringiem są OK na egzaminie

                lvHistoria.Items.Add(nowaTrasa);

                // E. Alert (Wymóg zadania)
                if (kosztCalkowity > 500)
                {
                    MessageBox.Show("Droga podróż! Koszt przekracza 500 zł.", "Uwaga", 
                                    MessageBoxButton.OK, MessageBoxImage.Warning);
                }
            }
            else
            {
                MessageBox.Show("Wpisz poprawny dystans (liczba).");
            }
        }
    }
}
```

### Co zyskujesz dzięki temu ćwiczeniu?

1.  Umiesz obsługiwać **logikę warunkową (if)** dla cen (`rbBenzyna`, `rbDiesel`).
2.  Wiesz jak działa mnożnik w **CheckBox** (`dystans * 2`).
3.  Zobaczyłeś `double` w akcji – przydaje się przy pieniądzach i podziale trasy, bo `int` uciąłby grosze.
4.  Wiesz jak zaokrąglić liczbę: `Math.Round(liczba, 2)`.

To zadanie pokrywa około 95% mechanizmów logicznych, jakie mogą pojawić się na egzaminie w części desktopowej. Pozostałe 5% to zazwyczaj po prostu inny układ graficzny.