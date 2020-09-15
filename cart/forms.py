from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductFrom(forms.Form):
    quantity = forms.TypedMultipleChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int)
    override = forms.BooleanField(initial=False,
                                  required=False,
                                  widget=forms.HiddenInput)
