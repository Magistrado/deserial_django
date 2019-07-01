from django.conf.urls import url
from .views import StudentViewSet

app_name = 'api'

urlpatterns = [
    url(
        r'list/$',
        StudentViewSet.as_view({'get': 'list'}),
        name='student_list',
    ),
]
