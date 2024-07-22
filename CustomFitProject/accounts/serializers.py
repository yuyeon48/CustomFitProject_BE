from rest_framework import serializers
from .models import CustomUser, Keyword

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ['keyword_id', 'keyword_name']

class CustomUserSerializer(serializers.ModelSerializer):
    keyword_id = serializers.PrimaryKeyRelatedField(queryset=Keyword.objects.all(), source='keyword', write_only=True)
    keyword = KeywordSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'keyword', 'keyword_id']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
