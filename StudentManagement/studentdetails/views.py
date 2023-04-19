from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Staff, Student, Course
from .serializers import UserSerializer, StaffSerializer, StudentSerializer, CourseSerializer
# from rest_framework.authentication import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Student

class AdminView(APIView):
    authentication_classes = [IsAdminUser]

    def get(self, request):
        students = Student.objects.all()
        staffs = Staff.objects.all()
        courses = Course.objects.all()
        student_serializer = StudentSerializer(students, many=True)
        staff_serializer = StaffSerializer(staffs, many=True)
        course_serializer = CourseSerializer(courses, many=True)
        return Response({
            'students': student_serializer.data,
            'staffs': staff_serializer.data,
            'courses': course_serializer.data,
        })

class StaffView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        staff = Staff.objects.get(user=user)
        students = Student.objects.filter(courses__staff=staff)
        student_serializer = StudentSerializer(students, many=True)
        return Response(student_serializer.data)

# class StudentView(APIView):
#     authentication_classes = [IsAuthenticated]

#     def get(self, request):
#         user = request.user
#         student = Student.objects.get(user=user)
#         course = student.course
#         course_serializer = CourseSerializer(course, many=False)
#         student_serializer = StudentSerializer(student)
#         return Response({
#             'course': course_serializer.data,
#             'student': student_serializer.data,
#         })
class StudentView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student = Student.objects.get(user=request.user)
        course_serializer = CourseSerializer(student.course, many=False)
        student_serializer = StudentSerializer(student)
        return Response({
            'course': course_serializer.data,
            'student': student_serializer.data,
        })
