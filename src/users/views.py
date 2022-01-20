from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response


class CustomAuthToken(ObtainAuthToken):
    """
    AOverloaded ObtainAuthToken API so additional
    information can be served with token value.
    Could extend this further to override
    TokenAuthentication and implement more secure
    ExpiringTokenAuthentication.

    param request: request object having request params
    request param username : takes username as input
    request param password : takes password parameter as input
    return: HTTP Response
    rtype: JSON
    """

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                'token': token.key,
                'token_type': 'Token',
                'user_id': user.pk,
            }
        )
