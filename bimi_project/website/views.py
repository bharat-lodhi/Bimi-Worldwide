from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from custom_admin.models import ProductCategory,ProductSubCategory,Blog,SubCategory
from django.db.models import Q

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

# def categories(request):

#     search = request.GET.get('search')

#     categories = ProductCategory.objects.all()

#     # SEARCH FILTER
#     if search:

#         categories = categories.filter(

#             Q(name__icontains=search) |

#             Q(short_description__icontains=search)

#         )

#     categories = categories.order_by('-id')

#     paginator = Paginator(categories, 20)

#     page_number = request.GET.get('page')

#     page_obj = paginator.get_page(page_number)

#     context = {
#         'page_obj': page_obj,
#         'search': search
#     }

#     return render(
#         request,
#         'categories.html',
#         context
#     )


# def Products_list(request, pk):

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

#     paginator = Paginator(subcategories, 20)

#     page_number = request.GET.get('page')

#     page_obj = paginator.get_page(page_number)

#     context = {
#         'category': category,
#         'page_obj': page_obj,
#         'search': search
#     }

#     return render(
#         request,
#         'Products_list.html',
#         context
#     )
    

# def product_detail(request, pk):

#     product = get_object_or_404(
#         ProductSubCategory,
#         id=pk
#     )

#     related_products = ProductSubCategory.objects.filter(
#         category=product.category
#     ).exclude(
#         id=product.id
#     ).order_by('-id')[:6]

#     context = {
#         'product': product,
#         'related_products': related_products
#     }

#     return render(
#         request,
#         'product_detail.html',
#         context
#     )
    

# ============================================
# CATEGORIES
# ============================================

def categories(request):

    search = request.GET.get('search')

    categories = ProductCategory.objects.all()

    # SEARCH FILTER
    if search:

        categories = categories.filter(

            Q(name__icontains=search) |

            Q(short_description__icontains=search)

        )

    categories = categories.order_by('-id')

    paginator = Paginator(categories, 20)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search': search
    }

    return render(
        request,
        'categories.html',
        context
    )


# ============================================
# CATEGORY DETAIL
# ============================================

def Products_list(request, pk):

    category = get_object_or_404(
        ProductCategory,
        id=pk
    )

    search = request.GET.get('search')

    # ============================================
    # CHECK REAL SUBCATEGORIES
    # ============================================

    real_subcategories = SubCategory.objects.filter(
        category=category
    )

    # ============================================
    # IF REAL SUBCATEGORY EXISTS
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
            20
        )

        page_number = request.GET.get('page')

        page_obj = paginator.get_page(
            page_number
        )

        context = {
            'category': category,
            'page_obj': page_obj,
            'search': search,
            'has_subcategories': True
        }

        return render(
            request,
            'category_subcategories.html',
            context
        )

    # ============================================
    # DIRECT PRODUCTS
    # ============================================

    products = ProductSubCategory.objects.filter(
        category=category,
        subcategory__isnull=True
    )

    # SEARCH FILTER
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

    paginator = Paginator(products, 20)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'page_obj': page_obj,
        'search': search,
        'has_subcategories': False
    }

    return render(
        request,
        'Products_list.html',
        context
    )


# ============================================
# SUBCATEGORY PRODUCTS
# ============================================

def subcategory_products(request, pk):

    subcategory = get_object_or_404(
        SubCategory,
        id=pk
    )

    search = request.GET.get('search')

    products = ProductSubCategory.objects.filter(
        subcategory=subcategory
    )

    # SEARCH FILTER
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

    paginator = Paginator(products, 20)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'subcategory': subcategory,
        'page_obj': page_obj,
        'search': search
    }

    return render(
        request,
        'Products_list.html',
        context
    )


# ============================================
# PRODUCT DETAIL
# ============================================

def product_detail(request, pk):

    product = get_object_or_404(
        ProductSubCategory,
        id=pk
    )

    # ============================================
    # RELATED PRODUCTS
    # ============================================

    if product.subcategory:

        related_products = ProductSubCategory.objects.filter(

            subcategory=product.subcategory

        ).exclude(

            id=product.id

        ).order_by('-id')[:6]

    else:

        related_products = ProductSubCategory.objects.filter(

            category=product.category,
            subcategory__isnull=True

        ).exclude(

            id=product.id

        ).order_by('-id')[:6]

    context = {
        'product': product,
        'related_products': related_products
    }

    return render(
        request,
        'product_detail.html',
        context
    )

#===================Blogs======================================

def blog_list(request):

    blogs = Blog.objects.filter(
        is_published=True
    ).order_by('-created_at')

    paginator = Paginator(blogs, 12)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(
        request,
        "blog_list.html",
        context
    )

def blog_detail(request, pk):

    blog = get_object_or_404(
        Blog,
        id=pk,
        is_published=True
    )

    related_blogs = Blog.objects.filter(
        is_published=True
    ).exclude(
        id=blog.id
    ).order_by('-created_at')[:6]

    context = {
        'blog': blog,
        'related_blogs': related_blogs
    }

    return render(
        request,
        "blog_detail.html",
        context
    )
#===============================================================