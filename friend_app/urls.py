from django.contrib import admin
from django.urls import path
from friend_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('all/', views.all ),
     path('best/', views.best),
]
