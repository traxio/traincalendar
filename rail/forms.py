from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from datetimewidget.widgets import DateTimeWidget
from .models import Album, Vpe, Mozdony
from functools import partial
from rail.choices import LOCOCHOICE
DateInput = partial(forms.DateTimeInput, {'class': 'datepicker'})


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['vnev', 'indulas', 'indulas_ido', 'belepes', 'belepes_ido','erkezes','kilepes','rakott','rakomany_fajta','brutto_tonna','fekhossz','helyzet','megjegyzesek']
        widgets = {'indulas_ido': DateInput(),'belepes_ido': DateInput()}

    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.fields['indulas_ido'].widget.attrs['class'] = 'datepicker'
        self.fields['belepes_ido'].widget.attrs['class'] = 'datepicker'
        self.fields['indulas'].widget.attrs['class'] = 'szhely_auto'
        self.fields['erkezes'].widget.attrs['class'] = 'szhely_auto'
        self.fields['belepes'].widget.attrs['class'] = 'szhely_auto'
        self.fields['kilepes'].widget.attrs['class'] = 'szhely_auto'
        self.fields['helyzet'].widget.attrs['class'] = 'szhely_auto'

class VpeForm(forms.ModelForm):

    class Meta:
        model = Vpe
        fields = ['vpe', 'indulas_ido','kilepes_igazolt','kilepes_tenyleges','erekezes_ido','megjegyzesek']

    def __init__(self, *args, **kwargs):
        super(VpeForm, self).__init__(*args, **kwargs)
        self.fields['indulas_ido'].widget.attrs['class'] = 'datepicker'
        self.fields['kilepes_igazolt'].widget.attrs['class'] = 'datepicker'
        self.fields['kilepes_tenyleges'].widget.attrs['class'] = 'datepicker'
        self.fields['erekezes_ido'].widget.attrs['class'] = 'datepicker'

class MozdonyForm(forms.ModelForm):
    mozdony = forms.ChoiceField(choices=LOCOCHOICE, initial="", widget=forms.Select(), required=True)

    class Meta:
        model = Mozdony
        fields = ['mozdony', 'mozdony_hozzarendelve','megjegyzesek']

    def __init__(self, *args, **kwargs):
        super(MozdonyForm, self).__init__(*args, **kwargs)
        self.fields['mozdony_hozzarendelve'].widget.attrs['class'] = 'datepicker'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
