from decimal import Decimal

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from user.models import User


class EditBalanceForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_superuser=False))
    operation = forms.ChoiceField(choices=((None, '---------'), ('add', 'add'), ('subtract', 'subtract')))
    amount = forms.IntegerField(validators=[MinValueValidator(Decimal('0.01'))])

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get("user")
        operation = cleaned_data.get("operation")
        amount = cleaned_data.get("amount")

        if operation == 'subtract' and user.balance < amount:
            raise ValidationError("User balance cannot be below 0.")
