from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from app01.activities.serializer import ActivitySerializer, ActivitySlideSerializer
from app01.models import Activity, ActivitySlide

from rest_framework import viewsets, status

from app01.mypage import MyPage
from app01.permissions import IsNotAuthenticated


class ActivityModelViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    # get_all_items
    # def list(self, request, *args, **kwargs):

    # add_item
    # def create(self, request, *args, **kwargs):

    # get_one_item
    # def retrieve(self, request, *args, **kwargs):

    # edit_item
    # def update(self, request, *args, **kwargs):

    # delete
    # def destroy(self, request, *args, **kwargs):


class ActivitySlideViewSet(viewsets.ModelViewSet):
    queryset = ActivitySlide.objects.all().order_by('sort')
    serializer_class = ActivitySlideSerializer
