from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

# Model object ( single student data)
def student_detail(request,pk):
    stu = Student.objects.get(id = pk) # complex data
    serializer = StudentSerializer(stu) # converted into python native data
    json_data = JSONRenderer().render(serializer.data) # convert the python native data into json format
    return HttpResponse(json_data,content_type='application/json')

def student_detail_all(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

