from rest_framework.response import Response
from rest_framework.views import APIView
from tpc_api.models import Student
import requests
import json



class GetAllStudents(APIView):

    def get(self, request):
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)

        if userRecord.groups.filter(name='Superuser'):
            url = "https://tpc-backend-node.herokuapp.com/filter"
            payload = ""
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            return Response(response.json())
        else:
            return Response(
                {'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}, 
                status = 403
            )


class GetStudentByRollNo(APIView):

    def post(self, request):
        user_roll_no = request.data['roll_no']
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)

        if (user_roll_no == jwt_roll_no and userRecord.groups.filter(name='Student')) or (userRecord.groups.filter(name='Superuser')):
            url = "https://tpc-backend-node.herokuapp.com/filter/" + user_roll_no
            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            return Response(response.json())
        else:
            return Response(
                {'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}, 
                status = 403
            )


class GetStudentsByDept(APIView):

    def post(self, request):
        department = request.data['department']
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)

        if userRecord.groups.filter(name='Superuser'):
            url = "https://tpc-backend-node.herokuapp.com/filter/dept/" + department
            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            return Response(response.json())
        else:
            return Response(
                {'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}, 
                status = 403
            )


class GetStudentProfile(APIView):

    def post(self, request):
        user_roll_no = request.data['roll_no']
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)

        if (user_roll_no == jwt_roll_no and userRecord.groups.filter(name='Student')) or (userRecord.groups.filter(name='Superuser')):
            url = "https://tpc-backend-node.herokuapp.com/filter/profile/" + user_roll_no
            payload = ""
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            return Response(response.json())
        else:
            return Response(
                {'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}, 
                status = 403
            )


class Dashboard(APIView):

    def post(self, request):
        roll_no = request.data['roll_no']
        sem_pointer = request.data['sem_pointer'].lower()
        project = request.data['project'].lower()
        hobbies = request.data['hobbies'].lower()
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)

        if userRecord.groups.filter(name='Superuser'):
            fields = {'rollno': True}
            if hobbies == 'true':
                fields['hobbies'] = hobbies.capitalize()
            if sem_pointer == 'true':
                fields['sem_pointer'] = sem_pointer.capitalize()
            if project == 'true':
                fields['project'] = project.capitalize()

            url = "https://tpc-backend-node.herokuapp.com/filter/dashboard"
            payload = json.dumps({
                "fields": fields,
                "queries": {
                    "rollno": roll_no
                }
            })
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            return Response(response.json())
        else:
            return Response(
                {'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}, 
                status = 403
            )
