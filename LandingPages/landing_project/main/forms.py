from django import forms
from .models import InterestedCustomer


class InterestForm(forms.ModelForm):
    class Meta:
        model = InterestedCustomer
        fields = ["name", "email", "university", "message"]
        widgets = {
            "message": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Optional message..."}
            ),
        }
