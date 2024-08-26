from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/' , views.about , name='about'),
    path('terms/of/use/' , views.terms_of_use , name='terms_of_use'),
]
