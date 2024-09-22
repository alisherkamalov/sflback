from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import CustomAccount
from .serializers import AccountSerializer

class AccountView(APIView):
    def get(self, request):
        accounts = CustomAccount.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request):
        print("Incoming data:", request.data)
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Validation errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
