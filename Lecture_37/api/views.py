from django.shortcuts import render
from .serializers import StudentSeralizer
from rest_framework.generics import ListAPIView
from .models import Student
from rest_framework.filters import SearchFilter
# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class =StudentSeralizer
    filter_backends = [SearchFilter]
    # search_fields = ['city']
    # search_fields = ['city', 'pass_by']
    search_fields = ['^name']