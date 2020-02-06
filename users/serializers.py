from rest_framework.serializers import ModelSerializer

from users.models import UserProfile


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username')


class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'user_type')


class userFullSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'first_name', 'last_name')


class UserFullSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user_type', 'first_name', 'last_name', 'username', 'email')
