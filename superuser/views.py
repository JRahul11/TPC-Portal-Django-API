from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework.views import APIView
from tpc_api.models import *
import pandas as pd
from datetime import datetime



class AddBatchViaExcel(APIView):
    
    def post(self, request):
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)
        
        if userRecord.groups.filter(name='Superuser'):
            excelFile = request.FILES['excelFile']
            df = pd.read_excel(excelFile, engine='openpyxl').fillna('')
            studentData = df[['roll_no', 'birth_date']]
            studentGroup = Group.objects.get(name ='Student')

            for row in range(0, len(studentData)):
                if studentData.iloc[row]['roll_no'] != '' and studentData.iloc[row]['birth_date'] != '':
                    roll_no = studentData.iloc[row]['roll_no']
                    birth_date = datetime.strptime(studentData.iloc[row]['birth_date'], '%m/%d/%Y %H:%M:%S').strftime('%d%m%Y')
                    try:
                        student = Student.objects.get(roll_no=roll_no)
                    except:
                        student = Student.objects.create(roll_no=roll_no, rait_email=roll_no, password=make_password(birth_date))
                        student.groups.add(studentGroup)

            return Response({'Status': 'Success'})
        else:
            return Response({'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}, status = 403)