from django.db import models
from django.contrib.auth.models import User


# =========================================================
# BLOG MODEL
# =========================================================

class Blog(models.Model):

    title = models.CharField(max_length=1000)

    subtitle = models.CharField(
        max_length=1000,
        blank=True,
        null=True
    )

    description = models.TextField()

    author = models.CharField(max_length=100)

    image = models.ImageField(
        upload_to='blog_images/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    is_published = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title


import os
from django.core.exceptions import ValidationError

def validate_video_file(value):
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = ['.mp4', '.webm', '.ogg']
    if ext not in valid_extensions:
        raise ValidationError('Unsupported file extension. Only .mp4, .webm, and .ogg are allowed.')
    
    max_size = 100 * 1024 * 1024 # 100MB
    if value.size > max_size:
        raise ValidationError('File size exceeds the 100MB limit.')


# =========================================================
# PRODUCT CATEGORY
# =========================================================

class ProductCategory(models.Model):

    name = models.CharField(
        max_length=255
    )

    short_description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to='categories/',
        blank=True,
        null=True
    )

    category_video = models.FileField(
        upload_to='categories/videos/',
        blank=True,
        null=True,
        validators=[validate_video_file]
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


# =========================================================
# REAL SUB CATEGORY
# =========================================================

class SubCategory(models.Model):

    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name='real_subcategories'
    )

    name = models.CharField(
        max_length=255
    )

    short_description = models.TextField(
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='real_subcategories/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.category.name} - {self.name}"


# =========================================================
# PRODUCT MODEL
# =========================================================

class ProductSubCategory(models.Model):

    # CATEGORY
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name='products'
    )

    # REAL SUBCATEGORY
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name='products',
        blank=True,
        null=True
    )

    # PRODUCT NAME
    name = models.CharField(
        max_length=255
    )

    # SHORT DESCRIPTION
    short_description = models.TextField(
        blank=True
    )

    # LONG DESCRIPTION
    long_description = models.TextField(
        blank=True
    )

    # PRODUCT IMAGE
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )

    # BENEFITS
    benefits = models.TextField(
        blank=True,
        null=True
    )

    # SPECIFICATIONS
    specifications = models.TextField(
        blank=True,
        null=True
    )

    # PACKING DETAILS
    packing_details = models.TextField(
        blank=True,
        null=True
    )

    # CREATED DATE
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


# =========================================================
# CONTACT ENQUIRY MODEL
# =========================================================

class ContactEnquiry(models.Model):
    
    STATUS_CHOICES = [

        ("pending", "Pending"),

        ("contacted", "Contacted"),

        ("closed", "Closed"),

    ]

    # NAME
    name = models.CharField(
        max_length=255
    )

    # MOBILE NUMBER
    number = models.CharField(
        max_length=20
    )

    # EMAIL
    email = models.EmailField(
        blank=True,
        null=True
    )

    # COMPANY NAME
    company_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    # INTERESTED PRODUCT
    interested_product = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    # SUITABLE TIME TO CONTACT
    suitable_time = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    # MESSAGE (OPTIONAL)
    message = models.TextField(
        blank=True,
        null=True
    )
    
    # STATUS
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="pending",
        blank=True,
        null=True
    )

    # SUBMITTED DATE & TIME
    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - {self.number}"



# from django.db import models
# from django.contrib.auth.models import User

# class Blog(models.Model):
#     title = models.CharField(max_length=1000)
#     subtitle = models.CharField(max_length=1000, blank=True, null=True)
#     description = models.TextField()
#     author = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_published = models.BooleanField(default=True)

#     def __str__(self):
#         return self.title


# #--------------------------------------------------------

# class ProductCategory(models.Model):
#     name = models.CharField(max_length=255)

#     short_description = models.TextField(blank=True)

#     image = models.ImageField(
#         upload_to='categories/',
#         blank=True,
#         null=True
#     )

#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# class ProductSubCategory(models.Model):
#     category = models.ForeignKey(
#         ProductCategory,
#         on_delete=models.CASCADE,
#         related_name='subcategories'
#     )

#     name = models.CharField(max_length=255)

#     short_description = models.TextField(blank=True)

#     long_description = models.TextField(blank=True)

#     image = models.ImageField(
#         upload_to='subcategories/',
#         blank=True,
#         null=True
#     )

#     benefits = models.TextField(blank=True,null=True)

#     specifications = models.TextField(blank=True,null=True)

#     packing_details = models.TextField(blank=True,null=True)

#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

class SupplierRegistration(models.Model):
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    product_category = models.CharField(max_length=255)
    manufacturing_capacity = models.TextField()
    export_experience = models.CharField(max_length=100)
    certifications = models.TextField()
    products_you_supply = models.TextField(blank=True, null=True)
    monthly_supply_capacity = models.CharField(max_length=255, blank=True, null=True)
    minimum_order_quantity = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=500, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    company_profile = models.FileField(upload_to='supplier_profiles/', blank=True, null=True)
    certifications_file = models.FileField(upload_to='supplier_certs/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} - {self.contact_person}"


class ProductEnquiry(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Contacted", "Contacted"),
        ("Quotation Sent", "Quotation Sent"),
        ("Follow Up", "Follow Up"),
        ("Closed", "Closed"),
        ("Rejected", "Rejected"),
    ]

    enquiry_no = models.CharField(max_length=50, unique=True, editable=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='product_enquiries')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='product_enquiries')
    product = models.ForeignKey(ProductSubCategory, on_delete=models.CASCADE, related_name='product_enquiries')
    customer_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    company_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.CharField(max_length=100, blank=True, null=True)
    suitable_call_time = models.CharField(max_length=255, blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    admin_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.enquiry_no:
            max_id = ProductEnquiry.objects.all().order_by("-id").first()
            next_id = (max_id.id + 1) if max_id else 1
            self.enquiry_no = f"BIMI-ENQ-{next_id:05d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.enquiry_no} - {self.customer_name}"


class EnquiryNote(models.Model):
    enquiry = models.ForeignKey(ProductEnquiry, on_delete=models.CASCADE, related_name='notes')
    admin_name = models.CharField(max_length=255)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note by {self.admin_name} on {self.created_at}"