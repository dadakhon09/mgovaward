from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from users.models import UserProfile
from users.serializers import UserProfileSerializer, UserFullSerializer, UserSerializer, userFullSerializer


# @permission_classes((IsAdminUserProfile, IsAuthenticated))
class UserCreate(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        first_name = data['first_name']
        last_name = data['last_name']
        user_type = data['user_type']

        user_check = UserProfile.objects.filter(username=username)
        if not user_check:
            new_user = UserProfile.objects.create(username=username, first_name=first_name, last_name=last_name)
            new_user.set_password(raw_password=password)
            token, _ = Token.objects.get_or_create(user=new_user)
            new_user.user_type = user_type
            new_user.save()
            return Response("user is created")
        else:
            return Response("We have already the same username")


@permission_classes((AllowAny,))
class UserLogin(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password!',
                             'status': 'error'})
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials!',
                             'status': 'error'})
        token, _ = Token.objects.get_or_create(user=user)
        profile = UserProfile.objects.get(username=user.username, password=user.password)
        return Response({'token': token.key,
                         'user_id': profile.id,
                         'username': profile.username,
                         'status': 'success',
                         'user_type': profile.get_user_type_display()})


# @permission_classes((IsAuthenticated,))
class UserLogout(APIView):
    def get(self, request):
        if request.user:
            request.user.auth_token.delete()
        else:
            Response("Please login first")
        return Response("Successfully logged out")


class UserListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    # permission_classes = (IsAdminUserProfile, IsAuthenticated)


class UserUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = UserFullSerializer
    queryset = UserProfile.objects.all()
    # permission_classes = (IsAuthenticated, IsAdminUserProfile)

    def update(self, request, *args, **kwargs):
        obj = UserProfile.objects.get(id=kwargs['id'])
        obj.username = self.request.data['username']
        obj.first_name = self.request.data['first_name']
        obj.last_name = self.request.data['last_name']
        obj.set_password(self.request.data.get("password"))
        serializer = self.get_serializer(self.request.data)
        obj.save()
        return Response(serializer.data)


class UserDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = UserFullSerializer
    queryset = UserProfile.objects.all()
    # permission_classes = (IsAdminUserProfile, IsAuthenticated)


class DoctorsListAPIView(ListAPIView):
    serializer_class = userFullSerializer
    queryset = UserProfile.objects.filter(user_type=2)


class PatientsListAPIView(ListAPIView):
    serializer_class = userFullSerializer
    queryset = UserProfile.objects.filter(user_type=1)


class DoctorDetailAPIView(ListAPIView):
    serializer_class = userFullSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.kwargs['doctor_id'])


class PatientDetailAPIView(ListAPIView):
    serializer_class = userFullSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.kwargs['patient_id'])
