from django import forms


class TextField(forms.Form):
    text = forms.CharField(label="Type here your text")
