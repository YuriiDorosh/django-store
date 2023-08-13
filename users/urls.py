from django.urls import path

from users.views import login, registration, profile

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),  # ../users/login/
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
]
