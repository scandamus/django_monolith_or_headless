from django import forms
from .models import DataOmikuji


class FormOmikuji(forms.ModelForm):
    class Meta:
        model = DataOmikuji
        fields = ['nick_name', 'result']

# フォームからの格納先
