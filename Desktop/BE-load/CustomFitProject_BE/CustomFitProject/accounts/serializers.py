from django.contrib.auth.models import User 
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['gender', 'age', 'disease', 'height', 'weight']


# 회원 가입
class UserSerializer(ModelSerializer):
    email = serializers.EmailField(required=True)
    nickname = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True, required=True)
    profile = UserProfileSerializer()

    def create(self, validated_data):
        if validated_data['password'] != validated_data['password_confirm']:  # 비밀번호와 비밀번호 확인 확인 로직
            raise serializers.ValidationError({'password': '비밀번호와 비밀번호 확인이 일치하지 않습니다. 다시 입력해주세요!'})

        profile_data = validated_data.pop('profile', {})
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )

        user.first_name = validated_data.pop('nickname')
        user.save()

        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})

        # Update user fields
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('nickname', instance.first_name)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()

        # Update or create profile
        profile, created = UserProfile.objects.get_or_create(user=instance)
        for attr, value in profile_data.items():
            setattr(profile, attr, value)
        profile.save()

        return instance
    
    class Meta:
        model = User
        fields = ['id','username', 'password', 'password_confirm','nickname', 'email', 'profile']





# 회원 정보 수정
class UserUpdateSerializer(ModelSerializer) :
    current_password = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False)
    password_confirm = serializers.CharField(write_only=True, required=False)
    name = serializers.CharField(write_only=True)
    profile = UserProfileSerializer()

    def update(self, instance, validated_data):
        current_password = validated_data.pop('current_password', None)
        password = validated_data.pop('password', None)
        password_confirm = validated_data.pop('password_confirm', None)

        # 본인이 맞는지 확인하기 위한 비밀번호 확인 로직
        if current_password and not instance.check_password(current_password):
            raise serializers.ValidationError({'current_password': '현재 비밀번호가 일치하지 않습니다.'})

        # 비밀번호를 정확히 입력했는지 확인하기 위한 로직
        if password and password_confirm and password != password_confirm:
            raise serializers.ValidationError({'password': '비밀번호와 비밀번호 확인이 일치하지 않습니다. 다시 입력해주세요!'})

        if password:
            instance.set_password(password)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
   

    class Meta:
        model = User
        fields = ['id','current_password','nickname','username', 'password', 'password_confirm', 'email', 'profile']