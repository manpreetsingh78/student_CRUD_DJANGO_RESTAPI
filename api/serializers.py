from rest_framework import serializers
from api.models import Student_Data
from .models import Student_Score

class Student_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Data
        fields = ['id','student_id','full_name','address','email','guardian_name','created_at', 'updated_at']
        read_only_fields = ['created_at','updated_at']
    
    # def create(self, validated_data):
    #     return super().create(validated_data)

class Student_Score_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Score
        fields = ['studentid','course_name','scores','yearofexam','created_at', 'updated_at']
        read_only_fields = ['created_at','updated_at']
    # def create(self, validated_data):
    #     return super().create(validated_data)

        


