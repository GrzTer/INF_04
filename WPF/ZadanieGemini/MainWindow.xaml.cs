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

namespace ZadanieGemini
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

        public class DanePogodowe
        {
            public string Czas { get; set; }
            public int Wartosc { get; set; }
        }

        private void Button_Zatwierdz_Click(object sender, RoutedEventArgs e)
        {
            int temperatura = (int)sliderTemp.Value;
            DanePogodowe nowyWpis = new DanePogodowe();
            nowyWpis.Czas = DateTime.Now.ToString("HH:mm:ss");
            nowyWpis.Wartosc = temperatura;

            lvHistoria.Items.Add(nowyWpis);

            if (temperatura > 30)
            {
                MessageBox.Show("UWAGA: Wysoka temperatura!", "Alarm termiczny", MessageBoxButton.OK, MessageBoxImage.Warning);
            }
            else if (temperatura < 0)
            {
                MessageBox.Show("OSTRZEŻENIE: Możliwe oblodzenie", "Zimno", MessageBoxButton.OK, MessageBoxImage.Information);
            }
            sliderTemp.Value = 0;
        }
    }
}