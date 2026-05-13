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
    interested_product = models.ForeignKey(
        ProductSubCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='enquiries'
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