from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Product
from .forms import ProductForm

def public_index(request):
    products = Product.objects.all()
    return render(request, 'product/public_index.html', {'products': products})

def public_nosotros(request):
    return render(request, 'product/public_nosotros.html', {})

@login_required
@permission_required('products.change_product', login_url='/')
def index(request):
    products = Product.objects.all()
    form = ProductForm()
    return render(request, 'product/index.html', {'products': products, "form": form})

@login_required
@permission_required('products.change_product', login_url='/')
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'status':200}) 
        return JsonResponse({'status':"error"})

def view(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product/view.html', {'product': product})

def viewData(request, id):
    productDB = Product.objects.get(id=id)
    product = {
        'id': productDB.id,
        'img': productDB.image_path.url,
        'name': productDB.name,
        'description': productDB.description,
        'price': productDB.price
        }
    return JsonResponse(product)

def delete(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return JsonResponse({'status':200})
    return JsonResponse({'status':'error'}) 

def update(request, id):
    product = Product.objects.get(id=id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({'status':200})
        return JsonResponse({'status':'error'})

