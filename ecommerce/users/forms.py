from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets, ModelForm

from users.models import UserAddress



class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.labels = {'first_name': 'Imię', 'last_name': 'Nazwisko', 'username': 'Nazwa użytkownika', "email":"Adres email", 'password1': 'Utwórz hasło', 'password2': 'Powtórz hasło'}
        for name,field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': f'{self.labels[name]}'})

class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password',]

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.labels = {'username': 'Nazwa użytkownika', 'password': 'Hasło'}
        for name,field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': f'{self.labels[name]}'})


class UserAddressForm(ModelForm):
    class Meta:
        model = UserAddress
        fields = ['street', 'building', 'post_code', 'city']
        labels = {'street': "Ulica", 'building': 'Numer Budynku', 'post_code': 'Kod pocztowy', 'city': 'Miasto'}

    def __init__(self, *args, **kwargs):
        super(UserAddressForm, self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})