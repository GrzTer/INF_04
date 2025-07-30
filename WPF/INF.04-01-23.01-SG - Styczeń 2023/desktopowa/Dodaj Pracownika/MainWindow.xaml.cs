using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Dodaj_Pracownika
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private const string MaleLitery = "abcdefghijklmnopqrstuvwxyz";
        private const string WielkieLitery = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        private const string Cyfry = "0123456789";
        private const string ZnakiSpecjalne = "!@#$%^&*()_+-";
        private string wygenerowaneHaslo = "";
        public MainWindow()
        {
            InitializeComponent();
        }

        private void GenerujHaslo_Click(object sender, RoutedEventArgs e)
        {
            int liczbaZnakow = int.Parse(LiczZnak.Text);
            bool maleIWielkieLitery = (bool)MaleIWielkieLiteryCheckBox.IsChecked;
            bool Cyfry = (bool)CyfryCheckBox.IsChecked;
            bool znakiSpecjalne = (bool)ZnakiSpecjalneCheckBox.IsChecked;

            wygenerowaneHaslo = GenerujHaslo(liczbaZnakow, maleIWielkieLitery, Cyfry, znakiSpecjalne);
            MessageBox.Show(wygenerowaneHaslo);
        }

        private string GenerujHaslo(int liczbaZnakow, bool maleIWIelkieLitery, bool cyfry, bool znakiSpecjalne)
        {
            string pulaZnakow = MaleLitery;
            if (maleIWIelkieLitery) pulaZnakow += WielkieLitery;
            string haslo = "";
            Random rand = new Random();

            for (int i = 0; i < liczbaZnakow; i++) haslo += pulaZnakow[rand.Next(pulaZnakow.Length)];

            if (cyfry) haslo = ZamienZnak(haslo, Cyfry, rand, 0);
            if (znakiSpecjalne) haslo = ZamienZnak(haslo, ZnakiSpecjalne, rand, 1);

            return haslo;
        }


        private string ZamienZnak(string haslo, string zestaw, Random rand, int pozycja)
        {
            if (haslo.Length <= pozycja) return haslo;
            char nowyZnak = zestaw[rand.Next(zestaw.Length)];
            return haslo.Substring(0, pozycja) + nowyZnak + haslo.Substring(pozycja + 1);
        }

        private void Zatwierdz_Click(object sender, RoutedEventArgs e)
        {
            string imie = ImieTextBox.Text;
            string nazwisko = NazwiskoTextBox.Text;
            string stanowisko = StanowiskoComboBox.SelectionBoxItem.ToString();
            string komunikat = $"Dane pracownika: {imie} {nazwisko} {stanowisko} Haslo: {wygenerowaneHaslo}";
            MessageBox.Show(komunikat);
        }
    }
}