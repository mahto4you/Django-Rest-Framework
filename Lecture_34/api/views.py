from django.shortcuts import render
from .serializers import StudentSeralizer
from rest_framework.generics import ListAPIView
from .models import Student
# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class =StudentSeralizer
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(pass_by=user)
