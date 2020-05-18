"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Cars.views import HomeListView
from Cars.views import HomeDetailView, CarCreateView, CarUpdateView, CarDeleteView, MyprojectLoginView, RegisterUserView , MyProjectLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  HomeListView.as_view()),
    path('details/<int:pk>',  HomeDetailView.as_view(), name = 'detail_page'),
    path('edit_page',  CarCreateView.as_view(), name= 'edit_page'),
    path('update_page/<int:pk>',  CarUpdateView.as_view(), name='update_page'),
    path('delete_page/<int:pk>',  CarDeleteView.as_view(), name='delete_page'),
    path('login/',  MyprojectLoginView.as_view(), name='login_page'),
    path('register',  RegisterUserView.as_view(), name='register_page'),
    path('logout',  MyProjectLogoutView.as_view(), name='logout_page'),
    path('accounts/login/',  MyprojectLoginView.as_view(), name='login_page'),




]
