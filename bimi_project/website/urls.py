from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    
    #======================Products===================================
    # path('products-category/',views.categories,name='products_category'),
    # path('products-list/<int:pk>/',views.Products_list,name='products_list'),
    # path('product-detail/<int:pk>/',views.product_detail,name='product_detail'),
    
    path(
    'products-category/',
    views.categories,
    name='products_category'
),

# CATEGORY DETAIL
path(
    'products-list/<int:pk>/',
    views.Products_list,
    name='products_list'
),

# SUBCATEGORY PRODUCTS
path(
    'subcategory-products/<int:pk>/',
    views.subcategory_products,
    name='subcategory_products'
),

# PRODUCT DETAIL
path(
    'product-detail/<int:pk>/',
    views.product_detail,
    name='product_detail'
),
    #======================Blogs=======================================
    path("blogs/", views.blog_list, name="blog_list"),
    # path("blogs/detail/", views.blog_detail, name="blog_detail"),
    path('blog/<int:pk>/',views.blog_detail,name='blog_detail'),
    
]

