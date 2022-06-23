from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework.views import APIView
from tpc_api.models import Student, PlacementDetails
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
            emptyValueRows = []

            for row in range(0, len(studentData)):
                if studentData.iloc[row]['roll_no'] != '' and studentData.iloc[row]['birth_date'] != '':
                    roll_no = studentData.iloc[row]['roll_no']
                    birth_date = datetime.strptime(studentData.iloc[row]['birth_date'], '%m/%d/%Y %H:%M:%S').strftime('%d%m%Y')
                    try:
                        student = Student.objects.get(roll_no=roll_no)
                    except:
                        student = Student.objects.create(roll_no=roll_no, rait_email=roll_no, password=make_password(birth_date))
                        student.groups.add(studentGroup)
                else:
                    emptyValueRows.append(row+2)
            return Response({'emptyValueRows': emptyValueRows})
        else:
            return Response({'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}, status = 403)


class AddPlacedStudents(APIView):
    
    def post(self, request):
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)

        if userRecord.groups.filter(name='Superuser'):
            excelFile = request.FILES['excelFile']
            df = pd.read_excel(excelFile, engine='openpyxl').fillna('')
            studentData = df[['roll_no', 'company', 'package']]
            moreThanThreeCompaniesRows = []         # List to store student rows with more than 3 companies
            studentNotExistsRows = []               # List to store student rows with no record in Student table
            emptyValueRows = []                     # List to store student rows with empty values in columns

            for row in range(0, len(studentData)):
                if studentData.iloc[row]['roll_no'] != '' and studentData.iloc[row]['company'] != '' and studentData.iloc[row]['package'] != '':
                    roll_no = studentData.iloc[row]['roll_no']
                    company_name = studentData.iloc[row]['company']
                    package = studentData.iloc[row]['package']

                    try:
                        student = Student.objects.get(roll_no=roll_no)
                        try:
                            studentPlacementDetails = PlacementDetails.objects.get(student=student)
                            if studentPlacementDetails.placed_org_one == None or studentPlacementDetails.placed_org_two == '':
                                studentPlacementDetails.placed_org_one = company_name
                                studentPlacementDetails.package_one = package
                                studentPlacementDetails.save(update_fields=['placed_org_one', 'package_one'])
                            elif studentPlacementDetails.placed_org_two == None or studentPlacementDetails.placed_org_two == '':
                                studentPlacementDetails.placed_org_two = company_name
                                studentPlacementDetails.package_two = package
                                studentPlacementDetails.save(update_fields=['placed_org_two', 'package_two'])
                            elif studentPlacementDetails.placed_org_three == None or studentPlacementDetails.placed_org_three == '':
                                studentPlacementDetails.placed_org_three = company_name
                                studentPlacementDetails.package_three = package
                                studentPlacementDetails.save(update_fields=['placed_org_three', 'package_three'])
                            else:
                                moreThanThreeCompaniesRows.append(row+2)
                        except:
                            PlacementDetails.objects.create(student=student, placed_org_one=company_name, package_one=package)
                    except:
                        studentNotExistsRows.append(row+2)
                else:
                    emptyValueRows.append(row+2)
            return Response({'emptyValueRows': emptyValueRows, 
                            'studentNotExistsRows': studentNotExistsRows, 
                            'moreThanThreeCompaniesRows': moreThanThreeCompaniesRows
                        })
        else:
            return Response({'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}, status = 403)