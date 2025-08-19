using System.Windows;
using System.Windows.Media.Imaging;

namespace desktop
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    
    /// 8:50/10:10

    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            UstawObraz("pocztowka.png");
            UstawCene("1");
        }

        private enum TypPrzesylki
        {
            Pocztowka,
            List,
            Paczka
        }

        private TypPrzesylki PobierzWybranyTyp()
        {
            if (pocztowkaRadio.IsChecked == true) return TypPrzesylki.Pocztowka;
            if (listRadio.IsChecked == true) return TypPrzesylki.List;
            return TypPrzesylki.Paczka;
        }

        private void UaktualnijCeneIObraz(TypPrzesylki typ)
        {
            switch (typ)
            {
                case TypPrzesylki.Pocztowka:
                    UstawObraz("pocztowka.png");
                    UstawCene("1");
                    break;

                case TypPrzesylki.List:
                    UstawObraz("list.png");
                    UstawCene("1,5");
                    break;

                case TypPrzesylki.Paczka:
                    UstawObraz("paczka.png");
                    UstawCene("10");
                    break;
            }
        }
        private void UstawCene(string cena)
        {
            cenaLabel.Content = $"Cena: {cena} zł";
        }

        private void UstawObraz(string nazwaPliku)
        {
            var uri = new Uri($"img/{nazwaPliku}", UriKind.Relative);
            przesylkaImage.Source = new BitmapImage(uri);
        }

        private void SprawdzCeneButton(object sender, RoutedEventArgs e)
        {
            var typ = PobierzWybranyTyp();
            UaktualnijCeneIObraz(typ);
        }

        private bool WalidujKodPocztowy(string input, out string komunikat)
        {
            komunikat = string.Empty;
            if (input == null) input = "";
            input = input.Trim();

            if (input.Length != 5)
            {
                komunikat = "Nieprawidłowa liczba cyfr w kodzie pocztowym";
                return false;
            }

            foreach (char c in input)
            {
                if(!char.IsDigit(c))
                {
                    komunikat = "Kod pocztowy powinien się składać z samych cyfr";
                    return false;
                }
            }
            return true;
        }

        private void ZatwierdzButton(object sender, RoutedEventArgs e)
        {
            if (WalidujKodPocztowy(kodPocztowyTextBox.Text, out string msg))
            {
                MessageBox.Show("Dane przesyłki zostały wprowadzone",
                                "Sukces", MessageBoxButton.OK, MessageBoxImage.Information);
            }
            else
            {
                MessageBox.Show(msg,
                                "Błąd", MessageBoxButton.OK, MessageBoxImage.Warning);
            }
        }
    }
}