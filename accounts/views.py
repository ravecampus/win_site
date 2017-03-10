from django.shortcuts import render

from django.views.generic import TemplateView, View
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest

class LoginView(TemplateView):

    def get(self, *args, **kwargs):
        return render(self.request, 'accounts/login.html', {})


class DashboardView(TemplateView):

    def get(self, *args, **kwargs):
        return render(self.request, 'accounts/dashboard.html', {})