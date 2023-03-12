from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework import viewsets

# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# for read only actions
class StudentReadOnlyModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# class StudentViewset(viewsets.ViewSet):
#     def list(self,request):
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu,many=True)
#         return Response(serializer.data)
#     def retrieve(self,requst,pk=None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.all()
#             serializer = StudentSerializer(stu,many=True)
#             return Response(serializer.data)
#     def create(self,request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def update(self,request,pk):
#         id = pk
#         stu = Student.objects.get(id=pk)
#         serializer = StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'complete data updated'})
#         return Response(serializer.errors)
#     def partial_update(self,request,pk):
#         id = pk
#         stu = Student.objects.get(id=pk)
#         serializer = StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'partial data updated'})
#         return Response(serializer.errors)
#     def destroy(self,request,pk):
#         id = pk
#         stu = Student.objects.get(id=pk)
#         stu.delete()
#         return Response({'msg':'data deleted'})

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRetrieve(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentUpdate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentDestroy(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRetrieveUpdate(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRetrieveDestroy(RetrieveDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentListCreate(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRetrieveDestor

# list and create are in one group
# class LCStudentListAPI(GenericAPIView,CreateModelMixin,ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self,request,*args,**kwargs):
#         return self.list(self,request,*args,**kwargs)
#     def post(self,request,*args,**kwargs):
#         return self.create(self,request,*args,**kwargs)

# class RUDStudentAPI(GenericAPIView,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(self,request,*args,**kwargs)
#     def put(self,request,*args,**kwargs):
#             return self.update(self,request,*args,**kwargs)
#     def delete(self,request,*args,**kwargs):
#             return self.destroy(self,request,*args,**kwargs)

# class StudentList(GenericAPIView,ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self,request,*args,**kwargs):
#         return self.list(self,request,*args,**kwargs)

# class StudentCreate(GenericAPIView,CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def post(self,request,*args,**kwargs):
#         return self.create(self,request,*args,**kwargs)

# class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(self,request,*args,**kwargs)
    
# class StudentUpdate(GenericAPIView,UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def put(self,request,*args,**kwargs):
#         return self.update(self,request,*args,**kwargs)
    
# class StudentDestroy(GenericAPIView,DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(self,request,*args,**kwargs)

# class StudentAPI(APIView):
#     def get(self,request,format=None,pk=None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu,many=True)
#         return Response(serializer.data)
#     def post(self,request,format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
#     def put(self,request,format=None,pk=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'complete data updated'})
#         return Response(serializer.errors)
#     def patch(self,request,format=None,pk=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'partial data updated'})
#         return Response(serializer.errors)

# @api_view(['GET','POST','PUT','PATCH','DELETE',])
# def studentapi(request,pk=None):
#     if request.method == "GET":
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu,many=True)
#         return Response(serializer.data)
#     if request.method == "POST":
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
#     if request.method == "PUT":
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'complete data updated'})
#         return Response(serializer.errors)
#     if request.method == "DELETE":
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'data deleted'})
#     if request.method == "PATCH":
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'partial data updated'})
#         return Response(serializer.errors)

