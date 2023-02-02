from django.contrib.auth.backends import ModelBackend

from myapp.models import CustomUser


class CustomBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password) is True:
                return user
        except CustomUser.DoesNotExist:
            pass

    def get_user(self, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None
