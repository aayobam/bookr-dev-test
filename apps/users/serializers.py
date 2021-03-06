from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer, RefreshToken
from .models import CustomUser



class UserSerializer(serializers.ModelSerializer):

    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'phone_no',
        )

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        return user
    
    def detail_url(self, obj):
        return obj.get_absolute_url()


class RegisterUserSerializer(serializers.ModelSerializer):

    detail_url = serializers.SerializerMethodField()
    email = serializers.EmailField()
    password = serializers.CharField(
        max_length=120, 
        min_length=8, 
        write_only=True, 
        help_text="must not be less than 8", 
        style={'input_type':"password"},
        required=True,
    )
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'phone_no', 'email', 'username', 'password')
        extra_kwargrs = {'password': {"write_only": True}}

    def create(self, validated_data):
        password = validated_data["password"]
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.role = "Customer"
        user.save()
        return user

    def update(self, instance, validated_data):
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def detail_url(self, obj):
        return obj.get_absolute_url()


class EmailTokenObtainSerializer(TokenObtainSerializer):
    username_field = CustomUser.EMAIL_FIELD


class CustomTokenObtainPairSerializer(EmailTokenObtainSerializer):
    """
    Generates refresh token for users and returns new access token
    """
    @classmethod
    def get_token(cls, user):
        token = RefreshToken.for_user(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        user = UserSerializer(self.user)
        data["user"] = user.data
        return data