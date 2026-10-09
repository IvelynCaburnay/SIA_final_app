
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import Pet
from .forms import PetForm


def SignUp(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                'Your account was created successfully!'
            )
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


@login_required(login_url='login')
def Home(request):
    pets = Pet.objects.all().order_by('pet_id')

    return render(request, 'dashboard.html', {
        'pets': pets,
        'form': PetForm(),
        'dog_count': Pet.objects.filter(
            pet_type__iexact='Dog'
        ).count(),
        'cat_count': Pet.objects.filter(
            pet_type__iexact='Cat'
        ).count(),
    })


@login_required(login_url='login')
def AddPet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Pet added successfully!')
            return redirect('dashboard')

        return render(request, 'dashboard.html', {
            'pets': Pet.objects.all().order_by('pet_id'),
            'form': form,
            'dog_count': Pet.objects.filter(
                pet_type__iexact='Dog'
            ).count(),
            'cat_count': Pet.objects.filter(
                pet_type__iexact='Cat'
            ).count(),
            'modal_to_open': 'add',
        })

    return redirect('dashboard')


@login_required(login_url='login')
def EditPet(request, pet_id):
    pet = get_object_or_404(Pet, pet_id=pet_id)

    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)

        if form.is_valid():
            form.save()
            messages.success(request, 'Pet updated successfully!')
            return redirect('dashboard')
    else:
        form = PetForm(instance=pet)

    return render(request, 'edit_pet.html', {
        'form': form,
        'pet': pet,
    })


@login_required(login_url='login')
def DeletePet(request, pet_id):
    if request.method == 'POST':
        pet = get_object_or_404(Pet, pet_id=pet_id)
        pet.delete()
        messages.success(request, 'Pet deleted successfully!')

    return redirect('dashboard')