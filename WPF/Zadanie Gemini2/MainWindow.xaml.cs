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

namespace Zadanie_Gemini2
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

        public class Trasa
        {
            public string Paliwo { get; set; }
            public double Dystans { get; set; }
            public double Spalanie { get; set; }
            public string Koszt {  get; set; }
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            if (double.TryParse(txtDystans.Text, out double dystans))
            {
                if (chkObieStrony.IsChecked == true)
                {
                    dystans = dystans * 2;
                }

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
                else
                {
                    cenaPaliwa = 3.00;
                    nazwaPaliwa = "LPG";
                } 
                double spalanie = sliderSpalanie.Value;
                double kosztCalkowity = (dystans / 100) * spalanie * cenaPaliwa;

                kosztCalkowity = System.Math.Round(kosztCalkowity, 2);

                Trasa nowaTrasa = new Trasa();
                nowaTrasa.Paliwo = nazwaPaliwa;
                nowaTrasa.Dystans = dystans;
                nowaTrasa.Spalanie = spalanie;
                nowaTrasa.Koszt = kosztCalkowity + " zł";

                lvHistoria.Items.Add(nowaTrasa);

                if (kosztCalkowity > 500)
                {
                    MessageBox.Show("Droga podróż! Koszt przekracza 500 zł.", "Uwaga", MessageBoxButton.OK, MessageBoxImage.Warning);
                }
            }
            else
            {
                MessageBox.Show("Wpisz poprawny dystans (liczba).");
            }
        }
    }
}