from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistrationForm

from django.shortcuts import redirect, render
from django.urls import reverse

from django.contrib import messages
from django.views.generic.base import TemplateView


def register_page(request):

    if request.user.is_authenticated:
        messages.warning(request, "You've aleready been authenticated")
        
        return redirect(reverse('film_list'))

    form = RegistrationForm()

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for ${user}')

            return redirect(reverse('login'))

    context = {'form': form}
    return render(request, 'vtb_users/register.html', context)


class ProfileView(LoginRequiredMixin, TemplateView):
    permission_denied_message = "NO! You are not authenticated for this action!"
    login_url = 'login/'
    raise_exception = True
    template_name = 'vtb_users/profile.html'
