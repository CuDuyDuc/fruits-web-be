from fruits_web.apps.platforms.serializers_container import LoginSerializer, RegisterSerializer, UserSerializer, AddProductSerializer, UpdateProductSerializer, AddCartSerializer, UpdateCartSerializer, CreateShopSerializer, UpdateUserSerializer,ListCartSerializer, ListProductSerializer, NotificationSerializer
from fruits_web.apps.platforms.models_container import User, Product, Cart
from rest_framework import generics, status, parsers, renderers
from fruits_web.apps.platforms.views_container.user import *
from fruits_web.apps.platforms.views_container.product import *
from fruits_web.apps.platforms.views_container.cart import *
from fruits_web.apps.platforms.views_container.notification import *
from rest_framework.response import Response
