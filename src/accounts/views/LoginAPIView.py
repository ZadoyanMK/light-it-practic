from ..serializers import LoginSerializer, UserSerializer
from rest_framework import generics, permissions, serializers, status
from django.contrib.auth.signals import user_logged_in, user_logged_out
from rest_framework.response import Response
from knox.models import AuthToken
from youtube_media.models import Featured


class LoginAPIView(generics.GenericAPIView):
    
    serializer_class = LoginSerializer
    permissions_classes = [
        permissions.AllowAny
    ]

    def post(self, request, *a, **kw):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        featured_list = [
            x.link.video_id for x in Featured.objects.filter(user=user)
        ]

        return Response({
            "data": {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": f'{AuthToken.objects.create(user)[1]}',
                'links': featured_list
            }
        })
