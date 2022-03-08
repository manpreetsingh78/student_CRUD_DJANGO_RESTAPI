from .models import Student_Data,Student_Score
from .serializers import Student_Data_Serializer,Student_Score_Serializer
from rest_framework import viewsets
#---------------------------Using Model View Set---------------------------

class StudentDataViewSet(viewsets.ModelViewSet):
    queryset = Student_Data.objects.all()
    serializer_class = Student_Data_Serializer
    def get_queryset(self):
        return Student_Data.objects.all()


class StudentScoreViewSet(viewsets.ModelViewSet):
    queryset = Student_Score.objects.all()
    serializer_class = Student_Score_Serializer
    def get_queryset(self):
        return Student_Score.objects.all()













