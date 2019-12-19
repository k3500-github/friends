from django.contrib import admin
from django.urls import path
from quotes_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all/', views.allbest),
    path('features/', views.features),
]
