from django import forms
from django.utils.translation import gettext as _


class TextField(forms.Form):
    text = forms.CharField(label=_("Type here your text"))
