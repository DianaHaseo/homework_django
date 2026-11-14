from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "image",
            "category",
            "price",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.required = True
            field.widget.attrs["class"] = "form-control"

        self.fields["description"].widget.attrs["rows"] = 4
        self.fields["price"].min_value = 0
        self.fields["price"].widget.attrs["min"] = 0

    def clean_price(self):
        price = self.cleaned_data["price"]

        if price < 0:
            raise forms.ValidationError(
                "Цена не может быть отрицательной."
            )

        return price