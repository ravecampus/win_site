from .models import Account

from .serializers import AccountSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

class AccountAPI(viewsets.ViewSet):
    serializer_class = AccountSerializer

    def list(self, *args, **kwargs):
        queryset = Account.objects.all()
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, *args, **kwargs):
        serializer = AccountSerializer(data = self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

class AccountAPI2(viewsets.ViewSet):

    serializer_class = AccountSerializer

    def get(self, *args, **kwargs):
        user = get_object_or_404(Account, pk=kwargs.get('user_id'))
        serializer = AccountSerializer(user)
        return Response(serializer.data)

    def update(self, *args, **kwargs):
        user = get_object_or_404(Account, pk=kwargs.get('user_id'))
        serializer = AccountSerializer(user, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, *args, **kwargs):
        poke = get_object_or_404(Account, pk=kwargs.get('user_id'))
        poke.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
