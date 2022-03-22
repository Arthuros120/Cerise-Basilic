from django.urls import path
from .views import ActualiteView, ContactView, produits, home, ProduitView, TestView, EquipeView

urlpatterns = [
    path('produit', produits, name='produits'),
    path('', home, name='home'),
    path('data-json/', ProduitView.as_view(), name='data-json'),
    path('testPage', TestView.as_view(), name='testPage'),
    path('contact', ContactView.as_view(), name='contact'),
    path('actu', ActualiteView.as_view(), name='actu'),
    path('equipe', EquipeView.as_view(), name='equipe'),
]