from .recommender import Recommender
from django.shortcuts import render, get_object_or_404
from .models import Category, Types, Product
from cart.forms import CartAddProductForm


def category_list(request, category_slug=None):
    category = None
    categories = Category.objects.all().order_by('id')
    rolls = Product.objects.filter(category=1)[:8]
    sushi = Product.objects.filter(category=2)[:8]
    zakuski = Product.objects.filter(category=3)[:8]
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    return render(request,'shop/category/category_list.html',{'category': category,'categories': categories,'rolls': rolls, 'sushi': sushi, 'zakuski': zakuski})


def product_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    
    selected_types = request.GET.getlist('types')
    
    products = Product.objects.filter(category=category, available=True)
    for type_id in selected_types:
        products = products.filter(types__id=type_id)

    types = Types.objects.filter(category=category)

    return render(request, 'shop/product/list.html', {
        'products': products,
        'types': types,
        'selected_types': selected_types,
    })


def product_detail(request, id, slug):
    cart_product_form = CartAddProductForm()
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    types = [type for type in product.types.all()]
    r = Recommender()
    if r.suggest_products_for([product], 4):
        recommended_products = r.suggest_products_for([product], 4)
    else:
        recommended_products = (Product.objects.filter(category=product.category) & Product.objects.exclude(id=product.id))[:4]
    return render(request,'shop/product/detail.html',{'types': types,'product': product,'cart_product_form': cart_product_form,'recommended_products': recommended_products})

