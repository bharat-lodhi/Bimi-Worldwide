from django import forms
from .models import ProductEnquiry, ProductCategory, SubCategory, ProductSubCategory

class ProductEnquiryForm(forms.ModelForm):
    class Meta:
        model = ProductEnquiry
        fields = [
            'category',
            'sub_category',
            'product',
            'customer_name',
            'mobile',
            'email',
            'company_name',
            'address',
            'country',
            'state',
            'city',
            'pincode',
            'quantity',
            'suitable_call_time',
            'requirements',
            'status',
            'admin_notes'
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({'class': 'form-control', 'rows': 3})
            elif isinstance(field.widget, (forms.Select, forms.NullBooleanSelect)):
                field.widget.attrs.update({'class': 'form-select'})
            else:
                field.widget.attrs.update({'class': 'form-control'})
