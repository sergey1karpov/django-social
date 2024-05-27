from django.contrib.auth import login
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class RegistrationTest(TestCase):
    def test_registration(self):
        data = {
            'username': 'sergey1karpov',
            'email': 'new_user@example.com',
            'password': 'password1',
        }
        response = self.client.post('http://127.0.0.1:8000/registration/', data)
        self.assertEqual(response.status_code, 302)  # Проверяем, что после регистрации происходит редирект
        self.assertEqual(response['Location'], '/')  # Проверяем URL, на который происходит редирект
        self.assertTrue(
            User.objects.filter(username='sergey1karpov').exists())  # Проверяем, что пользователь был создан

        # Проверяем, что пользователь аутентифицирован
        self.assertEqual(self.client.login(username='sergey1karpov', password='password1'), True)

        # Проверяем, что пользователь видит главную страницу
        response = self.client.get(reverse('blogger:main_page'))
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        #создали юзера в бд
        User.objects.create_user(
            username='sergey1karpov',
            password='password',
            email='sergey1karpov@example.com'
        )

        response = self.client.post('http://127.0.0.1:8000/login/', {
            'username': 'sergey1karpov',
            'password': 'password'
        })

        # Проверяем, что пользователь аутентифицирован
        self.assertEqual(self.client.login(username='sergey1karpov', password='password'), True)

        # Проверяем что произошел редирект со статусом 302(Редирект) на страницу "/"
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/')

        # Проверяем, что пользователь видит главную страницу
        response = self.client.get(reverse('blogger:main_page'))
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        # создали юзера в бд и залогинились
        User.objects.create_user(
            username='sergey1karpov',
            password='password',
            email='sergey1karpov@example.com'
        )

        self.client.post('http://127.0.0.1:8000/login/', {
            'username': 'sergey1karpov',
            'password': 'password'
        })

        response = self.client.get('http://127.0.0.1:8000/logout/')

        # Проверяем что произошел редирект со статусом 302(Редирект) на страницу "/"
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/')

        # Проверяем, что пользователь видит главную страницу
        response = self.client.get(reverse('blogger:main_page'))
        self.assertEqual(response.status_code, 200)

        # Проверили что пользователь не авторизован
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_redirect_if_user_already_authenticated(self):
        paths = [
            '/registration/',
            '/login/'
        ]

        User.objects.create_user(
            username='sergey1karpov',
            password='password',
            email='sergey1karpov@example.com',
        )

        client = Client()
        client.login(username='sergey1karpov', password='password')

        for path in paths:
            self.client.get(f"http://127.0.0.1:8000/{path}/")

            # Проверяем, что пользователь видит главную страницу
            response = self.client.get(reverse('blogger:main_page'))
            self.assertEqual(response.status_code, 200)

            # Проверили что пользователь не авторизован
            self.assertFalse(response.wsgi_request.user.is_authenticated)



