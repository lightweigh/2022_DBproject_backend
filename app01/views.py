from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from app01.models import *

from rest_framework import viewsets, status

from app01.myfilter import UsersFilter
from app01.mypage import MyPage
from app01.permissions import IsNotAuthenticated
from app01.serializer import *


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # pagination_class = MyPage
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)  # 指定过滤器的配置类, 配置搜索的项
    # filter_fields = ('username',)  # 过滤字段
    filterset_class = UsersFilter
    # 搜索字段
    search_fields = ('username', 'age')
    # 排序字段
    ordering_fields = ('username', 'id')


class UserView(ViewSet):
    permission_classes = [IsAuthenticated]

    def get_item(self, request):
        user = User.objects.get(id=request.user.id)
        bs = UserSerializer(instance=user)
        return Response(bs.data)

    def edit_item(self, request):
        instance = User.objects.get(id=request.user.id)
        bs = UserUpdateSerializer(instance=instance, data=request.data, partial=True)
        if bs.is_valid():
            bs.save()
            return Response(bs.data, status.HTTP_200_OK)
        else:
            return Response(bs.errors, status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    permission_classes = (IsNotAuthenticated,)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.instance
        Token.objects.get_or_create(user=user)
        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )


class LoginView(APIView):
    permission_classes = [IsNotAuthenticated, ]

    def post(self, request):
        print(request.data)
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username)
        if user is not None:
            user = authenticate(username=username, password=password)
            if user:  # 如果验证通过
                if user.is_active:  # 如果用户状态为激活
                    # print("登录")
                    login(request, user)
            serializer = UserSerializer(user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "登录失败。"}, status.HTTP_401_UNAUTHORIZED)
