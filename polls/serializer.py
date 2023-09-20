from rest_framework.serializers import ModelSerializer

from .models import AuthorModel


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('__all__')
