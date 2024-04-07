from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings
from django.utils.timezone import now


class CreateUserView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            # Assuming you have access and refresh token lifetimes set in your settings
            access_token_lifetime = api_settings.ACCESS_TOKEN_LIFETIME
            refresh_token_lifetime = api_settings.REFRESH_TOKEN_LIFETIME
            
            response.data["access_token_expires"] = int((now() + access_token_lifetime).timestamp())
            # response.data["refresh_token_expires"] = int((now() + refresh_token_lifetime).timestamp())
        return response


# class CustomTokenRefreshView(TokenRefreshView):
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         if response.status_code == 200:
#             # Decode the response data and add the expiration time
#             access_token = response.data["access"]
#             refresh_token = request.data.get("refresh")

#             # Decode the new access token to get its expiration time
#             access_token_obj = RefreshToken(access_token)
#             refresh_token_obj = RefreshToken(refresh_token)

#             # Update the response to include the expiration times
#             response.data["access_token_expires"] = int(access_token_obj.access_token.lifetime.total_seconds())
#             response.data["refresh_token_expires"] = int(refresh_token_obj.lifetime.total_seconds())
#         return response
