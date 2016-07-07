from django.contrib.auth.models import Permission, User, Group
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from rail.choices import LOCOCHOICE


class Album(models.Model):
    class Meta:
        permissions = (("view_album", "Can view album"),)
    user = models.ForeignKey(User, default=1)
    vnev = models.CharField(max_length=100, verbose_name='Vonat megnevezése*')
    indulas = models.CharField(max_length=250 ,  verbose_name='Indulás helye*')
    indulas_ido = models.DateTimeField(verbose_name='Várható indulás*')
    belepes = models.CharField(max_length=250, verbose_name='Belépés helye ha tranzit', null=True, blank=True)
    belepes_ido = models.DateTimeField( verbose_name='Belépés ideje ha tranzit', null=True, blank=True)
    erkezes = models.CharField(max_length=250 ,  verbose_name='Érkezés helye', null=True, blank=True)
    kilepes = models.CharField(max_length=250 ,  verbose_name='Kilépés helye ha tranzit', null=True, blank=True)
    rakott = models.BooleanField(verbose_name='Rakott')
    rakomany_fajta = models.CharField(max_length=150, verbose_name='Rakomány fajtája', null=True, blank=True)
    brutto_tonna = models.FloatField(validators=[MinValueValidator(0)], verbose_name='Bruttó tonna*', null=True)
    fekhossz = models.IntegerField(verbose_name='Féktechnikai hosszúság', null=True, blank=True)
    helyzet = models.CharField(max_length=250 ,  verbose_name='Legutóbb ismert helyzete', null=True, blank=True)
    megjegyzesek = models.TextField(max_length=350, verbose_name='Megjegyzések', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vnev + ' - ' + str(self.indulas_ido)



class Vpe(models.Model):
    album = models.ForeignKey(Album, verbose_name='vonat kiválasztása', on_delete=models.CASCADE)
    vpe = models.CharField(max_length=14, verbose_name='VPE szám', null=True, blank=True)
    indulas_ido = models.DateTimeField(verbose_name='Tényleges indulás/határtól ha tranzit')
    kilepes_igazolt = models.DateTimeField( verbose_name='Kilépés visszaigazolt ideje ha tranzit', null=True, blank=True)
    kilepes_tenyleges =models.DateTimeField( verbose_name='Tényleges kilépés ideje ha tranzit', null=True, blank=True)
    erekezes_ido = models.DateTimeField( verbose_name='Tényleges érkezés ideje ha nem tranzit', null=True, blank=True)
    user = models.ForeignKey(User, default=1)
    megjegyzesek = models.TextField(max_length=350, verbose_name='Megjegyzések', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vpe

class Mozdony(models.Model):
    album = models.ForeignKey(Album, verbose_name='vonat kiválasztása', on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1)
    mozdony = models.CharField(max_length=16, choices=LOCOCHOICE, verbose_name='Továbbító mozdony')
    mozdony_hozzarendelve = models.DateTimeField(verbose_name='Mozdony hozzárendelve', null=True, blank=True)
    megjegyzesek = models.TextField(max_length=350, verbose_name='Megjegyzések', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mozdony

