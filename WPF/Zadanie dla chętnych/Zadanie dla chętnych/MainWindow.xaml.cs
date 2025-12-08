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

namespace Zadanie_dla_chętnych
{
    public partial class MainWindow : Window
    {
        List<int> historiaCisnien = new List<int>();

        public MainWindow()
        {
            InitializeComponent();
        }

        public class Pomiar
        {
            public string Czas { get; set; }
            public int Wartosc { get; set; }
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            string tekst = txtCisnienie.Text;
            int cisnienie;

            if (int.TryParse(tekst, out cisnienie))
            {
                if (cisnienie >= 900 && cisnienie <= 1100)
                {
                    Pomiar nowy = new Pomiar();
                    nowy.Czas = DateTime.Now.ToString("HH:mm");
                    nowy.Wartosc = cisnienie;

                    lvPomiary.Items.Add(nowy);

                    historiaCisnien.Add(cisnienie);

                    SprawdzTrend();
                }
                else
                {
                    MessageBox.Show("Błąd: Wartość musi być z zakresu 900-1100");
                }
            }
            else
            {
                MessageBox.Show("Błąd: Wpisz poprawną liczbę");
            }
        }

        private void SprawdzTrend()
        {
            if (historiaCisnien.Count >= 2)
            {
                int ostatniIndex = historiaCisnien.Count - 1;
                int przedostatniIndex = historiaCisnien.Count - 2;

                int ostatniaWartosc = historiaCisnien[ostatniIndex];
                int przedostatniaWartosc = historiaCisnien[przedostatniIndex];

                if (ostatniaWartosc > przedostatniaWartosc)
                {
                    txtTrend.Text = "Trend: wzrost";
                }
                else if (ostatniaWartosc < przedostatniaWartosc)
                {
                    txtTrend.Text = "Trend: spadek";
                }
                else
                {
                    txtTrend.Text = "Trend: stabilnie";
                }
            }
            else
            {
                txtTrend.Text = "Brak danych";
            }
        }
    }
}