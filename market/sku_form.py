from django import forms


class SKUFilterForm(forms.Form):
    location = forms.CharField(label="Location", max_length=150)
    department = forms.CharField(label="Department", max_length=150)
    category = forms.CharField(label="Category", max_length=150)
    subcategory = forms.CharField(label="Sub Category", max_length=150)

