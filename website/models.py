from django.conf import settings
from django.db import models
from django.utils import timezone


class Produit(models.Model):
    
    LEGUME = 'LEG'
    FRUIT = 'FRU'
    CHARCUTERIE = 'CHA'
    EPICERIE = 'EPI'
    FROMAGE = 'FRO'
    
    KILOGRAM = "KG"
    LITRE = "L"
    UNITE = 'U'
    
    CATEGORIES_CHOICE = [
        (FRUIT, 'Fruits'),
        (LEGUME, 'Legumes'),
        (FROMAGE, 'Fromages'),
        (CHARCUTERIE, 'Charcuteries'),
        (EPICERIE, 'Épicerie fine'),
    ]
    
    UNITE_CHOICE = [
        (KILOGRAM, 'Kilo'),
        (LITRE, 'Litre'),
        (UNITE, 'Unite'),
    ]
    
    name = models.CharField(max_length=50)
    
    categorie = models.CharField(max_length=3, choices=CATEGORIES_CHOICE, default=LEGUME,)

    image = models.ImageField(upload_to='img/produit', null=True, blank=True)
    
    description = models.CharField(max_length=100)

    price = models.FloatField(max_length=4)
    
    unite = models.CharField(max_length=2, choices=UNITE_CHOICE, default=KILOGRAM,)
    
    disponibile = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200)
    
    text = models.TextField()
    
    created_date = models.DateTimeField(default=timezone.now)
    
    published_date = models.DateTimeField(blank=True, null=True)
    

    def publish(self):
        
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title    