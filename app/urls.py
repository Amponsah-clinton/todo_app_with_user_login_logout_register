from django.urls import path 
from .import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register_user, name='register_user'),
    path('update/<int:id>', views.Update, name='update'),
    path('delete/<int:id>', views.Delete, name='delete'),
    path('', views.login_user, name='login')
]
