from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from tpc_api.models import *


class StudentLogin(APIView):
    permission_classes = []

    def post(self, request):
        rait_email = request.data['rait_email']
        password = request.data['password']

        try:
            student = Student.objects.get(rait_email=rait_email)
            if check_password(password, student.password):
                roleList = []
                for role in student.groups.all():
                    roleList.append(role.name)
                refresh = RefreshToken.for_user(student)
                access = str(refresh.access_token)
                response = Response(
                    {
                        'status': 'User Logged In',
                        'role': roleList,
                        'refresh': str(refresh),
                        'access': access
                    }
                )
                response.set_cookie(key='jwt', value=access, httponly=True)
                return response
            else:
                raise(Exception('Password is incorrect'))
        except Exception as e:
            return Response(
                {
                    'status': 'Incorrect Credentials', 
                    'error_msg': str(e)
                }, 
                status=500
            )


class DummyStudentSignUp(APIView):
    permission_classes = []

    def post(self, request):
        roll_no = request.data['roll_no']
        rait_email = request.data['rait_email']
        password = request.data['password']
        role = request.data['role']
        
        try:
            student = Student.objects.get(roll_no=roll_no)
            return Response(
                {
                    'status': role + ' Exists'
                }
            )
        except:
            student = Student.objects.create(roll_no=roll_no, rait_email=rait_email, password=make_password(password))
            if role == 'Student':
                studentGroup = Group.objects.get(name ='Student')
                student.groups.add(studentGroup)
            elif role == 'Superuser':
                studentGroup = Group.objects.get(name ='Superuser')
                student.groups.add(studentGroup)
            return Response(
                {
                    'status': role + ' Added'
                }
            )