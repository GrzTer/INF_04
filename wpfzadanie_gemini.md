Oto przykładowe zadanie egzaminacyjne przygotowane specjalnie pod Twoje wymagania: **Suwaki (Slider), Listy (ListView) i Alerty (MessageBox)**.

Jest to klasyczny wariant zadania "monitoring", ale zamiast wpisywania liczby ręcznie, musisz użyć suwaka, a zamiast panelu trendu, musisz obsłużyć wyskakujące powiadomienia (Alerty).

-----

# ARKUSZ EGZAMINACYJNY (Symulacja INF.04)

**Temat zadania:** Aplikacja "Panel Temperatury".

**Opis zadania:**
Stwórz aplikację desktopową do rejestrowania temperatury w pomieszczeniu.
Aplikacja powinna umożliwiać:

1.  Ustawienie temperatury za pomocą **suwaka** (Slider).
2.  Podgląd aktualnie wybranej na suwaku wartości.
3.  Dodanie pomiaru do listy.
4.  Wyświetlenie **alertu** (okno komunikatu), jeśli temperatura jest krytyczna.

**Wymagania dotyczące interfejsu (Wygląd):**

  * **Tytuł okna:** "Panel Temperatury – [Twój numer PESEL]"
  * **Wymiary okna:** 600x450
  * **Kolorystyka:**
      * Tło aplikacji: `MintCream` (\#F5FFFA)
      * Przyciski: `SeaGreen` (\#2E8B57), tekst biały.
  * **Układ:**
      * Góra: Suwak oraz przycisk "Zatwierdź".
      * Dół: Tabela z historią pomiarów.

**Funkcjonalność:**

1.  **Suwak (Slider):**
      * Zakres wartości: od **-10** do **40**.
      * Musi być liczbą całkowitą (bez przecinków).
      * Obok suwaka musi wyświetlać się aktualnie ustawiona na nim liczba (np. "22 stopni").
2.  **Tabela (ListView):**
      * Kolumny: "Godzina", "Temperatura".
3.  **Przycisk "Zatwierdź":**
      * Dodaje aktualną wartość suwaka i czas do tabeli.
4.  **Alerty (MessageBox):**
      * Jeśli użytkownik zatwierdzi temperaturę **powyżej 30 stopni**, aplikacja musi wyświetlić okno z ostrzeżeniem: *"UWAGA: Wysoka temperatura\!"* i ikoną ostrzeżenia.
      * Jeśli użytkownik zatwierdzi temperaturę **poniżej 0 stopni**, aplikacja wyświetla komunikat: *"OSTRZEŻENIE: Możliwe oblodzenie"*.

-----

# ROZWIĄZANIE (KROK PO KROKU)

### 1\. Kod XAML (Widok)

Kluczowe nowości tutaj to `Slider` oraz `Binding` w TextBlocku, który pozwala wyświetlać wartość suwaka na żywo bez pisania kodu C\#.

```xml
<Window x:Class="PanelTemperatury.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="Panel Temperatury – 00000000000" Height="450" Width="600"
        Background="#F5FFFA"> <Grid Margin="15">
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto"/> <RowDefinition Height="*"/>    </Grid.RowDefinitions>

        <StackPanel Grid.Row="0" Margin="0,0,0,20">
            
            <TextBlock Text="Ustaw temperaturę:" FontSize="16" Margin="0,0,0,5"/>

            <Slider Name="sliderTemp" 
                    Minimum="-10" Maximum="40" 
                    TickFrequency="1" IsSnapToTickEnabled="True"
                    Margin="0,0,0,10"/>

            <StackPanel Orientation="Horizontal" HorizontalAlignment="Center" Margin="0,0,0,15">
                <TextBlock Text="Wybrana wartość: " FontSize="14" FontWeight="Bold"/>
                <TextBlock Text="{Binding ElementName=sliderTemp, Path=Value}" FontSize="14" FontWeight="Bold"/>
                <TextBlock Text=" °C" FontSize="14" FontWeight="Bold"/>
            </StackPanel>

            <Button Content="Zatwierdź" Background="#2E8B57" Foreground="White"
                    Height="35" Width="150" FontSize="14"
                    Click="Button_Zatwierdz_Click"/>
        </StackPanel>

        <Border Grid.Row="1" BorderBrush="Black" BorderThickness="1" Background="White">
            <ListView Name="lvHistoria">
                <ListView.View>
                    <GridView>
                        <GridViewColumn Header="Godzina" Width="150" DisplayMemberBinding="{Binding Czas}"/>
                        <GridViewColumn Header="Temperatura" Width="150" DisplayMemberBinding="{Binding Wartosc}"/>
                    </GridView>
                </ListView.View>
            </ListView>
        </Border>
    </Grid>
</Window>
```

-----

### 2\. Kod C\# (Logika)

Tutaj stosujemy tę samą "prymitywną" i bezpieczną logikę co wcześniej. Pobieramy wartość prosto z kontrolki (`sliderTemp.Value`).

```csharp
using System;
using System.Windows;

namespace PanelTemperatury
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        // Klasa danych do tabeli (Musi mieć get; set;)
        public class DanePogodowe
        {
            public string Czas { get; set; }
            public int Wartosc { get; set; }
        }

        private void Button_Zatwierdz_Click(object sender, RoutedEventArgs e)
        {
            // 1. Pobranie wartości z suwaka
            // Slider zwraca double (z przecinkiem), więc rzutujemy na int (całkowitą)
            int temperatura = (int)sliderTemp.Value;

            // 2. Dodanie do listy (ListView)
            DanePogodowe nowyWpis = new DanePogodowe();
            nowyWpis.Czas = DateTime.Now.ToString("HH:mm:ss");
            nowyWpis.Wartosc = temperatura;

            lvHistoria.Items.Add(nowyWpis);

            // 3. Obsługa ALERTÓW (Wymaganie egzaminacyjne)
            
            if (temperatura > 30)
            {
                // MessageBox z ikoną ostrzeżenia
                MessageBox.Show("UWAGA: Wysoka temperatura!", "Alarm termiczny", 
                                MessageBoxButton.OK, MessageBoxImage.Warning);
            }
            else if (temperatura < 0)
            {
                // MessageBox z informacją
                MessageBox.Show("OSTRZEŻENIE: Możliwe oblodzenie", "Zimno", 
                                MessageBoxButton.OK, MessageBoxImage.Information);
            }

            // Opcjonalnie: reset suwaka na środek (np. 20 stopni) po dodaniu
            // sliderTemp.Value = 20; 
        }
    }
}
```

### Na co zwrócić uwagę (Pułapki w tym wariancie):

1.  **Slider Value jest typu `double`**:
      * Nawet jeśli ustawisz `IsSnapToTickEnabled="True"`, C\# widzi wartość jako np. `20.0`.
      * Dlatego przy pobieraniu musisz zrobić rzutowanie: `(int)sliderTemp.Value`.
2.  **Wyświetlanie wartości suwaka**:
      * Najłatwiej zrobić to w XAML używając `{Binding ElementName=nazwaSuwaka, Path=Value}`. Dzięki temu nie musisz pisać zdarzenia `ValueChanged` w C\#, co oszczędza czas i eliminuje błędy.
3.  **MessageBoxImage**:
      * Warto dodać czwarty parametr w `MessageBox.Show(..., ..., ..., MessageBoxImage.Warning)`. Egzaminatorzy lubią, gdy ikona zgadza się z treścią alertu.