from fruits_web.apps.platforms.models_container import User, Product, Cart
from rest_framework import serializers,status
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from rest_framework.response import Response
from fruits_web.apps.platforms.serializers_container.user import *
from fruits_web.apps.platforms.serializers_container.product import *
from fruits_web.apps.platforms.serializers_container.cart import *
