from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.utils.timezone import localtime
from django.db.models import Q
from django.core.paginator import Paginator
from .models import SubCategory

# ---------- LOGIN ----------
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        # if user is not None:
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid admin credentials')
            return redirect('admin_login')

    return render(request, 'custom_admin/login.html')

#-------login-redirect------------

def redirect_to_login(request):
    return redirect('admin_login')


# ---------- DASHBOARD ----------
@login_required(login_url='admin_login')
def admin_dashboard(request):
    return render(request, 'custom_admin/dashboard.html')

@login_required(login_url='admin_login')
def blogs(request):

    search = request.GET.get('search')

    blogs = Blog.objects.all()

    # SEARCH FILTER
    if search:

        blogs = blogs.filter(

            Q(title__icontains=search) |

            Q(subtitle__icontains=search) |

            Q(description__icontains=search) |

            Q(author__icontains=search)

        )

    blogs = blogs.order_by('-created_at')

    # PAGINATION
    paginator = Paginator(blogs, 12)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search': search
    }

    return render(
        request,
        'custom_admin/blogs.html',
        context
    )

# ---------- LOGOUT ----------
def admin_logout(request):
    logout(request)
    return redirect('admin_login')


from django.contrib import messages
from .models import Blog

@login_required(login_url='admin_login')
def add_blog(request):
    if request.method == 'POST':
        title = request.POST.get('blog_title')
        subtitle = request.POST.get('blog_subtitle')
        description = request.POST.get('blog_description')
        author = request.POST.get('author_name')
        image = request.FILES.get('blog_image')

        if not title or not description or not author:
            messages.error(request, 'Title, description and author are required!')
            return redirect('create_blog')

        blog = Blog(
            title=title,
            subtitle=subtitle,
            description=description,
            author=author,
            image=image
        )
        blog.save()
        messages.success(request, 'Blog created successfully!')
        return redirect('blogs') 

    return render(request, 'custom_admin/add_blog.html')


@login_required(login_url='admin_login')
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()  # image auto delete ho jayegi
    messages.success(request, f'Blog "{blog.title}" deleted successfully.')
    return redirect('blogs')


#========================================================================================


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import ProductCategory, ProductSubCategory


# =====================================
# CATEGORY LIST
# =====================================

@login_required(login_url='admin_login')
def category_list(request):

    search = request.GET.get('search')

    categories = ProductCategory.objects.all()

    # SEARCH FILTER
    if search:

        categories = categories.filter(

            Q(name__icontains=search) |

            Q(short_description__icontains=search)

        )

    categories = categories.order_by('-id')

    # PAGINATION
    paginator = Paginator(categories, 12)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search': search
    }

    return render(
        request,
        'custom_admin/category_list.html',
        context
    )

# =====================================
# ADD CATEGORY
# =====================================
@login_required(login_url='admin_login')
def add_category(request):

    if request.method == 'POST':

        ProductCategory.objects.create(
            name=request.POST.get('name'),
            short_description=request.POST.get('short_description'),
            image=request.FILES.get('image')
        )

        messages.success(request, 'Category Added')
        return redirect('category_list')

    return render(request, 'custom_admin/add_category.html')


# =====================================
# EDIT CATEGORY
# =====================================
@login_required(login_url='admin_login')
def edit_category(request, pk):

    category = get_object_or_404(ProductCategory, id=pk)

    if request.method == 'POST':

        category.name = request.POST.get('name')

        category.short_description = request.POST.get(
            'short_description'
        )

        if request.FILES.get('image'):
            category.image = request.FILES.get('image')

        category.save()

        messages.success(request, 'Category Updated')

        return redirect('category_list')

    return render(
        request,
        'custom_admin/edit_category.html',
        {'category': category}
    )


# =====================================
# DELETE CATEGORY
# =====================================
@login_required(login_url='admin_login')
def delete_category(request, pk):

    category = get_object_or_404(ProductCategory, id=pk)

    category.delete()

    messages.success(request, 'Category Deleted')

    return redirect('category_list')


