   M S B A M L   `   `   `  ����K  GDodaj Pracownika, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null3clr-namespace:Dodaj_PracownikaDodaj_Pracownika  5   	   !    Dodaj_Pracownika.MainWindow   5   	   W SPresentationCore, Version=8.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=8.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35e aSystem.Windows.Controls.Ribbon, Version=8.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089R NWindowsBase, Version=8.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35F 9http://schemas.microsoft.com/winfx/2006/xaml/presentation     5   	   R NSystem.Xaml, Version=8.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   0localclr-namespace:Dodaj_Pracownika     5   	     � Title$-  'Dodaj Pracownika Grzegorz Tereszkiewicz��5   	   $	��300��69   $	��637��6F   ���#B0C4DE.��5	      � .+�5
   
   �� $��Dane Pracownika��6   $��	39,33,0,0q�6,   $
��Left=�6?   $	��258��6Z   $	��190��6f   $	��Top=�6s   .��5      �� $	��160��6   .+�5      ��  �� Orientation$ 
Horizontal=�6   $��0,0,0,0q�66   .+�5      �� $��Imię��6   $	��100��6+   $��10,0,0,0q�67   �� 5      -   5        $��ImieTextBox��5   2    �� TextWrapping$
 Wrap=�6   $	��120��6E   5      �� 5      $ 
Horizontal=�6   $��0,20,0,0q�66   .+�5      �� $��Nazwisko��6   $	��100��6/   $��10,0,0,0q�6;   �� 5      -   5        $��NazwiskoTextBox��5   2   $
 Wrap=�6   $	��120��6I   5      �� 5      $ 
Horizontal=�6   $��0,20,0,0q�66   .+�5      �� $��
Stanowisko��6   $	��100��61   $��10,0,0,0q�6=   �� 5      -   5        $��StanowiskoComboBox��5      $	��120��69   .@�5      �� $��	Kierownik��6'   �� 5      $��Starszy programista��6'   �� 5      $��Młodszy programista��6'   �� 5      $��Tester��6'   5      5      5      5      �� 5   
   $��Generowanie hasła��6   $��
346,33,0,0q�6.   $
��Left=�6B   $	��264��6]   $	��190��6i   $	��Top=�6v   .��5       �� $	��160��6   .+�5!      �� $ 
Horizontal=�6   $��0,0,0,0q�66   $	��227��6G   .+�5"      �� $��Ile znaków?��6   $	��100��62   $��10,0,0,0q�6>   �� 5#      -   5        $��LiczZnak��5#   2   $
 Wrap=�6   $	��122��6B   5$      �� 5%      $ Vertical=�6   $��0,10,0,0q�64   .+�5&      �� -   5        $ ��MaleIWielkieLiteryCheckBox��5&   ?   $��Małe i wielkie litery��6    d� 	IsChecked$
 TrueY�6a   $��20,0,0,0q�6r   �� 5'      -   5        $��CyfryCheckBox��5'   /   $��Cyfry��6   $��	20,20,0,0q�6D   �� 5(      -   5        $��ZnakiSpecjalneCheckBox��5(   9   $��Znaki specjalne��6   $��	20,20,0,0q�6W   5)      �� 5*      $ Vertical=�6   $��0,20,0,0q�64   �� 5+      -   5        $��Generuj hasło��5+      $��80��61   ���#4682B4
�������6l   5,      5-      �� 5.   
   -	   5        $��
Zatwierdź��5.      $��
0,0,241,10q�6%   ���#4682B4
�������$��Right=�6z   $	��181��6�   $��21��6�   $��Bottom=�6�   5/      50      