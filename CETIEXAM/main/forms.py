from django import forms
from .models import Country, City



class createCounrty(forms.ModelForm):
    class Meta:
        fields = ("NameCountry", "GovType", "Language", "Continent")
        model = Country
        widgets = {
            "NameCountry": forms.TextInput(attrs={'placeholder': 'Country Name'}),
            "GovType": forms.TextInput(attrs={'placeholder': 'GovType'}),
            "Language": forms.TextInput(attrs={'placeholder': 'Language'}),
            "Continent": forms.TextInput(attrs={'placeholder': 'Continent'}),
        }

class createCity(forms.ModelForm):
    class Meta:
        model = City
        fields = ("NameCity", "CodCountry", "Capital")
        widgets = {
            "NameCity": forms.TextInput(attrs={"class": "NameCity"}),
        }

    def __init__(self, *args, **kwargs):
        super(createCity, self).__init__(*args, **kwargs)
        self.fields['CodCountry'].queryset = Country.objects.all()


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['CodCity', 'NameCity', 'CodCountry', 'Capital']