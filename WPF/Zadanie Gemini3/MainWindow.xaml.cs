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

namespace Zadanie_Gemini3
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        public class Zamowienie
        {
            public string Nazwa { get; set; }
            public string Kat{ get; set; }
            public int Ile { get; set; }
            public string Tryb { get; set; }
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            if (string.IsNullOrWhiteSpace(txtProdukt.Text))
            {
                MessageBox.Show("Podaj nazwę produktu!", "Błąd", MessageBoxButton.OK, MessageBoxImage.Error);
                return;
            }

            string nazwa = txtProdukt.Text;
            int ilosc = (int)sliderIlosc.Value;

            ComboBoxItem wybranyItem = (ComboBoxItem)cbKategoria.SelectedItem;
            string kategoria = wybranyItem.Content.ToString();

            string statusTekst = "";
            if (chkPriorytet.IsChecked == true)
            {
                statusTekst = "PILNE"; 
            }
            else
            {
                statusTekst = "Standart";
            }

            Zamowienie z = new Zamowienie();
            z.Nazwa = nazwa;
            z.Kat = kategoria;
            z.Ile = ilosc;
            z.Tryb = statusTekst;

            lvZamowienia.Items.Add(z);

            if (ilosc > 40)
            {
                MessageBox.Show("Duże zamówienie! Potrzebny wózek widłowy.", "Info logistyczne", MessageBoxButton.OK, MessageBoxImage.Information);
            }
        }
    }

}