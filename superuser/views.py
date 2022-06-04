from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.views import APIView
from tpc_api.models import *
import pandas as pd
from datetime import datetime



class AddBatchViaExcel(APIView):
    
    def post(self, request):
        excelFile = request.FILES['excelFile']
        df = pd.read_excel(excelFile, engine='openpyxl').fillna('')
        studentData = df[['roll_no', 'birth_date']]

        for row in range(0, len(studentData)):
            if studentData.iloc[row]['roll_no'] != '' and studentData.iloc[row]['birth_date'] != '':
                roll_no = studentData.iloc[row]['roll_no']
                birth_date = datetime.strptime(studentData.iloc[row]['birth_date'], '%m/%d/%Y %H:%M:%S').strftime('%d%m%Y')
                try:
                    student = Student.objects.get(roll_no=roll_no)
                except:
                    Student.objects.create(roll_no=roll_no, rait_email=roll_no, password=make_password(birth_date))

        return Response({'Status': 'Success'})
