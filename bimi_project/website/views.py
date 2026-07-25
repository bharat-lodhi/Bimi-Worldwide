from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from custom_admin.models import ProductCategory,ProductSubCategory,Blog,SubCategory,SupplierRegistration,ProductEnquiry
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
import json

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
# =========================================================

from django.shortcuts import render, redirect
from django.contrib import messages


from custom_admin.models import ProductSubCategory,ContactEnquiry
from bimi_project.send_otp import send_email_otp

# =========================================================
# CONTACT FORM + OTP VERIFY
# =========================================================

# def contact_form(request):

#     show_otp_field = False

#     # FORM DATA DEFAULT
#     form_data = {
#         "name": "",
#         "number": "",
#         "email": "",
#         "company_name": "",
#         "interested_product": "",
#         "suitable_time": "",
#         "message": "",
#     }

#     # =====================================================
#     # SEND OTP
#     # =====================================================

#     if request.method == "POST" and "send_otp" in request.POST:

#         # GET FORM DATA
#         form_data = {
#             "name": request.POST.get("name"),
#             "number": request.POST.get("number"),
#             "email": request.POST.get("email"),
#             "company_name": request.POST.get("company_name"),
#             "interested_product": request.POST.get("interested_product"),
#             "suitable_time": request.POST.get("suitable_time"),
#             "message": request.POST.get("message"),
#         }

#         # SEND OTP
#         otp = send_email_otp(form_data["email"])

#         # SAVE FORM DATA
#         request.session['contact_form_data'] = form_data

#         # SAVE OTP
#         request.session['contact_otp'] = str(otp)

#         show_otp_field = True

#         messages.success(
#             request,
#             "OTP sent to your email."
#         )

#     # =====================================================
#     # VERIFY OTP
#     # =====================================================

#     elif request.method == "POST" and "verify_otp" in request.POST:

#         entered_otp = request.POST.get("otp")

#         saved_otp = request.session.get("contact_otp")

#         form_data = request.session.get(
#             "contact_form_data",
#             {}
#         )

#         show_otp_field = True

#         # OTP EMPTY
#         if not entered_otp:

#             messages.error(
#                 request,
#                 "Please enter OTP."
#             )

#         # OTP INVALID
#         elif entered_otp != saved_otp:

#             messages.error(
#                 request,
#                 "Invalid OTP."
#             )

#         # OTP CORRECT
#         else:

#             # SAVE DATA
#             ContactEnquiry.objects.create(
#                 name=form_data.get("name"),
#                 number=form_data.get("number"),
#                 email=form_data.get("email"),
#                 company_name=form_data.get("company_name"),
#                 interested_product=form_data.get("interested_product"),
#                 suitable_time=form_data.get("suitable_time"),
#                 message=form_data.get("message"),
#             )

#             # CLEAR SESSION
#             del request.session['contact_form_data']
#             del request.session['contact_otp']

#             messages.success(
#                 request,
#                 "Your enquiry submitted successfully."
#             )

#             return redirect("contact_form")

#     context = {
#         "show_otp_field": show_otp_field,
#         "form_data": form_data,
#     }

#     return render(
#         request,
#         "contact_form.html",
#         context
#     )

# =========================================================
# CONTACT FORM + OTP VERIFY
# =========================================================

def contact_form(request):

    # =====================================================
    # DEFAULTS
    # =====================================================

    show_otp_field = False

    form_data = request.session.get(
        "contact_form_data",
        {
            "name": "",
            "number": "",
            "email": "",
            "company_name": "",
            "interested_product": "",
            "suitable_time": "",
            "message": "",
        }
    )

    # =====================================================
    # IF OTP ALREADY EXISTS
    # =====================================================

    if request.session.get("contact_otp"):

        show_otp_field = True

    # =====================================================
    # SEND OTP
    # =====================================================

    if request.method == "POST" and "send_otp" in request.POST:

        # GET FORM DATA
        form_data = {
            "name": request.POST.get("name"),
            "number": request.POST.get("number"),
            "email": request.POST.get("email"),
            "company_name": request.POST.get("company_name"),
            "interested_product": request.POST.get("interested_product"),
            "suitable_time": request.POST.get("suitable_time"),
            "message": request.POST.get("message"),
        }

        # SEND OTP
        otp = send_email_otp(form_data["email"])

        # SAVE SESSION
        request.session['contact_form_data'] = form_data

        request.session['contact_otp'] = str(otp)
        request.session['otp_created_at'] = timezone.now().isoformat()

        show_otp_field = True

        messages.success(
            request,
            "OTP sent to your email."
        )

    # =====================================================
    # VERIFY OTP
    # =====================================================

    elif request.method == "POST" and "verify_otp" in request.POST:

        entered_otp = request.POST.get("otp")

        saved_otp = request.session.get(
            "contact_otp"
        )
        
        otp_created_at = request.session.get("otp_created_at")
        
        if otp_created_at:

            otp_time = timezone.datetime.fromisoformat(
                otp_created_at
            )

            # EXPIRE AFTER 10 MINUTES
            if timezone.now() > otp_time + timedelta(minutes=10):

                # CLEAR ONLY CONTACT FORM SESSION
                del request.session['contact_form_data']

                del request.session['contact_otp']

                del request.session['otp_created_at']

                messages.error(
                    request,
                    "OTP expired. Please try again."
                )

                return redirect("contact_form")

        # EMPTY OTP
        if not entered_otp:

            messages.error(
                request,
                "Please enter OTP."
            )

        # INVALID OTP
        elif entered_otp != saved_otp:

            messages.error(
                request,
                "Invalid OTP."
            )

        # VALID OTP
        else:

            # SAVE DATA
            ContactEnquiry.objects.create(
                name=form_data.get("name"),
                number=form_data.get("number"),
                email=form_data.get("email"),
                company_name=form_data.get("company_name"),
                interested_product=form_data.get("interested_product"),
                suitable_time=form_data.get("suitable_time"),
                message=form_data.get("message"),
            )

            # CLEAR SESSION
            del request.session['contact_form_data']
            del request.session['contact_otp']

            messages.success(
                request,
                "Your enquiry submitted successfully."
            )

            return redirect("contact_form")

    context = {
        "show_otp_field": show_otp_field,
        "form_data": form_data,
    }

    return render(
        request,
        "contact_form.html",
        context
    )
# ==================================================================

def why_us(request):
    return render(request, "why_us.html")

def become_supplier(request):
    if request.method == "POST":
        company_name = request.POST.get("company_name")
        contact_person = request.POST.get("contact_person")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        country = request.POST.get("country")
        product_category = request.POST.get("product_category")
        manufacturing_capacity = request.POST.get("manufacturing_capacity")
        export_experience = request.POST.get("export_experience")
        
        # Get list of checked certifications and join them
        certifications_list = request.POST.getlist("certifications")
        certifications = ", ".join(certifications_list)
        other_certification = request.POST.get("other_certification")
        if other_certification and "Other" in certifications_list:
            certifications += f" (Other: {other_certification})"
            
        products_you_supply = request.POST.get("products_you_supply")
        custom_product = request.POST.get("custom_product")
        if products_you_supply == "Other" and custom_product:
            products_you_supply = custom_product
            
        monthly_supply_capacity = request.POST.get("monthly_supply_capacity")
        minimum_order_quantity = request.POST.get("minimum_order_quantity")
        
        website = request.POST.get("website")
        message = request.POST.get("message")
        
        company_profile = request.FILES.get("company_profile")
        certifications_file = request.FILES.get("certifications_file")

        SupplierRegistration.objects.create(
            company_name=company_name,
            contact_person=contact_person,
            email=email,
            phone_number=phone_number,
            country=country,
            product_category=product_category,
            manufacturing_capacity=manufacturing_capacity,
            export_experience=export_experience,
            certifications=certifications,
            products_you_supply=products_you_supply,
            monthly_supply_capacity=monthly_supply_capacity,
            minimum_order_quantity=minimum_order_quantity,
            website=website,
            message=message,
            company_profile=company_profile,
            certifications_file=certifications_file
        )
        
        messages.success(request, "Your application has been submitted successfully. Our sourcing team will review it and get back to you soon.")
        return redirect("become_supplier")
        
    return render(request, "become_supplier.html")


def submit_product_enquiry(request):
    if request.method != 'POST':
        return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)

    # Support JSON or form-encoded POST
    if request.content_type == 'application/json':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON data."}, status=400)
    else:
        data = request.POST

    customer_name = data.get("customer_name")
    mobile = data.get("mobile")
    email = data.get("email")
    company_name = data.get("company_name", "")
    category_id = data.get("category_id")
    sub_category_id = data.get("sub_category_id")
    product_id = data.get("product_id")
    suitable_call_time = data.get("suitable_call_time", "")
    address = data.get("address", "")
    country = data.get("country", "")
    state = data.get("state", "")
    city = data.get("city", "")
    pincode = data.get("pincode", "")
    quantity = data.get("quantity", "")
    requirements = data.get("requirements", "")

    # Validate required fields
    if not all([customer_name, mobile, email, product_id, category_id]):
        return JsonResponse({"status": "error", "message": "Please fill in all required fields marked with *."}, status=400)

    # Basic validations
    if "@" not in email or "." not in email:
        return JsonResponse({"status": "error", "message": "Please enter a valid email address."}, status=400)

    clean_mobile = "".join(filter(str.isdigit, mobile))
    if len(clean_mobile) < 7:
        return JsonResponse({"status": "error", "message": "Please enter a valid mobile number."}, status=400)

    # Fetch referenced models
    category = get_object_or_404(ProductCategory, id=category_id)
    product = get_object_or_404(ProductSubCategory, id=product_id)
    sub_category = None
    if sub_category_id:
        sub_category = get_object_or_404(SubCategory, id=sub_category_id)

    # Spam Protection (within last 5 minutes)
    time_threshold = timezone.now() - timedelta(minutes=5)
    recent_enquiry = ProductEnquiry.objects.filter(
        email=email,
        mobile=mobile,
        product=product,
        created_at__gte=time_threshold
    ).exists()

    if recent_enquiry:
        return JsonResponse({
            "status": "error", 
            "message": "We have already received an enquiry from you for this product recently. Please try again after 5 minutes."
        }, status=429)

    # Create Product Enquiry
    ProductEnquiry.objects.create(
        category=category,
        sub_category=sub_category,
        product=product,
        customer_name=customer_name,
        mobile=mobile,
        email=email,
        company_name=company_name,
        address=address,
        country=country,
        state=state,
        city=city,
        pincode=pincode,
        quantity=quantity,
        suitable_call_time=suitable_call_time,
        requirements=requirements,
        status="Pending"
    )

    return JsonResponse({
        "status": "success", 
        "message": "Your product enquiry has been submitted successfully! Our sales team will get back to you soon."
    })