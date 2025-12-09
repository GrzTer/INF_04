Oto kolejne zadanie, które łączy wszystkie dotychczasowe umiejętności: **ComboBox**, **CheckBox**, **Slider** oraz **Alert**.

To jest klasyk egzaminacyjny: **Formularz zgłoszeniowy / System zamówień**.

-----

# ZADANIE TRENINGOWE: "System Zamówień Magazynowych"

**Scenariusz:** Tworzysz aplikację dla pracownika magazynu, który dodaje nowe zamówienia do systemu.

**Wymagania:**

1.  **Wygląd:**
      * Tytuł: "Magazyn - [Twój PESEL]".
      * Tło: `#E6E6FA` (Lavender).
      * Przycisk: `#8A2BE2` (BlueViolet), biały tekst.
2.  **Formularz:**
      * **Nazwa produktu:** Pole tekstowe.
      * **Kategoria (ComboBox):** Do wyboru: "Elektronika", "Odzież", "Inne".
      * **Ilość (Slider):** Zakres 1 do 50. Wyświetlanie wartości obok.
      * **Priorytet (CheckBox):** Opcja "Wysyłka natychmiastowa".
3.  **Tabela (ListView):**
      * Kolumny: Produkt, Kategoria, Ilość, Status.
      * *Logika statusu:* Jeśli CheckBox zaznaczony -\> wpisz "PILNE", jeśli nie -\> "Standard".
4.  **Alerty (MessageBox):**
      * Jeśli pracownik wybierze **Ilość powyżej 40 sztuk**, wyświetl informację: *"Duże zamówienie\! Potrzebny wózek widłowy."* (Ikona: Information).
      * Walidacja: Jeśli nie wpisano nazwy produktu, wyświetl błąd (Ikona: Error).

-----

# WSKAZÓWKI (Zanim zaczniesz pisać)

To zadanie sprawdza, czy pamiętasz jak obsługiwać różne typy danych:

1.  **ComboBox:** Pamiętaj o rzutowaniu na `(ComboBoxItem)` żeby wyciągnąć tekst.
2.  **CheckBox:** Pamiętaj, że w tabeli ma pojawić się słowo ("PILNE"), a nie `true/false`. Użyj `if`.
3.  **Walidacja:** `string.IsNullOrWhiteSpace(tekst)` to przyjaciel egzaminacyjny.

-----

# ROZWIĄZANIE

### 1\. XAML (Widok)

Zwróć uwagę na `ComboBoxItem` wpisane na sztywno i binding suwaka.

```xml
<Window x:Class="Magazyn.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="Magazyn - 00000000000" Height="450" Width="600"
        Background="#E6E6FA"> <Grid Margin="15">
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto"/>
            <RowDefinition Height="*"/>
        </Grid.RowDefinitions>

        <StackPanel Grid.Row="0" Margin="0,0,0,20">
            
            <TextBlock Text="Nazwa produktu:"/>
            <TextBox Name="txtProdukt" Margin="0,0,0,10"/>

            <TextBlock Text="Kategoria:"/>
            <ComboBox Name="cbKategoria" SelectedIndex="0" Margin="0,0,0,10">
                <ComboBoxItem Content="Elektronika"/>
                <ComboBoxItem Content="Odzież"/>
                <ComboBoxItem Content="Inne"/>
            </ComboBox>

            <TextBlock Text="Ilość sztuk:"/>
            <StackPanel Orientation="Horizontal" Margin="0,0,0,10">
                <Slider Name="sliderIlosc" Minimum="1" Maximum="50" Width="200" 
                        IsSnapToTickEnabled="True" TickFrequency="1"/>
                <TextBlock Text="{Binding ElementName=sliderIlosc, Path=Value}" 
                           FontWeight="Bold" Margin="10,0,0,0"/>
            </StackPanel>

            <CheckBox Name="chkPriorytet" Content="Wysyłka natychmiastowa" 
                      FontWeight="Bold" Margin="0,0,0,15"/>

            <Button Content="DODAJ ZAMÓWIENIE" Click="Button_Click"
                    Background="#8A2BE2" Foreground="White"
                    Height="35" Width="200" HorizontalAlignment="Left"/>
        </StackPanel>

        <ListView Name="lvZamowienia" Grid.Row="1">
            <ListView.View>
                <GridView>
                    <GridViewColumn Header="Produkt" Width="150" DisplayMemberBinding="{Binding Nazwa}"/>
                    <GridViewColumn Header="Kategoria" Width="100" DisplayMemberBinding="{Binding Kat}"/>
                    <GridViewColumn Header="Ilość" Width="50" DisplayMemberBinding="{Binding Ile}"/>
                    <GridViewColumn Header="Status" Width="100" DisplayMemberBinding="{Binding Tryb}"/>
                </GridView>
            </ListView.View>
        </ListView>
    </Grid>
</Window>
```

-----

### 2\. C\# (Logika)

```csharp
using System.Windows;
using System.Windows.Controls; // Ważne dla ComboBoxItem

namespace Magazyn
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        // 1. KLASA DANYCH
        public class Zamowienie
        {
            public string Nazwa { get; set; }
            public string Kat { get; set; }
            public int Ile { get; set; }
            public string Tryb { get; set; } // Tu trafi tekst "PILNE" lub "Standard"
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            // A. WALIDACJA
            if (string.IsNullOrWhiteSpace(txtProdukt.Text))
            {
                MessageBox.Show("Podaj nazwę produktu!", "Błąd", MessageBoxButton.OK, MessageBoxImage.Error);
                return; // Stop
            }

            // B. POBIERANIE DANYCH
            string nazwa = txtProdukt.Text;
            int ilosc = (int)sliderIlosc.Value;

            // ComboBox (Rozpakowanie pudełka)
            ComboBoxItem wybranyItem = (ComboBoxItem)cbKategoria.SelectedItem;
            string kategoria = wybranyItem.Content.ToString();

            // CheckBox (Logika Statusu)
            string statusTekst = "";
            if (chkPriorytet.IsChecked == true)
            {
                statusTekst = "PILNE";
            }
            else
            {
                statusTekst = "Standard";
            }

            // C. TWORZENIE OBIEKTU I DODANIE DO LISTY
            Zamowienie z = new Zamowienie();
            z.Nazwa = nazwa;
            z.Kat = kategoria;
            z.Ile = ilosc;
            z.Tryb = statusTekst;

            lvZamowienia.Items.Add(z);

            // D. ALERT (WARUNEK)
            if (ilosc > 40)
            {
                MessageBox.Show("Duże zamówienie! Potrzebny wózek widłowy.", 
                                "Info Logistyczne", 
                                MessageBoxButton.OK, 
                                MessageBoxImage.Information);
            }
        }
    }
}
```

### Autorefleksja (Sprawdź się):

1.  Czy pamiętałeś, że `IsChecked` trzeba sprawdzić `== true`?
2.  Czy pamiętałeś o rzutowaniu suwaka na `(int)`, żeby nie mieć przecinków w tabeli?
3.  Czy klasa `Zamowienie` ma `public` i `get; set;`?

Jeśli napisałeś to bez zaglądania w kod – jesteś gotowy na egzamin. To jest dokładnie ten poziom trudności.