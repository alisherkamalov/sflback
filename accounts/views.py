# views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import CustomAccount
from .serializers import AccountSerializer

class AccountView(APIView):
    # GET для получения списка аккаунтов
    def get(self, request):
        accounts = CustomAccount.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    # POST для создания нового аккаунта
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
