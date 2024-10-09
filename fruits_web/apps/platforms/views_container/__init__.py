from fruits_web.apps.platforms.serializers_container import LoginSerializer, RegisterSerializer, UserSerializer, AddProductSerializer, UpdateProductSerializer, AddCartSerializer, UpdateCartSerializer, CreateShopSerializer, UpdateUserSerializer,ListCartSerializer, ListProductSerializer
from fruits_web.apps.platforms.models_container import User, Product, Cart
from rest_framework import generics, status
from fruits_web.apps.platforms.views_container.user import *
from fruits_web.apps.platforms.views_container.product import *
from fruits_web.apps.platforms.views_container.cart import *
from rest_framework.response import Response
