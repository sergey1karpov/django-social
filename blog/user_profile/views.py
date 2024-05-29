from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import UserProfile


@login_required(login_url='auth_module:login')
def profile_info(request):
    user = request.user
    return render(request, 'user_profile/profile_info.html', {user: user})


@login_required(login_url='auth_module:login')
def edit_profile_info(request):
    if request.method == 'GET':
        return render(request, 'user_profile/forms/edit_info.html', {'user': request.user})

    if request.method == 'POST':
        user = get_object_or_404(User, id=request.user.id)

        user.profile.phone_number = request.POST.get('phone_number')
        user.profile.mobile_number = request.POST.get('mobile_number')
        user.profile.city = request.POST.get('city')
        user.profile.country = request.POST.get('country')
        user.profile.job_title = request.POST.get('job_title')
        user.profile.company = request.POST.get('company')
        user.profile.avatar = request.FILES.get('avatar')
        user.profile.save()

        return redirect(reverse('user_profile:profile_information'), user=user)
