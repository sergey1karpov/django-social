from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class AuthCheckMiddleware(MiddlewareMixin):

    paths = [
        '/registration/',
        '/login/'
    ]

    def process_request(self, request):
        for path in self.paths:
            if request.path.startswith(path):
                if request.user.is_authenticated:
                    return redirect(reverse('blogger:main_page'))
