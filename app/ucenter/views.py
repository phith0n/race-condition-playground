from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import F

from . import models, forms

class BaseWithdrawView(LoginRequiredMixin, generic.FormView):
    template_name = 'form.html'
    form_class = forms.WithdrawForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class WithdrawView1(BaseWithdrawView):
    success_url = reverse_lazy('ucenter:withdraw1')

    def form_valid(self, form):
        amount = form.cleaned_data['amount']
        self.request.user.money -= amount
        self.request.user.save()
        models.WithdrawLog.objects.create(user=self.request.user, amount=amount)

        return redirect(self.get_success_url())


class WithdrawView2(BaseWithdrawView):
    success_url = reverse_lazy('ucenter:withdraw2')

    @transaction.atomic
    def form_valid(self, form):
        amount = form.cleaned_data['amount']
        self.request.user.money -= amount
        self.request.user.save()
        models.WithdrawLog.objects.create(user=self.request.user, amount=amount)

        return redirect(self.get_success_url())


class WithdrawView3(BaseWithdrawView):
    success_url = reverse_lazy('ucenter:withdraw3')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.user
        return kwargs

    @transaction.atomic
    def dispatch(self, request, *args, **kwargs):
        self.user = get_object_or_404(models.User.objects.select_for_update().all(), pk=self.request.user.pk)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        amount = form.cleaned_data['amount']
        self.user.money -= amount
        self.user.save()
        models.WithdrawLog.objects.create(user=self.user, amount=amount)

        return redirect(self.get_success_url())


class WithdrawView4(BaseWithdrawView):
    success_url = reverse_lazy('ucenter:withdraw4')

    @transaction.atomic
    def form_valid(self, form):
        amount = form.cleaned_data['amount']
        rows = models.User.objects.filter(pk=self.request.user, money__gte=amount).update(money=F('money')-amount)
        if rows > 0:
            models.WithdrawLog.objects.create(user=self.request.user, amount=amount)

        return redirect(self.get_success_url())
