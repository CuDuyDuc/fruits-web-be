from fruits_web.apps.platforms.models_container import UserManager, make_password, uuid, AbstractBaseUser, PermissionsMixin, models, RefreshToken


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')
        extra_fields.setdefault('role', 'super-admin')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    password = models.CharField(max_length=128, blank=True)
    username = models.CharField(max_length=128, null=False, blank=False)
    full_name = models.CharField(max_length=128, null=True, blank=False)
    is_active = models.BooleanField(default=True, blank=True)
    is_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    role = models.CharField(max_length=30, null=False, blank=False, default='user')
    objects = CustomUserManager()
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Thêm related_name để tránh xung đột
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Thêm related_name để tránh xung đột
        blank=True
    )
    def __str__(self) -> str:
        return self.email
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }