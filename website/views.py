from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import Produit
from django.core import serializers
from django.http import JsonResponse

def produits(request):
    
    inv = dict()
    
    dict_categorie = dict()
    
    for cat in Produit.CATEGORIES_CHOICE:
        
        produit = Produit.objects.filter(categorie = cat[0])
        
        if cat[0] == Produit.EPICERIE:
            
            dict_categorie["Épicerie"] = "Épicerie fine".upper()
            
            inv["Épicerie"] = produit
        
        else :
            
            dict_categorie[cat[1]] = cat[1].upper()
            
            inv[cat[1]] = produit
        
    return render(request, 'website/produit.html', {'inv' : inv, 'categories' : dict_categorie})

def home(request):
    
    return render(request, 'website/index.html')

class ProduitView(View):
    def get(self, request):
        qs = Produit.objects.all()
        data = serializers.serialize('json', qs)
        return JsonResponse({'data' : data}, safe=False)
    
class TestView(TemplateView):
    template_name = 'website/test.html'
    

class ContactView(TemplateView):
    template_name = 'website/contact.html'
    
class ActualiteView(TemplateView):
    template_name = 'website/actualite.html'
    
class EquipeView(TemplateView):
    template_name = 'website/equipe.html'