from django.db import models


class Przedmiot(models.Model):
    nazwa = models.CharField(max_length=255)
    klasyfikacja = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nazwa}"


class Uczen(models.Model):
    imie = models.CharField(max_length=255)
    nazwisko = models.CharField(max_length=255)
    pesel = models.CharField(max_length=255)
    klasa = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Ocena(models.Model):
    przedmiot_id = models.ForeignKey(Przedmiot, on_delete=models.CASCADE)
    uczen_id = models.ForeignKey(Uczen, on_delete=models.CASCADE)
    ocena = models.PositiveIntegerField()
    data_wystawienia = models.DateField()

    def __str__(self):
        return f"Ocena: {self.ocena} wystawiona {self.data_wystawienia} z przedmiotu {self.przedmiot_id.nazwa}"
