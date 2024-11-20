from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from users.serializers import (CreateUserSerializer, LoginUserSerializer,
                               RecoverPasswordSerializer,
                               RecoveryCodeSerializer)


def response(serializer: Serializer) -> Response:
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


class CreateUserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = CreateUserSerializer(data=request.data)
        return response(serializer)


class LoginUserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.get_token(serializer.validated_data)
            return Response({"token": token})
        return Response(serializer.errors, status=400)


class RecoveryCodeView(APIView):
    def post(self, request):
        serializer = RecoveryCodeSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.get_code(serializer.validated_data)
            return Response({"code": code}, status=201)
        return Response(serializer.errors, status=400)

class RecoverPasswordView(APIView):
    def patch(self, request: Request) -> Response:
        serializer = RecoverPasswordSerializer(data=request.data)
        return response(serializer)