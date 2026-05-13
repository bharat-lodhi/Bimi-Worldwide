from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_login, name='redirect_to_login'),
    path('login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('blogs/',views.blogs, name="blogs"),
    path('add_blog/',views.add_blog, name="add_blog"),
    path('blogs/delete/<int:pk>/', views.delete_blog, name='delete_blog'),
        

    # Category
    path(
        'categories/',
        views.category_list,
        name='category_list'
    ),

    path(
        'add-category/',
        views.add_category,
        name='add_category'
    ),

    path(
        'edit-category/<int:pk>/',
        views.edit_category,
        name='edit_category'
    ),

    path(
        'delete-category/<int:pk>/',
        views.delete_category,
        name='delete_category'
    ),

    path(
        'category/<int:pk>/',
        views.category_detail,
        name='category_detail'
    ),

    # ========================Products URL ===========================
    path(
        'subcategories/',
        views.subcategory_list,
        name='subcategory_list'
    ),

    path(
        'add-subcategory/',
        views.add_subcategory,
        name='add_subcategory'
    ),

    path(
        'edit-subcategory/<int:pk>/',
        views.edit_subcategory,
        name='edit_subcategory'
    ),

    path(
        'delete-subcategory/<int:pk>/',
        views.delete_subcategory,
        name='delete_subcategory'
    ),
    #====================Products URL END ======================
    
    # =========================================================
    # Subcategories
    # =========================================================
    
    path(
    'real-subcategories/',
    views.real_subcategory_list,
    name='category_real_subcategory_list'
    ),
    
    path(
    'real-subcategories/<int:category_id>/',
    views.real_subcategory_list,
    name='category_real_subcategory_list'
    ),

    path(
        'add-real-subcategory/',
        views.add_real_subcategory,
        name='add_real_subcategory'
    ),

    path(
        'edit-real-subcategory/<int:pk>/',
        views.edit_real_subcategory,
        name='edit_real_subcategory'
    ),

    path(
        'delete-real-subcategory/<int:pk>/',
        views.delete_real_subcategory,
        name='delete_real_subcategory'
    ),

    path(
        'real-subcategory-products/<int:pk>/',
        views.real_subcategory_products,
        name='real_subcategory_products'
    ),
    
    #==========Contact Form==========================
   

    path(
        'enquiries/',
        views.enquiry_list,
        name='enquiry_list'
    ),

    path(
        'enquiry/<int:enquiry_id>/',
        views.enquiry_detail,
        name='enquiry_detail'
    ),

    path(
        'enquiry-status/<int:enquiry_id>/',
        views.update_enquiry_status,
        name='update_enquiry_status'
    ),

    path(
        'enquiry-delete/<int:enquiry_id>/',
        views.delete_enquiry,
        name='delete_enquiry'
    ),
    
]