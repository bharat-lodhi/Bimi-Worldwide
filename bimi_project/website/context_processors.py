from custom_admin.models import ProductCategory

def footer_categories(request):
    return {
        'footer_categories': ProductCategory.objects.all().order_by('id')
    }
