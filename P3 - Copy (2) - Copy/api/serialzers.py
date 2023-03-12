from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','roll','city']
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
#     def update(self,instance,validated_data): # instance is the new object to be updated and validated_data is the new information which is provided by the client
#         instance.name = validated_data.get('name',instance.name)
#         instance.roll = validated_data.get('roll',instance.roll)
#         instance.city = validated_data.get('city',instance.city)
#         instance.save()
#         return instance
    
#     # Field level validation
#     def validate_roll(self,value): # this is to validate a field in serializers.py
#         if value>=200:
#             raise serializers.ValidationError('seat full')
#         return value
#     # object level validation -> validate is inbuilt function
#     def validate(self, data):
#         nm = data.get('name')
#         ct = data.get('city')
#         if(nm.lower() == "rohit" and ct.lower()!="ranchi"):
#             raise serializers.ValidationError('city must be Ranchi!')
#         return data
