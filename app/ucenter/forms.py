from django.shortcuts import get_object_or_404
from django import forms

from . import models


class WithdrawForm(forms.Form):
    amount = forms.IntegerField(min_value=1)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount > self.user.money:
            raise forms.ValidationError('insufficient user balance')

        return amount
