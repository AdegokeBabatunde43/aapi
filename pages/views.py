from django.shortcuts import render, redirect
from pages.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from pages.serializers import ProductSerializer
import requests


# Create your views here.
def home(request):
    all_product = Product.objects.all()
    return render(request, 'index.html', {'all_product': all_product})


def aboutus(request):
    return render(request, 'aboutus.html')


def contact(request):
    return render(request, 'contact.html')

def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        price = request.POST['price']
        
        form = Product(name=name, desc=desc, price=price)
        form.save()
        return redirect('/')
                
    return render(request, 'add.html')


def detail(request, id):    
    single_product = Product.objects.get(id=id)
    return render(request, 'detail.html', {'single_product': single_product})


def deleteitem(request, id):    
    single_product = Product.objects.get(id=id)
    single_product.delete()
    return redirect('/')

def movies(request):
    data = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = data.json()
    return render(request, 'movie.html', {'posts': posts})

# @api_view(['POST'])
# def createproduct(request):
#    products =  ProductSerializer(data=request.data)
#    if products.is_valid():
#        products.save()
#    return Response(products.data)
