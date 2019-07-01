from rest_framework import viewsets
from quickstart.models import Student
from api.serializers import StudentSerializer
from rest_framework.response import Response
from collections import deque
from rest_framework.renderers import JSONRenderer


import io
from rest_framework.parsers import JSONParser






class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    http_method_names = [u'get']
    queryset = Student.objects.all()

    def list(self, request):
        queryset = Student.objects.all()

        serializer = StudentSerializer(queryset, many=True)
        json = JSONRenderer().render(serializer.data)
        print(json)

        print('Reversing')
        stream = io.BytesIO(json)
        data = JSONParser().parse(stream)

        json_list = StudentSerializer(data=data, many=True)
        data.reverse()
        json_list.is_valid()
        json = JSONRenderer().render(json_list.validated_data)
        print(json)

        return Response(json_list.validated_data)

