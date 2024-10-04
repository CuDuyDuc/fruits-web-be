from django.db import OperationalError
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from fruits_web.apps.platforms.models_container.user import User
from django.contrib.auth.hashers import make_password

@receiver(post_migrate)
def create_admin_user_if_not_exists(sender, **kwargs):
    try:
        if sender.name == 'fruits_web.apps.platforms':  
            if not User.objects.filter(email='admin123@gmail.com').exists():
                user = User(
                    email='admin123@gmail.com',
                    username='admin123',
                    full_name='Admin User',
                    password=make_password('admin123'),
                    is_active=True,
                    role='admin'
                )
                user.save()
                print("Admin user created successfully.")
    except OperationalError:
        print("Database is not ready yet.")
    except Exception as e:
        print(f"An error occurred: {e}")