# =====================================
# CATEGORY DETAIL PAGE
# =====================================

@login_required(login_url='admin_login')
def category_detail(request, pk):

    category = get_object_or_404(
        ProductCategory,
        id=pk
    )

    search = request.GET.get('search')

    # REAL SUBCATEGORIES
    real_subcategories = SubCategory.objects.filter(
        category=category
    )

    # ============================================
    # IF CATEGORY HAS REAL SUBCATEGORIES
    # ============================================

    if real_subcategories.exists():

        if search:

            real_subcategories = real_subcategories.filter(

                Q(name__icontains=search) |

                Q(short_description__icontains=search)

            )

        real_subcategories = real_subcategories.order_by(
            '-id'
        )

        paginator = Paginator(
            real_subcategories,
            12
        )

        page_number = request.GET.get('page')

        page_obj = paginator.get_page(
            page_number
        )

        context = {
            'category': category,
            'page_obj': page_obj,
            'search': search,
            'has_real_subcategories': True
        }

        return render(
            request,
            'custom_admin/category_detail.html',
            context
        )

    # ============================================
    # DIRECT PRODUCTS
    # ============================================

    products = ProductSubCategory.objects.filter(
        category=category,
        subcategory__isnull=True
    )

    if search:

        products = products.filter(

            Q(name__icontains=search) |

            Q(short_description__icontains=search) |

            Q(long_description__icontains=search) |

            Q(benefits__icontains=search) |

            Q(specifications__icontains=search) |

            Q(packing_details__icontains=search)

        )

    products = products.order_by('-id')

    paginator = Paginator(products, 12)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'page_obj': page_obj,
        'search': search,
        'has_real_subcategories': False
    }

    return render(
        request,
        'custom_admin/category_detail.html',
        context
    )


# @login_required(login_url='admin_login')
# def category_detail(request, pk):

#     category = get_object_or_404(
#         ProductCategory,
#         id=pk
#     )

#     search = request.GET.get('search')

#     subcategories = ProductSubCategory.objects.filter(
#         category=category
#     )

#     # SEARCH FILTER
#     if search:

#         subcategories = subcategories.filter(

#             Q(name__icontains=search) |

#             Q(short_description__icontains=search) |

#             Q(long_description__icontains=search) |

#             Q(benefits__icontains=search) |

#             Q(specifications__icontains=search) |

#             Q(packing_details__icontains=search)

#         )

#     subcategories = subcategories.order_by('-id')

#     # PAGINATION
#     paginator = Paginator(subcategories, 12)

#     page_number = request.GET.get('page')

#     page_obj = paginator.get_page(page_number)

#     context = {
#         'category': category,
#         'page_obj': page_obj,
#         'search': search
#     }

#     return render(
#         request,
#         'custom_admin/category_detail.html',
#         context
#     )

@login_required(login_url='admin_login')
def subcategory_list(request):

    search = request.GET.get('search')

    subcategories = ProductSubCategory.objects.select_related(
        'category'
    ).all()

    # SEARCH FILTER
    if search:

        subcategories = subcategories.filter(

            Q(name__icontains=search) |

            Q(category__name__icontains=search) |

            Q(short_description__icontains=search) |

            Q(long_description__icontains=search) |

            Q(benefits__icontains=search) |

            Q(specifications__icontains=search) |

            Q(packing_details__icontains=search)

        )

    subcategories = subcategories.order_by('-id')

    # PAGINATION
    paginator = Paginator(subcategories, 12)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search': search
    }

    return render(
        request,
        'custom_admin/subcategory_list.html',
        context
    )

# =====================================
# ADD SUBCATEGORY
# =====================================
# @login_required(login_url='admin_login')
# def add_subcategory(request):

#     categories = ProductCategory.objects.all()

#     if request.method == 'POST':

#         category = ProductCategory.objects.get(
#             id=request.POST.get('category')
#         )

#         ProductSubCategory.objects.create(
#             category=category,
#             name=request.POST.get('name'),
#             short_description=request.POST.get(
#                 'short_description'
#             ),
#             long_description=request.POST.get(
#                 'long_description'
#             ),
#             benefits=request.POST.get('benefits'),
#             specifications=request.POST.get(
#                 'specifications'
#             ),
#             packing_details=request.POST.get(
#                 'packing_details'
#             ),
#             image=request.FILES.get('image')
#         )

#         messages.success(request, 'Subcategory Added')

#         return redirect('subcategory_list')

#     return render(
#         request,
#         'custom_admin/add_subcategory.html',
#         {'categories': categories}
#     )


@login_required(login_url='admin_login')
def add_subcategory(request):

    categories = ProductCategory.objects.all()

    subcategories = SubCategory.objects.select_related(
        'category'
    ).all()

    if request.method == 'POST':

        # CATEGORY
        category = get_object_or_404(
            ProductCategory,
            id=request.POST.get('category')
        )

        # SUBCATEGORY (OPTIONAL)
        subcategory = None

        subcategory_id = request.POST.get(
            'subcategory'
        )

        # CHECK SUBCATEGORY EXISTS
        if subcategory_id:

            subcategory = get_object_or_404(
                SubCategory,
                id=subcategory_id,
                category=category
            )

        # CREATE PRODUCT
        ProductSubCategory.objects.create(

            # CATEGORY
            category=category,

            # REAL SUBCATEGORY
            subcategory=subcategory,

            # PRODUCT NAME
            name=request.POST.get('name'),

            # SHORT DESCRIPTION
            short_description=request.POST.get(
                'short_description'
            ),

            # LONG DESCRIPTION
            long_description=request.POST.get(
                'long_description'
            ),

            # BENEFITS
            benefits=request.POST.get(
                'benefits'
            ),

            # SPECIFICATIONS
            specifications=request.POST.get(
                'specifications'
            ),

            # PACKING DETAILS
            packing_details=request.POST.get(
                'packing_details'
            ),

            # IMAGE
            image=request.FILES.get('image')

        )

        messages.success(
            request,
            'Product Added Successfully'
        )

        return redirect('subcategory_list')

    context = {
        'categories': categories,
        'subcategories': subcategories
    }

    return render(
        request,
        'custom_admin/add_subcategory.html',
        context
    )


# =====================================
# EDIT Product
# =====================================
# @login_required(login_url='admin_login')
# def edit_subcategory(request, pk):

#     subcategory = get_object_or_404(
#         ProductSubCategory,
#         id=pk
#     )

#     categories = ProductCategory.objects.all()

#     if request.method == 'POST':

#         subcategory.category = ProductCategory.objects.get(
#             id=request.POST.get('category')
#         )

#         subcategory.name = request.POST.get('name')

#         subcategory.short_description = request.POST.get(
#             'short_description'
#         )

#         subcategory.long_description = request.POST.get(
#             'long_description'
#         )

#         subcategory.benefits = request.POST.get(
#             'benefits'
#         )

#         subcategory.specifications = request.POST.get(
#             'specifications'
#         )

#         subcategory.packing_details = request.POST.get(
#             'packing_details'
#         )

#         if request.FILES.get('image'):
#             subcategory.image = request.FILES.get('image')

#         subcategory.save()

#         messages.success(request, 'Subcategory Updated')

#         return redirect('subcategory_list')

#     context = {
#         'subcategory': subcategory,
#         'categories': categories
#     }

#     return render(
#         request,
#         'custom_admin/edit_subcategory.html',
#         context
#     )

