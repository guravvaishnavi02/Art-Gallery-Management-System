from django.urls import path
from .views import *
urlpatterns = [
    path('home', homeView),
    path('about', aboutView),
    path('articles', artView), 
    path('artists', artistView),
    path('contact', contactView),
    path('exhibitions', exhibView),
    path('galleries', galleryView),
    path('holdings', holdView),
    path('showcases', showView),
    path('purchases', purView),
    path('purchasers', purchasersView),
    path('insurances', insurView),
    path('insurance_companies', icompView),
    path('organizers', orgView) 
]
