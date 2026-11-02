from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegisterForm(forms.ModelForm):
    password=forms.CharField(label='Parola',widget=forms.PasswordInput(attrs={'class':'form-cntrol'}))
    confirm_password=forms.CharField(label='Parola Doğrulama',widget=forms.PasswordInput(attrs={'class':'form.control'}))

    class Meta:
        model=User
        fields=['username','email']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

    def clean_confirm_password(self):
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Parolalar eşleşmiyor!')
        return confirm_password

    def save(self, commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save
        return user


class LoginForm(forms.Form):
    username=forms.CharField(label='Kullanıcı Adı',widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='Parola',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data=super().clean()
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('passsword')

        if username and password:
            self.user=authenticate(username=username, password=password)
            if not self.user:
                raise forms.ValidationError('Kullanıcı adı veya parola hatalı!')
            return self.cleaned_data

