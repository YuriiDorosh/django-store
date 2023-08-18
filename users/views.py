
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import User


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Ara Shop - Авторизація'



class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Ви успішно зареєструвалися!'
    title = 'Ara Shop - Реєстрація'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Ara Shop - Особистий кабінет'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))






