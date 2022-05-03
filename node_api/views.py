import json
import requests
from rest_framework.response import Response
from rest_framework.views import APIView



class GetAllStudents(APIView):

    def get(self, request):
        url = "https://tpc-backend-node.herokuapp.com/filter"
        payload = ""
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return Response(response.json())


class GetStudentByRollNo(APIView):

    def post(self, request):
        roll_no = request.data['roll_no']
        url = "https://tpc-backend-node.herokuapp.com/filter/" + roll_no
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return Response(response.json())


class GetStudentsByDept(APIView):

    def post(self, request):
        department = request.data['department']
        url = "https://tpc-backend-node.herokuapp.com/filter/dept/" + department
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return Response(response.json())


class GetStudentProfile(APIView):

    def post(self, request):
        roll_no = request.data['roll_no']
        url = "https://tpc-backend-node.herokuapp.com/filter/profile/" + roll_no
        payload = ""
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return Response(response.json())


class Dashboard(APIView):

    def post(self, request):
        url = "https://tpc-backend-node.herokuapp.com/filter/dashboard"
        payload = json.dumps({
            "fields": {
                "rollno": True,
                "hobbies": True,
                "sem_pointer": True,
                "project": True,
            },
            "queries": {
                "rollno": "19IT1024"
            }
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return Response(response.json())
