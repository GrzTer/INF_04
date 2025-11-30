from django.db import models


class Ryby(models.Model):
    nazwa = models.CharField(max_length=200)
    występowanie = models.CharField(max_length=200)
    styl_zycia = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nazwa}; występowanie - {self.występowanie} styl_zycia - {self.styl_zycia}"


class Okres_ochronny(models.Model):
    od_miesiaca = models.IntegerField()
    do_miesiaca = models.IntegerField()
    wymiar_ochrony = models.IntegerField()
    ryby_id = models.ForeignKey(Ryby, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ryby_id.nazwa} chroniony od {self.od_miesiaca} do {self.do_miesiaca}; wymiar ochrony - {self.wymiar_ochrony}"
