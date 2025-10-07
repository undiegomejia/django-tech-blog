from django.shortcuts import render, redirect
from .forms import UserCreationForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        
        if 'remove_image' in request.POST:
            profile.image.delete(save=False)
            profile.image = 'default.jpg'
            profile.save()
            messages.success(request, 'Profile picture removed.')
            return redirect('profile')
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
        else:
            if not u_form.is_valid():
                messages.error(request, 'Please correct the error in your user information.')
            if not p_form.is_valid():
                messages.error(request, 'Please correct the error in your profile information.')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'user_form': u_form,
        'profile_form': p_form
    }
    return render(request, 'users/profile.html', context)