@login_required(login_url='admin_login')
def edit_subcategory(request, pk):

    subcategory = get_object_or_404(
        ProductSubCategory,
        id=pk
    )

    categories = ProductCategory.objects.all()

    real_subcategories = SubCategory.objects.select_related(
        'category'
    ).all()

    if request.method == 'POST':

        # CATEGORY
        category = get_object_or_404(
            ProductCategory,
            id=request.POST.get('category')
        )

        subcategory.category = category

        # REAL SUBCATEGORY
        subcategory_id = request.POST.get(
            'subcategory'
        )

        if subcategory_id:

            subcategory.subcategory = get_object_or_404(
                SubCategory,
                id=subcategory_id,
                category=category
            )

        else:

            subcategory.subcategory = None

        # PRODUCT NAME
        subcategory.name = request.POST.get(
            'name'
        )

        # SHORT DESCRIPTION
        subcategory.short_description = request.POST.get(
            'short_description'
        )

        # LONG DESCRIPTION
        subcategory.long_description = request.POST.get(
            'long_description'
        )

        # BENEFITS
        subcategory.benefits = request.POST.get(
            'benefits'
        )

        # SPECIFICATIONS
        subcategory.specifications = request.POST.get(
            'specifications'
        )

        # PACKING DETAILS
        subcategory.packing_details = request.POST.get(
            'packing_details'
        )

        # IMAGE
        if request.FILES.get('image'):

            subcategory.image = request.FILES.get(
                'image'
            )

        subcategory.save()

        messages.success(
            request,
            'Product Updated Successfully'
        )

        return redirect('subcategory_list')

    context = {
        'subcategory': subcategory,
        'categories': categories,
        'real_subcategories': real_subcategories
    }

    return render(
        request,
        'custom_admin/edit_subcategory.html',
        context
    )


# =====================================
# DELETE SUBCATEGORY
# =====================================
@login_required(login_url='admin_login')
def delete_subcategory(request, pk):

    subcategory = get_object_or_404(
        ProductSubCategory,
        id=pk
    )

    subcategory.delete()

    messages.success(request, 'Subcategory Deleted')

    return redirect('subcategory_list')


#===================Real Sub-category==================================
# =========================================================
# ADD SUBCATEGORY
# =========================================================

@login_required(login_url='admin_login')
def add_real_subcategory(request):

    categories = ProductCategory.objects.all()

    if request.method == 'POST':

        category_id = request.POST.get('category')

        name = request.POST.get('name')

        short_description = request.POST.get(
            'short_description'
        )

        image = request.FILES.get('image')

        category = get_object_or_404(
            ProductCategory,
            id=category_id
        )

        SubCategory.objects.create(
            category=category,
            name=name,
            short_description=short_description,
            image=image
        )

        messages.success(
            request,
            'SubCategory Added Successfully'
        )

        return redirect('real_subcategory_list')

    context = {
        'categories': categories
    }

    return render(
        request,
        'custom_admin/sub_category/add_real_subcategory.html',
        context
    )


# =========================================================
# SUBCATEGORY LIST
# =========================================================

@login_required(login_url='admin_login')
def real_subcategory_list(request, category_id=None):

    search = request.GET.get('search')

    category = None

    # BASE QUERY
    subcategories = SubCategory.objects.select_related(
        'category'
    ).all()

    # FILTER BY CATEGORY
    if category_id:

        category = get_object_or_404(
            ProductCategory,
            id=category_id
        )

        subcategories = subcategories.filter(
            category=category
        )

    # SEARCH
    if search:

        subcategories = subcategories.filter(

            Q(name__icontains=search) |

            Q(category__name__icontains=search) |

            Q(short_description__icontains=search)

        )

    # ORDER
    subcategories = subcategories.order_by('-id')

    # PAGINATION
    paginator = Paginator(subcategories, 12)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'page_obj': page_obj,
        'search': search
    }

    return render(
        request,
        'custom_admin/sub_category/real_subcategory_list.html',
        context
    )


# =========================================================
# EDIT SUBCATEGORY
# =========================================================

@login_required(login_url='admin_login')
def edit_real_subcategory(request, pk):

    subcategory = get_object_or_404(
        SubCategory,
        id=pk
    )

    categories = ProductCategory.objects.all()

    if request.method == 'POST':

        category_id = request.POST.get('category')

        subcategory.category = get_object_or_404(
            ProductCategory,
            id=category_id
        )

        subcategory.name = request.POST.get('name')

        subcategory.short_description = request.POST.get(
            'short_description'
        )

        image = request.FILES.get('image')

        if image:
            subcategory.image = image

        subcategory.save()

        messages.success(
            request,
            'SubCategory Updated Successfully'
        )

        return redirect('real_subcategory_list')

    context = {
        'subcategory': subcategory,
        'categories': categories
    }

    return render(
        request,
        'custom_admin/sub_category/edit_real_subcategory.html',
        context
    )


