from django.contrib import admin
from api.models import Student_Data,Student_Score
# Register your models here.


@admin.register(Student_Data)
class Todo(admin.ModelAdmin):
    list_display = ['id','student_id','full_name','address','email','guardian_name','created_at', 'updated_at']


@admin.register(Student_Score)
class Todo(admin.ModelAdmin):
    list_display = ['studentid','course_name','scores','yearofexam']


