
from django.urls import path
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

from .views import SignUp, Home, AddPet, EditPet, DeletePet

urlpatterns = [
    path('', lambda request: redirect('dashboard'), name='home'),

    path('signup/', SignUp, name='signup'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html',
            redirect_authenticated_user=True
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='login'),
        name='logout'
    ),

    path('dashboard/', Home, name='dashboard'),
    path('add-pet/', AddPet, name='add_pet'),
    path('edit-pet/<int:pet_id>/', EditPet, name='edit_pet'),
    path('delete-pet/<int:pet_id>/', DeletePet, name='delete_pet'),
]