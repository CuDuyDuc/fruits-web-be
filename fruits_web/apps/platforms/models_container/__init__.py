import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import models

from fruits_web.apps.platforms.models_container.user import User
from fruits_web.apps.platforms.models_container.product import Product
from fruits_web.apps.platforms.models_container.cart import Cart