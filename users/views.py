from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import RegistrationSerializer, UserSelfSerializer, UserPatchSerializer
from utils.serializers import SuccessSerializer


class UserAPIView(APIView):

    @swagger_auto_schema(responses={200: UserSelfSerializer()})
    def get(self, request, *args, **kwargs):
        return Response(UserSelfSerializer(request.user).data)

    @swagger_auto_schema(request_body=UserPatchSerializer(), responses={200: SuccessSerializer()})
    def patch(self, request, *args, **kwargs):
        serializer = UserPatchSerializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True})


class RegistrationAPIView(APIView):

    @swagger_auto_schema(request_body=RegistrationSerializer(), responses={201: SuccessSerializer()})
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self._create_user_by_phone_number(**serializer.data)
        return Response({'success': True}, 201)

    @staticmethod
    def _create_user_by_phone_number(phone):
        user = User.objects.create(username=phone)
        user.set_password('123')
        user.save()