# =========================================================
# DELETE SUBCATEGORY
# =========================================================

@login_required(login_url='admin_login')
def delete_real_subcategory(request, pk):

    subcategory = get_object_or_404(
        SubCategory,
        id=pk
    )

    subcategory.delete()

    messages.success(
        request,
        'SubCategory Deleted Successfully'
    )

    return redirect('real_subcategory_list')


# =========================================================
# SUBCATEGORY PRODUCT LIST
# =========================================================

@login_required(login_url='admin_login')
def real_subcategory_products(request, pk):

    subcategory = get_object_or_404(
        SubCategory,
        id=pk
    )

    search = request.GET.get('search')

    products = ProductSubCategory.objects.filter(
        subcategory=subcategory
    )

    # SEARCH
    if search:

        products = products.filter(

            Q(name__icontains=search) |

            Q(short_description__icontains=search) |

            Q(long_description__icontains=search) |

            Q(benefits__icontains=search) |

            Q(specifications__icontains=search) |

            Q(packing_details__icontains=search)

        )

    products = products.order_by('-id')

    # PAGINATION
    paginator = Paginator(products, 12)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'subcategory': subcategory,
        'page_obj': page_obj,
        'search': search
    }

    return render(
        request,
        'custom_admin/sub_category/real_subcategory_products.html',
        context
    )
    
    
#==========================================================
# =========================================================
# admin_views.py
# =========================================================

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import ContactEnquiry


# =========================================================
# ENQUIRY LIST
# =========================================================

def enquiry_list(request):

    enquiries = ContactEnquiry.objects.all().order_by(
        '-id'
    )

    # =====================================================
    # SEARCH
    # =====================================================

    search = request.GET.get("search")

    if search:

        enquiries = enquiries.filter(

            Q(name__icontains=search) |
            Q(number__icontains=search) |
            Q(email__icontains=search) |
            Q(company_name__icontains=search) |
            Q(interested_product__icontains=search) |
            Q(status__icontains=search)

        )

    # =====================================================
    # STATUS FILTER
    # =====================================================

    status = request.GET.get("status")

    if status:

        enquiries = enquiries.filter(
            status=status
        )

    # =====================================================
    # PAGINATION
    # =====================================================

    paginator = Paginator(
        enquiries,
        20
    )

    page_number = request.GET.get("page")

    enquiries = paginator.get_page(
        page_number
    )

    context = {

        "enquiries": enquiries,

        "search": search,

        "status": status,

    }

    return render(
        request,
        "contact/enquiry_list.html",
        context
    )

# =========================================================
# ENQUIRY DETAIL
# =========================================================

def enquiry_detail(request, enquiry_id):

    enquiry = get_object_or_404(
        ContactEnquiry,
        id=enquiry_id
    )

    context = {
        "enquiry": enquiry
    }

    return render(
        request,
        "contact/enquiry_detail.html",
        context
    )


# =========================================================
# UPDATE STATUS
# =========================================================

def update_enquiry_status(request, enquiry_id):

    enquiry = get_object_or_404(
        ContactEnquiry,
        id=enquiry_id
    )

    if request.method == "POST":

        status = request.POST.get("status")

        enquiry.status = status

        enquiry.save()

        messages.success(
            request,
            "Status updated successfully."
        )

    return redirect(
        "enquiry_detail",
        enquiry_id=enquiry.id
    )


# =========================================================
# DELETE ENQUIRY
# =========================================================

def delete_enquiry(request, enquiry_id):

    enquiry = get_object_or_404(
        ContactEnquiry,
        id=enquiry_id
    )

    enquiry.delete()

    messages.success(
        request,
        "Enquiry deleted successfully."
    )

    return redirect("enquiry_list")

# ================================================