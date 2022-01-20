from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Overloading default User class as recommended in Django
# Further changes, if any, can be easily done.
class User(AbstractUser):
    class Meta:
        permissions = (('can_use_api', 'User can use API'),)

    # Further authentication can be done by creating permissions that
    # only allow certain users to access API only if the belong to a
    # particular group.
    # Just an idea, skipped implementation for now.
    @property
    def is_api_user(self):
        if self.groups.filter(name='api_users').exists():
            return True
        return False


# Post save signal to automatically create token for each user
# as soon as they are created.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
