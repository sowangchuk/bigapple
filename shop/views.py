# from datetime import timezone
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product, activelanding, featureProduct, landing1,address, service



from django.core.paginator import Paginator

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    

    artpost = products.all()
    paginator = Paginator(artpost, per_page=6)
    page_object = request.GET.get('page')
    service = paginator.get_page(page_object)
    totalpage = service.paginator.num_pages

 
    context = { 
        'category': category, 'categories': categories, 'products': products,
        
        'service': service,
        'lastpage': totalpage,
        'totalpagelist':[n+1 for n in range(totalpage)],
        
    }
    return render(request, 'shop/product/list.html', context)




def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    fproduct = featureProduct.objects.filter(available=True).order_by('-created')[:3]
    context = {'product': product, 'cart_product_form': cart_product_form, 'fproduct' :fproduct,}
    return render(request, 'shop/product/detail.html', context)


def home(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    display1 = landing1.objects.all().order_by('-created')[:2]
    display2 = activelanding.objects.all().order_by('-created')[:1]
    fproduct = featureProduct.objects.filter(available=True).order_by('-created')[:3]

    add = address.objects.all().order_by()[:1]
    ser = service.objects.all().order_by()[:1] 
    context = {
        'category': category,
        'categories': categories, 
        'products': products,
        'display1':display1,
        'display2':display2,
        'fproduct' :fproduct,
        'add':add,
        'ser':ser,
        
    }
    return render(request, 'shop/home.html', context)

def search(request):
    searched = request.GET['searched']
    user = Product.objects.filter(name__icontains= searched)
    context={
        'user': user,
    }
    return render(request, 'shop/search.html', context )