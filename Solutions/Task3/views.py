from pyexpat.errors import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Car
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from .forms import CarForm, AuthUserForm, RegisterUserForm, CommentForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)


class HomeListView(ListView):
    model = Car
    template_name = 'home.html'
    context_object_name = 'list_cars'


class HomeDetailView(CustomSuccessMessageMixin, FormMixin,DetailView):
    model = Car
    template_name = 'details.html'
    context_object_name = 'get_car'
    form_class = CommentForm
    success_msg = 'Комментарий добавлен'

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail_page', kwargs={'pk':self.get_object().id})

    def post(self,request,*args,**kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)






class CarCreateView(CustomSuccessMessageMixin, CreateView):
    model = Car
    template_name = 'edit_page.html'
    form_class = CarForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись добавлена'

    def get_context_data(self, **kwargs):
        kwargs['car_list'] = Car.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)


class CarUpdateView(LoginRequiredMixin,CustomSuccessMessageMixin, UpdateView):
    model = Car
    template_name = 'edit_page.html'
    form_class = CarForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class CarDeleteView(LoginRequiredMixin,DeleteView):
    model = Car
    template_name = 'edit_page.html'
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись удалена'

    def post(self,request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)


class MyprojectLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('edit_page')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Аккаунт зарегестрирован'


class MyProjectLogoutView(LogoutView):
    next_page = reverse_lazy('edit_page')

