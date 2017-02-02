from rest_framework import views
from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from django.shortcuts import redirect


class LoginView(views.APIView):
    def post(self, request):
        user = authenticate(username=self.request.data.pop('login'), password=self.request.data.pop('password'))
        login(request, user)
        return redirect('/')
