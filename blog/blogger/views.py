from django.shortcuts import render
from .models import BlogPost
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages


def main_page(request):
    return render(request, 'blogger/pages/main_page.html')


def create_post(request):
    print(request.POST.get('title'))
    post = BlogPost()
    post.title = request.POST.get('title')
    post.short_description = request.POST.get('short_description')
    post.full_description = request.POST.get('full_description')
    post.user = request.user
    post.photo = request.FILES.get('photo') if request.FILES.get('photo') else ''
 
    try:
        post.full_clean()
    except ValidationError as e:
        for error in e:
            messages.error(request, error)
        return redirect(reverse('user_profile:profile_information'))
    else:
        post.save()    

    return redirect(reverse('user_profile:profile_information'))