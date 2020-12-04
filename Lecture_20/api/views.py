from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,DjangoObjectPermissions

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]      #Register User
    # permission_classes = [AllowAny]             # Any Person
    # permission_classes = [IsAdminUser]          # Only is_Staff is True
    # permission_classes = [IsAuthenticatedOrReadOnly]          
    # permission_classes = [DjangoModelPermissions]          
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]          
    # permission_classes = [DjangoObjectPermissions]          
    