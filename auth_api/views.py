from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from tpc_api.models import *

class StudentLogin(APIView):

    def post(self, request):
        rait_email = request.data['rait_email']
        password = request.data['password']

        try:
            student = Student.objects.get(rait_email=rait_email)
            if check_password(password, student.password):
                refresh = RefreshToken.for_user(student)
                access = str(refresh.access_token)
                response = Response(
                    {
                        'status': 'User Logged In', 
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
