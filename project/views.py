from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response


def index(request, *args):
    return render(request, 'index.html')


class LoginView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        data = request.data

        user = authenticate(username=data.get('username'), password=data.get('password'))

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=200)
        return Response(status=400)
