from django.shortcuts import render
from django.views import View


class ProfileView(View):
    def get(self, request, *orgs, **kwargs):
        return render(request,  'accounts/profile.html')
