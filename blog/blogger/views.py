from django.shortcuts import render


def main_page(request):
    return render(request, 'blogger/pages/main_page.html')
