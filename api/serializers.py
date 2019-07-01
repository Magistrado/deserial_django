from rest_framework import serializers
from quickstart.models import Student


class StudentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    class Meta:
        model = Student
        fields = ('id', 'name', 'phone','login_datetime')



