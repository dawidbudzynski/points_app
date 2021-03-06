from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.views import View
from django.views.generic import ListView

from user.forms import EditBalanceForm
from user.models import User


class UserListView(ListView):
    """Lists all users (except superuser)"""

    def get_queryset(self):
        queryset = User.objects.filter(is_superuser=False).order_by('last_name', 'first_name')
        return queryset


class UserEditBalanceView(View):
    """Displays form which allows to change user balance"""

    def get(self, request):
        return render(
            request,
            template_name='user/edit_balance.html',
            context={'form': EditBalanceForm()}
        )

    def post(self, request):
        form = EditBalanceForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            operation = form.cleaned_data['operation']
            amount = form.cleaned_data['amount']
            user_object = User.objects.filter(email=user.email).first()
            if user_object:
                previous_balance = user_object.balance
                if operation == 'add':
                    user_object.balance = previous_balance + amount
                elif operation == 'subtract':
                    user_object.balance = previous_balance - amount
                user_object.save()

                messages.add_message(
                    request, messages.SUCCESS, _(f"Balance for user {user.email} has been changed successfully"))
                return HttpResponseRedirect(reverse('user:list'))

            messages.add_message(request, messages.WARNING, _(f"User {user.email} doesn't exist"))
            return HttpResponseRedirect(reverse('user:list'))

        messages.add_message(request, messages.ERROR, form.errors)
        return HttpResponseRedirect(reverse('user:edit-balance'))
