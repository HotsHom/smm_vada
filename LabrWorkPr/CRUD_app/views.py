from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required  
from .forms import socialNetworksForm, socialNetworksForm_types
from CRUD_app.models import socialNetworks,socialNetworks_types 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect

# Create your views here.
def home_page_cn(request):
    return render(request, 'Home_Page.html')  

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "register.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")

@login_required  
def socialNetworks_list(request):  
     if request.user.is_superuser:  
         socialNetworkss = socialNetworks.objects.select_related().all(); 
     else:  
         socialNetworkss = socialNetworks.objects.filter(user=request.user)  
     return render(request, 'socialNetworks_list.html', {  
         'object_list': socialNetworkss  
     })  
  
  
@login_required  
def socialNetworks_create(request):  
     form = socialNetworksForm(request.POST or None)  
   
     if form.is_valid():  
         socialNetworkss = form.save(commit=False)  
         socialNetworkss.user = request.user  
         socialNetworkss.save()  
         return redirect('CRUD_app:socialNetworks_list')  
     return render(request, 'socialNetworks_form.html', {'form': form})  
  
  
@login_required  
def socialNetworks_update(request, pk):  
     if request.user.is_superuser:  
         socialNetworkss = get_object_or_404(socialNetworks, pk=pk)  
     else:  
         socialNetworkss = get_object_or_404(socialNetworks, pk=pk, user=request.user)  
     form = socialNetworksForm(request.POST or None, instance=socialNetworkss)  
     if form.is_valid():  
         form.save()  
         return redirect('CRUD_app:socialNetworks_list')  
     return render(request, 'socialNetworks_form.html', {'form': form})  
  
  
@login_required  
def socialNetworks_delete(request, pk):  
     if request.user.is_superuser:  
         socialNetworkss = get_object_or_404(socialNetworks, pk=pk)  
     else:  
         socialNetworkss = get_object_or_404(socialNetworks, pk=pk, user=request.user)  
     if request.method == 'POST':  
         socialNetworkss.delete()  
         return redirect('CRUD_app:socialNetworks_list')  
     return render(request, 'socialNetworks_delete.html', {'object': socialNetworks})

#socialNetworks_types

@login_required  
def socialNetworks_types_list(request):  
     if request.user.is_superuser:  
         socialNetworks = socialNetworks_types.objects.all()  
     else:  
         socialNetworks = socialNetworks_types.objects.filter(user=request.user)  
     return render(request, 'socialNetworks_list.html', {  
         'object_list': socialNetworks  
     })  
  
  
@login_required  
def socialNetworks_types_create(request):  
     form = socialNetworksForm_types(request.POST or None)  
   
     if form.is_valid():  
         socialNetworks = form.save(commit=False)  
         socialNetworks.user = request.user  
         socialNetworks.save()  
         return redirect('CRUD_app:socialNetworks_list')  
     return render(request, 'socialNetworks_form.html', {'form': form})  
  
  
@login_required  
def socialNetworks_types_update(request, pk):  
     if request.user.is_superuser:  
         socialNetworks = get_object_or_404(socialNetworks_types, pk=pk)  
     else:  
         socialNetworks = get_object_or_404(socialNetworks_types, pk=pk, user=request.user)  
     form = socialNetworksForm_types(request.POST or None, instance=socialNetworks)  
     if form.is_valid():  
         form.save()  
         return redirect('CRUD_app:socialNetworks_list')  
     return render(request, 'socialNetworks_form.html', {'form': form})  
  
  
@login_required  
def socialNetworks_types_delete(request, pk):  
     if request.user.is_superuser:  
         socialNetworks = get_object_or_404(socialNetworks_types, pk=pk)  
     else:  
         socialNetworks = get_object_or_404(socialNetworks_types, pk=pk, user=request.user)  
     if request.method == 'POST':  
         socialNetworks.delete()  
         return redirect('CRUD_app:socialNetworks_list')  
     return render(request, 'confirm_delete.html', {'object': socialNetworks})