from .models import Users, PerevalAdded, Coords, PerevalAreas, PerevalImages
from rest_framework.serializers import ModelSerializer


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class CoordsSerializer(ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class PerevalAddedSerializer(ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = '__all__'


class PerevalImagesSerializer(ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = '__all__'


class PerevalAreasSerializer(ModelSerializer):
    class Meta:
        model = PerevalAreas
        fields = '__all__'


class PerevalAddedUpdateSerializer(ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = '__all__'
        read_only_fields = ['user', ]

