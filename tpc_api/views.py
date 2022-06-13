from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *


class GetData:
    def getData(self, request, field, Decimal=False, Integer=False, File=False):
        try:
            if Decimal:
                return float(request.data[field])
            elif Integer:
                return int(request.data[field])
            elif File:
                return request.FILES[field]
            else:
                return request.data[field]
        except:
            return None


class Welcome(APIView):
    permission_classes = []

    def get(self, request):
        return Response("Welcome to TPC Django REST Backend")


class AddStudent(APIView):

    def post(self, request):
        user_roll_no = request.data['roll_no'].strip()
        first_name = request.data['first_name']
        middle_name = request.data['middle_name']
        last_name = request.data['last_name']
        email = request.data['email']
        phone_number = request.data['phone_number']
        gender = request.data['gender']
        github = GetData.getData(self, request, 'github')
        linkedin = GetData.getData(self, request, 'linkedin')
        no_of_offers = GetData.getData(self, request, 'no_of_offers', Integer=True)
        password = make_password(request.data['password'])
        photo = GetData.getData(self, request, 'photo', File=True)
        department = request.data['department']
        batch = int(request.data['batch'])
        rait_email = request.data['rait_email']
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)
        status = 200
        try:
            if (user_roll_no == jwt_roll_no and userRecord.groups.filter(name='Student')) or (userRecord.groups.filter(name='Superuser')):
                student = Student.objects.get(roll_no=user_roll_no)
                student.first_name = first_name
                student.middle_name = middle_name
                student.last_name = last_name
                student.email = email
                student.phone_number = phone_number
                student.gender = gender
                student.github = github
                student.linkedin = linkedin
                student.no_of_offers = no_of_offers
                student.password = password
                student.photo = photo
                student.department = department
                student.batch = batch
                student.rait_email = rait_email
                student.save(update_fields=['first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'gender', 'github', 'linkedin', 'no_of_offers', 'password', 'photo', 'department', 'batch', 'rait_email'])
                context = {'status': 'Student Record Updated'}
            else:
                context = {'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}
                status = 403
        except:
            Student.objects.create(roll_no=user_roll_no, first_name=first_name, middle_name=middle_name, last_name=last_name, email=email, phone_number=phone_number, gender=gender, github=github, linkedin=linkedin, no_of_offers=no_of_offers, password=password, photo=photo, department=department, batch=batch, rait_email=rait_email)
            context = {'status': 'Student Record Added'}
        finally:
            return Response(context, status)


class AddAcademicInfo(APIView):

    def post(self, request):
        user_roll_no = request.data['roll_no'].strip()
        # SSC Data
        tenth_percent = request.data['tenth_percent']
        tenth_completion_date = GetData.getData(self, request, 'tenth_completion_date')
        tenth_obtained_marks = GetData.getData(self, request, 'tenth_obtained_marks', Integer=True)
        tenth_total_marks = GetData.getData(self, request, 'tenth_total_marks', Integer=True)
        # HSC Data
        twelveth_percent = GetData.getData(self, request, 'twelveth_percent', Decimal=True)
        twelveth_completion_date = GetData.getData(self, request, 'twelveth_completion_date')
        twelveth_obtained_marks = GetData.getData(self, request, 'twelveth_obtained_marks', Integer=True)
        twelveth_total_marks = GetData.getData(self, request, 'twelveth_total_marks', Integer=True)
        # Diploma
        diploma_percent = GetData.getData(self, request, 'diploma_percent', Decimal=True)
        diploma_completion_date = GetData.getData(self, request, 'diploma_completion_date')
        diploma_obtained_marks = GetData.getData(self, request, 'diploma_obtained_marks', Integer=True)
        diploma_total_marks = GetData.getData(self, request, 'diploma_total_marks', Integer=True)
        # Degree
        sem1_pointer = float(request.data['sem1_pointer'])
        sem1_completion_date = GetData.getData(self, request, 'sem1_completion_date')
        sem1_obtained_marks = GetData.getData(self, request, 'sem1_obtained_marks', Integer=True)
        sem1_total_marks = GetData.getData(self, request, 'sem1_total_marks', Integer=True)
        sem2_pointer = float(request.data['sem2_pointer'])
        sem2_completion_date = GetData.getData(self, request, 'sem2_completion_date')
        sem2_obtained_marks = GetData.getData(self, request, 'sem2_obtained_marks', Integer=True)
        sem2_total_marks = GetData.getData(self, request, 'sem2_total_marks', Integer=True)
        sem3_pointer = float(request.data['sem3_pointer'])
        sem3_completion_date = GetData.getData(self, request, 'sem3_completion_date')
        sem3_obtained_marks = GetData.getData(self, request, 'sem3_obtained_marks', Integer=True)
        sem3_total_marks = GetData.getData(self, request, 'sem3_total_marks', Integer=True)
        sem4_pointer = float(request.data['sem4_pointer'])
        sem4_completion_date = GetData.getData(self, request, 'sem4_completion_date')
        sem4_obtained_marks = GetData.getData(self, request, 'sem4_obtained_marks', Integer=True)
        sem4_total_marks = GetData.getData(self, request, 'sem4_total_marks', Integer=True)
        sem5_pointer = GetData.getData(self, request, 'sem5_pointer', Decimal=True)
        sem5_completion_date = GetData.getData(self, request, 'sem5_completion_date')
        sem5_obtained_marks = GetData.getData(self, request, 'sem5_obtained_marks', Integer=True)
        sem5_total_marks = GetData.getData(self, request, 'sem5_total_marks', Integer=True)
        sem6_pointer = GetData.getData(self, request, 'sem6_pointer', Decimal=True)
        sem6_completion_date = GetData.getData(self, request, 'sem6_completion_date')
        sem6_obtained_marks = GetData.getData(self, request, 'sem6_obtained_marks', Integer=True)
        sem6_total_marks = GetData.getData(self, request, 'sem6_total_marks', Integer=True)
        sem7_pointer = GetData.getData(self, request, 'sem7_pointer', Decimal=True)
        sem7_completion_date = GetData.getData(self, request, 'sem7_completion_date')
        sem7_obtained_marks = GetData.getData(self, request, 'sem7_obtained_marks', Integer=True)
        sem7_total_marks = GetData.getData(self, request, 'sem7_total_marks', Integer=True)
        sem8_pointer = GetData.getData(self, request, 'sem8_pointer', Decimal=True)
        sem8_completion_date = GetData.getData(self, request, 'sem8_completion_date')
        sem8_obtained_marks = GetData.getData(self, request, 'sem8_obtained_marks', Integer=True)
        sem8_total_marks = GetData.getData(self, request, 'sem8_total_marks', Integer=True)
        cgpa = request.data['cgpa']
        be_percent = request.data['be_percent']
        # Masters
        masters_sem1_pointer = GetData.getData(self, request, 'masters_sem1_pointer', Decimal=True)
        masters_sem1_completion_date = GetData.getData(self, request, 'masters_sem1_completion_date')
        masters_sem1_obtained_marks = GetData.getData(self, request, 'masters_sem1_obtained_marks', Integer=True)
        masters_sem1_total_marks = GetData.getData(self, request, 'masters_sem1_total_marks', Integer=True)
        masters_sem2_pointer = GetData.getData(self, request, 'masters_sem2_pointer', Decimal=True)
        masters_sem2_completion_date = GetData.getData(self, request, 'masters_sem2_completion_date')
        masters_sem2_obtained_marks = GetData.getData(self, request, 'masters_sem2_obtained_marks', Integer=True)
        masters_sem2_total_marks = GetData.getData(self, request, 'masters_sem2_total_marks', Integer=True)
        masters_sem3_pointer = GetData.getData(self, request, 'masters_sem3_pointer', Decimal=True)
        masters_sem3_completion_date = GetData.getData(self, request, 'masters_sem3_completion_date')
        masters_sem3_obtained_marks = GetData.getData(self, request, 'masters_sem3_obtained_marks', Integer=True)
        masters_sem3_total_marks = GetData.getData(self, request, 'masters_sem3_total_marks', Integer=True)
        masters_sem4_pointer = GetData.getData(self, request, 'masters_sem4_pointer', Decimal=True)
        masters_sem4_completion_date = GetData.getData(self, request, 'masters_sem4_completion_date')
        masters_sem4_obtained_marks = GetData.getData(self, request, 'masters_sem4_obtained_marks', Integer=True)
        masters_sem4_total_marks = GetData.getData(self, request, 'masters_sem4_total_marks', Integer=True)
        masters_cgpa = GetData.getData(self, request, 'masters_cgpa', Decimal=True)
        masters_percent = GetData.getData(self, request, 'masters_percent', Decimal=True)
        # kt
        livekt = GetData.getData(self, request, 'livekt', Integer=True)
        deadkt = GetData.getData(self, request, 'deadkt', Integer=True)
        gap =  GetData.getData(self, request, 'gap', Integer=True)
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)
        status = 200

        try:
            if (user_roll_no == jwt_roll_no and userRecord.groups.filter(name='Student')) or (userRecord.groups.filter(name='Superuser')):
                try:
                    student = Student.objects.get(roll_no=user_roll_no)
                except Exception as e:
                    return Response({'status': 'Student does not exist', 'error_msg': str(e)}, status=500)
                academicRecord = AcademicInfo.objects.get(student=student)
                academicRecord.tenth_percent = tenth_percent
                academicRecord.tenth_completion_date = tenth_completion_date
                academicRecord.tenth_obtained_marks = tenth_obtained_marks
                academicRecord.tenth_total_marks = tenth_total_marks
                academicRecord.twelveth_percent = twelveth_percent
                academicRecord.twelveth_completion_date = twelveth_completion_date
                academicRecord.twelveth_obtained_marks = twelveth_obtained_marks
                academicRecord.twelveth_total_marks = twelveth_total_marks
                academicRecord.diploma_percent = diploma_percent
                academicRecord.diploma_completion_date = diploma_completion_date
                academicRecord.diploma_obtained_marks = diploma_obtained_marks
                academicRecord.diploma_total_marks = diploma_total_marks
                academicRecord.sem1_pointer = sem1_pointer
                academicRecord.sem1_completion_date = sem1_completion_date
                academicRecord.sem1_obtained_marks = sem1_obtained_marks
                academicRecord.sem1_total_marks = sem1_total_marks
                academicRecord.sem2_pointer = sem2_pointer
                academicRecord.sem2_completion_date = sem2_completion_date
                academicRecord.sem2_obtained_marks = sem2_obtained_marks
                academicRecord.sem2_total_marks = sem2_total_marks
                academicRecord.sem3_pointer = sem3_pointer
                academicRecord.sem3_completion_date = sem3_completion_date
                academicRecord.sem3_obtained_marks = sem3_obtained_marks
                academicRecord.sem3_total_marks = sem3_total_marks
                academicRecord.sem4_pointer = sem4_pointer
                academicRecord.sem4_completion_date = sem4_completion_date
                academicRecord.sem4_obtained_marks = sem4_obtained_marks
                academicRecord.sem4_total_marks = sem4_total_marks
                academicRecord.sem5_pointer = sem5_pointer
                academicRecord.sem5_completion_date = sem5_completion_date
                academicRecord.sem5_obtained_marks = sem5_obtained_marks
                academicRecord.sem5_total_marks = sem5_total_marks
                academicRecord.sem6_pointer = sem6_pointer
                academicRecord.sem6_completion_date = sem6_completion_date
                academicRecord.sem6_obtained_marks = sem6_obtained_marks
                academicRecord.sem6_total_marks = sem6_total_marks
                academicRecord.sem7_pointer = sem7_pointer
                academicRecord.sem7_completion_date = sem7_completion_date
                academicRecord.sem7_obtained_marks = sem7_obtained_marks
                academicRecord.sem7_total_marks = sem7_total_marks
                academicRecord.sem8_pointer = sem8_pointer
                academicRecord.sem8_completion_date = sem8_completion_date
                academicRecord.sem8_obtained_marks = sem8_obtained_marks
                academicRecord.sem8_total_marks = sem8_total_marks
                academicRecord.cgpa = cgpa
                academicRecord.be_percent = be_percent
                academicRecord.masters_sem1_pointer = masters_sem1_pointer
                academicRecord.masters_sem1_completion_date = masters_sem1_completion_date
                academicRecord.masters_sem1_obtained_marks  = masters_sem1_obtained_marks
                academicRecord.masters_sem1_total_marks = masters_sem1_total_marks
                academicRecord.masters_sem2_pointer = masters_sem2_pointer
                academicRecord.masters_sem2_completion_date = masters_sem2_completion_date
                academicRecord.masters_sem2_obtained_marks  = masters_sem2_obtained_marks
                academicRecord.masters_sem2_total_marks = masters_sem2_total_marks
                academicRecord.masters_sem3_pointer = masters_sem3_pointer
                academicRecord.masters_sem3_completion_date = masters_sem3_completion_date
                academicRecord.masters_sem3_obtained_marks  = masters_sem3_obtained_marks
                academicRecord.masters_sem3_total_marks = masters_sem3_total_marks
                academicRecord.masters_sem4_pointer = masters_sem4_pointer
                academicRecord.masters_sem4_completion_date = masters_sem4_completion_date
                academicRecord.masters_sem4_obtained_marks  = masters_sem4_obtained_marks
                academicRecord.masters_sem4_total_marks = masters_sem4_total_marks
                academicRecord.masters_cgpa = masters_cgpa
                academicRecord.masters_percent = masters_percent
                academicRecord.livekt = livekt
                academicRecord.deadkt = deadkt
                academicRecord.gap = gap
                academicRecord.save(update_fields=['tenth_percent', 'tenth_completion_date', 'tenth_obtained_marks', 'tenth_total_marks', 'twelveth_percent', 'twelveth_completion_date', 'twelveth_obtained_marks', 'twelveth_total_marks', 'diploma_percent', 'diploma_completion_date', 'diploma_obtained_marks', 'diploma_total_marks', 'sem1_pointer', 'sem1_completion_date', 'sem1_obtained_marks', 'sem1_total_marks', 'sem2_pointer', 'sem2_completion_date', 'sem2_obtained_marks', 'sem2_total_marks', 'sem3_pointer', 'sem3_completion_date', 'sem3_obtained_marks', 'sem3_total_marks', 'sem4_pointer', 'sem4_completion_date', 'sem4_obtained_marks', 'sem4_total_marks', 'sem5_pointer', 'sem5_completion_date', 'sem5_obtained_marks', 'sem5_total_marks', 'sem6_pointer', 'sem6_completion_date', 'sem6_obtained_marks', 'sem6_total_marks', 'sem7_pointer', 'sem7_completion_date', 'sem7_obtained_marks', 'sem7_total_marks', 'sem8_pointer', 'sem8_completion_date', 'sem8_obtained_marks', 'sem8_total_marks', 'cgpa', 'be_percent', 'masters_sem1_pointer', 'masters_sem1_completion_date', 'masters_sem1_obtained_marks', 'masters_sem1_total_marks', 'masters_sem2_pointer', 'masters_sem2_completion_date', 'masters_sem2_obtained_marks', 'masters_sem2_total_marks', 'masters_sem3_pointer', 'masters_sem3_completion_date', 'masters_sem3_obtained_marks', 'masters_sem3_total_marks', 'masters_sem4_pointer', 'masters_sem4_completion_date', 'masters_sem4_obtained_marks', 'masters_sem4_total_marks', 'masters_cgpa', 'masters_percent','livekt', 'deadkt', 'gap'])
                context = {'status': 'Academic Record Updated'}
            else:
                context = {'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}
                status = 403
        except:
            AcademicInfo.objects.create(student=student, tenth_percent=tenth_percent, tenth_completion_date=tenth_completion_date, tenth_obtained_marks=tenth_obtained_marks, tenth_total_marks=tenth_total_marks, twelveth_percent=twelveth_percent, twelveth_completion_date=twelveth_completion_date, twelveth_obtained_marks=twelveth_obtained_marks, twelveth_total_marks=twelveth_total_marks, diploma_percent=diploma_percent, diploma_completion_date=diploma_completion_date, diploma_obtained_marks=diploma_obtained_marks, diploma_total_marks=diploma_total_marks, sem1_pointer=sem1_pointer, sem1_completion_date=sem1_completion_date, sem1_obtained_marks=sem1_obtained_marks, sem1_total_marks=sem1_total_marks, sem2_pointer=sem2_pointer, sem2_completion_date=sem2_completion_date, sem2_obtained_marks=sem2_obtained_marks, sem2_total_marks=sem2_total_marks, sem3_pointer=sem3_pointer, sem3_completion_date=sem3_completion_date, sem3_obtained_marks=sem3_obtained_marks, sem3_total_marks=sem3_total_marks, sem4_pointer=sem4_pointer, sem4_completion_date=sem4_completion_date, sem4_obtained_marks=sem4_obtained_marks, sem4_total_marks=sem4_total_marks, sem5_pointer=sem5_pointer, sem5_completion_date=sem5_completion_date, sem5_obtained_marks=sem5_obtained_marks, sem5_total_marks=sem5_total_marks, sem6_pointer=sem6_pointer, sem6_completion_date=sem6_completion_date, sem6_obtained_marks=sem6_obtained_marks, sem6_total_marks=sem6_total_marks, sem7_pointer=sem7_pointer, sem7_completion_date=sem7_completion_date, sem7_obtained_marks=sem7_obtained_marks, sem7_total_marks=sem7_total_marks, sem8_pointer=sem8_pointer, sem8_completion_date=sem8_completion_date, sem8_obtained_marks=sem8_obtained_marks, sem8_total_marks=sem8_total_marks, cgpa=cgpa, be_percent=be_percent, masters_sem1_pointer=masters_sem1_pointer, masters_sem1_completion_date=masters_sem1_completion_date, masters_sem1_obtained_marks=masters_sem1_obtained_marks, masters_sem1_total_marks=masters_sem1_total_marks, masters_sem2_pointer=masters_sem2_pointer, masters_sem2_completion_date=masters_sem2_completion_date, masters_sem2_obtained_marks=masters_sem2_obtained_marks, masters_sem2_total_marks=masters_sem2_total_marks, masters_sem3_pointer=masters_sem3_pointer, masters_sem3_completion_date=masters_sem3_completion_date, masters_sem3_obtained_marks=masters_sem3_obtained_marks, masters_sem3_total_marks=masters_sem3_total_marks, masters_sem4_pointer=masters_sem4_pointer, masters_sem4_completion_date=masters_sem4_completion_date, masters_sem4_obtained_marks=masters_sem4_obtained_marks, masters_sem4_total_marks=masters_sem4_total_marks, masters_cgpa=masters_cgpa, masters_percent=masters_percent, livekt=livekt, deadkt=deadkt, gap=gap)
            context = {'status': 'Academic Record Added'}
        finally:
            return Response(context, status)


class AddSkillSet(APIView):

    def post(self, request):
        user_roll_no = request.data['roll_no'].strip()
        certificate_one = GetData.getData(self, request, 'certificate_one')
        certificate_one_completion_date = GetData.getData(self, request, 'certificate_one_completion_date')
        certificate_two = GetData.getData(self, request, 'certificate_two')
        certificate_two_completion_date = GetData.getData(self, request, 'certificate_two_completion_date')
        certificate_three = GetData.getData(self, request, 'certificate_three')
        certificate_three_completion_date = GetData.getData(self, request, 'certificate_three_completion_date')
        certificate_four = GetData.getData(self, request, 'certificate_four')
        certificate_four_completion_date = GetData.getData(self, request, 'certificate_four_completion_date')
        acad_achievement_one = GetData.getData(self, request, 'acad_achievement_one')
        acad_achievement_two = GetData.getData(self, request, 'acad_achievement_two')
        acad_achievement_three = GetData.getData(self, request, 'acad_achievement_three')
        acad_achievement_four = GetData.getData(self, request, 'acad_achievement_four')
        career_obj = request.data['career_obj']
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)
        status = 200

        try:
            if (user_roll_no == jwt_roll_no and userRecord.groups.filter(name='Student')) or (userRecord.groups.filter(name='Superuser')):
                try:
                    student = Student.objects.get(roll_no=user_roll_no)
                except Exception as e:
                    return Response({'status': 'Student does not exist', 'error_msg': str(e)}, status=500)
                skillsetRecord = SkillSet.objects.get(student=student)
                skillsetRecord.certificate_one = certificate_one
                skillsetRecord.certificate_one_completion_date = certificate_one_completion_date
                skillsetRecord.certificate_two = certificate_two
                skillsetRecord.certificate_two_completion_date = certificate_two_completion_date
                skillsetRecord.certificate_three = certificate_three
                skillsetRecord.certificate_three_completion_date = certificate_three_completion_date
                skillsetRecord.certificate_four = certificate_four
                skillsetRecord.certificate_four_completion_date = certificate_four_completion_date
                skillsetRecord.acad_achievement_one = acad_achievement_one
                skillsetRecord.acad_achievement_two = acad_achievement_two
                skillsetRecord.acad_achievement_three = acad_achievement_three
                skillsetRecord.acad_achievement_four = acad_achievement_four
                skillsetRecord.career_obj = career_obj
                skillsetRecord.save(update_fields=['certificate_one', 'certificate_one_completion_date', 'certificate_two', 'certificate_two_completion_date', 'certificate_three', 'certificate_three_completion_date', 'certificate_four', 'certificate_four_completion_date', 'acad_achievement_one', 'acad_achievement_two', 'acad_achievement_three', 'acad_achievement_four', 'career_obj'])
                context = {'status': 'SkillSet Record Updated'}
            else:
                context = {'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}
                status = 403
        except:
            SkillSet.objects.create(student=student, certificate_one=certificate_one, certificate_one_completion_date=certificate_one_completion_date, certificate_two=certificate_two, certificate_two_completion_date=certificate_two_completion_date, certificate_three=certificate_three, certificate_three_completion_date=certificate_three_completion_date, certificate_four=certificate_four, certificate_four_completion_date=certificate_four_completion_date, acad_achievement_four=acad_achievement_four, acad_achievement_one=acad_achievement_one, acad_achievement_two=acad_achievement_two, acad_achievement_three=acad_achievement_three, career_obj=career_obj)
            context = {'status': 'SkillSet Record Added'}
        finally:
            return Response(context, status)


class AddExperience(APIView):

    def post(self, request):
        user_roll_no = request.data['roll_no'].strip()
        internship_one_title = GetData.getData(self, request, 'internship_one_title')
        internship_one_description = GetData.getData(self, request, 'internship_one_description')
        internship_one_start_date = GetData.getData(self, request, 'internship_one_start_date')
        internship_one_end_date = GetData.getData(self, request, 'internship_one_end_date')
        internship_two_title = GetData.getData(self, request, 'internship_two_title')
        internship_two_description = GetData.getData(self, request, 'internship_two_description')
        internship_two_start_date = GetData.getData(self, request, 'internship_two_start_date')
        internship_two_end_date = GetData.getData(self, request, 'internship_two_end_date')
        internship_three_title = GetData.getData(self, request, 'internship_three_title')
        internship_three_description = GetData.getData(self, request, 'internship_three_description')
        internship_three_start_date = GetData.getData(self, request, 'internship_three_start_date')
        internship_three_end_date = GetData.getData(self, request, 'internship_three_end_date')
        project_one_title = request.data['project_one_title']
        project_one_description = request.data['project_one_description']
        project_one_start_date = request.data['project_one_start_date']
        project_one_end_date = request.data['project_one_end_date']
        project_two_title = GetData.getData(self, request, 'project_two_title')
        project_two_description = GetData.getData(self, request, 'project_two_description')
        project_two_start_date = GetData.getData(self, request, 'project_two_start_date')
        project_two_end_date = GetData.getData(self, request, 'project_two_end_date')
        project_three_title = GetData.getData(self, request, 'project_three_title')
        project_three_description = GetData.getData(self, request, 'project_three_description')
        project_three_start_date = GetData.getData(self, request, 'project_three_start_date')
        project_three_end_date = GetData.getData(self, request, 'project_three_end_date')
        pref_lang = request.data['pref_lang']
        technologies = request.data['technologies']
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)
        status = 200

        try:
            if (user_roll_no == jwt_roll_no and userRecord.groups.filter(name='Student')) or (userRecord.groups.filter(name='Superuser')):
                try:
                    student = Student.objects.get(roll_no=user_roll_no)
                except Exception as e:
                    return Response({'status': 'Student does not exist', 'error_msg': str(e)}, status=500)
                experienceRecord = Experience.objects.get(student=student)
                experienceRecord.internship_one_title = internship_one_title
                experienceRecord.internship_one_description = internship_one_description
                experienceRecord.internship_one_start_date = internship_one_start_date
                experienceRecord.internship_one_end_date = internship_one_end_date
                experienceRecord.internship_two_title = internship_two_title
                experienceRecord.internship_two_description = internship_two_description
                experienceRecord.internship_two_start_date = internship_two_start_date
                experienceRecord.internship_two_end_date = internship_two_end_date
                experienceRecord.internship_three_title = internship_three_title
                experienceRecord.internship_three_description = internship_three_description
                experienceRecord.internship_three_start_date = internship_three_start_date
                experienceRecord.internship_three_end_date = internship_three_end_date
                experienceRecord.project_one_title = project_one_title
                experienceRecord.project_one_description = project_one_description
                experienceRecord.project_one_start_date = project_one_start_date
                experienceRecord.project_one_end_date = project_one_end_date
                experienceRecord.project_two_title = project_two_title
                experienceRecord.project_two_description = project_two_description
                experienceRecord.project_two_start_date = project_two_start_date
                experienceRecord.project_two_end_date = project_two_end_date
                experienceRecord.project_three_title = project_three_title
                experienceRecord.project_three_description = project_three_description
                experienceRecord.project_three_start_date = project_three_start_date
                experienceRecord.project_three_end_date = project_three_end_date
                experienceRecord.pref_lang = pref_lang
                experienceRecord.technologies = technologies
                experienceRecord.save(update_fields=['internship_one_title', 'internship_one_description', 'internship_one_start_date', 'internship_one_end_date', 'internship_two_title', 'internship_two_description', 'internship_two_start_date', 'internship_two_end_date', 'internship_three_title', 'internship_three_description', 'internship_three_start_date', 'internship_three_end_date', 'project_one_title', 'project_one_description', 'project_one_start_date', 'project_one_end_date', 'project_two_title', 'project_two_description', 'project_two_start_date', 'project_two_end_date', 'project_three_title', 'project_three_description', 'project_three_start_date', 'project_three_end_date', 'pref_lang', 'technologies'])
                context = {'status': 'Experience Record Updated'}
            else:
                context = {'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}
                status = 403
        except:
            Experience.objects.create(student=student, internship_one_title=internship_one_title, internship_one_description=internship_one_description, internship_one_start_date=internship_one_start_date, internship_one_end_date=internship_one_end_date, internship_two_title=internship_two_title, internship_two_description=internship_two_description, internship_two_start_date=internship_two_start_date, internship_two_end_date=internship_two_end_date, internship_three_title=internship_three_title, internship_three_description=internship_three_description, internship_three_start_date=internship_three_start_date, internship_three_end_date=internship_three_end_date, project_one_title=project_one_title, project_one_description=project_one_description, project_one_start_date=project_one_start_date, project_one_end_date=project_one_end_date, project_two_title=project_two_title, project_two_description=project_two_description, project_two_start_date=project_two_start_date, project_two_end_date=project_two_end_date, project_three_title=project_three_title, project_three_description=project_three_description, project_three_start_date=project_three_start_date, project_three_end_date=project_three_end_date, pref_lang=pref_lang, technologies=technologies)
            context = {'status': 'Experience Record Added'}
        finally:
            return Response(context, status)


class AddPlacementDetails(APIView):

    def post(self, request):
        user_roll_no = request.data['roll_no'].strip()
        offer_letter_one = GetData.getData(self, request, 'offer_letter_one', File=True)
        offer_letter_two = GetData.getData(self, request, 'offer_letter_two', File=True)
        offer_letter_three = GetData.getData(self, request, 'offer_letter_three', File=True)
        placed_org_one = GetData.getData(self, request, 'placed_org_one')
        placed_org_two = GetData.getData(self, request, 'placed_org_two')
        placed_org_three = GetData.getData(self, request, 'placed_org_three')
        package_one = GetData.getData(self, request, 'package_one', Decimal=True)
        package_two = GetData.getData(self, request, 'package_two', Decimal=True)
        package_three = GetData.getData(self, request, 'package_three', Decimal=True)
        placed_company = GetData.getData(self, request, 'placed_company')
        placed_package = GetData.getData(self, request, 'placed_package', Decimal=True)
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)
        status = 200

        try:
            if (user_roll_no == jwt_roll_no and userRecord.groups.filter(name='Student')) or (userRecord.groups.filter(name='Superuser')):
                try:
                    student = Student.objects.get(roll_no=user_roll_no)
                except Exception as e:
                    return Response({'status': 'Student does not exist', 'error_msg': str(e)}, status=500)
                placementRecord = PlacementDetails.objects.get(student=student)
                placementRecord.offer_letter_one = offer_letter_one
                placementRecord.offer_letter_two = offer_letter_two
                placementRecord.offer_letter_three = offer_letter_three
                placementRecord.placed_org_one = placed_org_one
                placementRecord.placed_org_two = placed_org_two
                placementRecord.placed_org_three = placed_org_three
                placementRecord.package_one = package_one
                placementRecord.package_two = package_two
                placementRecord.package_three = package_three
                placementRecord.placed_company = placed_company
                placementRecord.placed_package = placed_package
                placementRecord.save(update_fields=['offer_letter_one', 'offer_letter_two', 'offer_letter_three', 'placed_org_one', 'placed_org_two', 'placed_org_three', 'package_one', 'package_two', 'package_three', 'placed_company', 'placed_package'])
                context = {'status': 'Placement Record Updated'}
            else:
                context = {'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}
                status = 403
        except:
            PlacementDetails.objects.create(student=student, offer_letter_one=offer_letter_one, offer_letter_two=offer_letter_two, offer_letter_three=offer_letter_three, placed_org_one=placed_org_one, placed_org_two=placed_org_two, placed_org_three=placed_org_three, package_one=package_one, package_two=package_two, package_three=package_three, placed_company=placed_company, placed_package=placed_package)
            context = {'status': 'Placement Record Added'}
        finally:
            return Response(context, status)


class AddOtherInfo(APIView):

    def post(self, request):
        user_roll_no = request.data['roll_no'].strip()
        hobbies = request.data['hobbies']
        pos_of_res_one = GetData.getData(self, request, 'pos_of_res_one')
        pos_of_res_two = GetData.getData(self, request, 'pos_of_res_two')
        pos_of_res_three = GetData.getData(self, request, 'pos_of_res_three')
        pos_of_res_four = GetData.getData(self, request, 'pos_of_res_four')
        extracuricular_one = GetData.getData(self, request, 'extracuricular_one')
        extracuricular_two = GetData.getData(self, request, 'extracuricular_two')
        extracuricular_three = GetData.getData(self, request, 'extracuricular_three')
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)
        status = 200

        try:
            if (user_roll_no == jwt_roll_no and userRecord.groups.filter(name='Student')) or (userRecord.groups.filter(name='Superuser')):
                try:
                    student = Student.objects.get(roll_no=user_roll_no)
                except Exception as e:
                    return Response({'status': 'Student does not exist', 'error_msg': str(e)}, status=500)
                otherRecord = OtherInfo.objects.get(student=student)
                otherRecord.hobbies = hobbies
                otherRecord.pos_of_res_one = pos_of_res_one
                otherRecord.pos_of_res_two = pos_of_res_two
                otherRecord.pos_of_res_three = pos_of_res_three
                otherRecord.pos_of_res_four = pos_of_res_four
                otherRecord.extracuricular_one = extracuricular_one
                otherRecord.extracuricular_two = extracuricular_two
                otherRecord.extracuricular_three = extracuricular_three
                otherRecord.save(update_fields=['hobbies', 'pos_of_res_one', 'pos_of_res_two', 'pos_of_res_three', 'pos_of_res_four', 'extracuricular_one', 'extracuricular_two', 'extracuricular_three'])
                context = {'status': 'Other Info Updated'}
            else:
                context = {'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}
                status = 403
        except:
            OtherInfo.objects.create(student=student, hobbies=hobbies, pos_of_res_one=pos_of_res_one, pos_of_res_two=pos_of_res_two, pos_of_res_three=pos_of_res_three, pos_of_res_four=pos_of_res_four, extracuricular_one=extracuricular_one, extracuricular_two=extracuricular_two, extracuricular_three=extracuricular_three)
            context = {'status': 'Other Info Added'}
        finally:
            return Response(context, status)


class ViewStudent(APIView):

    def post(self, request):
        user_roll_no = request.data['roll_no'].strip()
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)

        if (user_roll_no == jwt_roll_no and userRecord.groups.filter(name='Student')) or (userRecord.groups.filter(name='Superuser')):
            try:
                student = Student.objects.get(roll_no=user_roll_no)
                try:
                    photo = student.photo.url
                except:
                    photo = ''
                response = {
                    'roll_no': student.roll_no,
                    'first_name': student.first_name,
                    'middle_name': student.middle_name,
                    'last_name': student.last_name,
                    'email': student.email,
                    'phone_number': student.phone_number,
                    'gender': student.gender,
                    'github': student.github,
                    'linkedin': student.linkedin,
                    'no_of_offers': student.no_of_offers,
                    'photo': photo,
                    'department': student.department,
                    'batch': student.batch,
                    'rait_email': student.rait_email
                }
                return Response(response)
            except Exception as e:
                return Response({'status': 'error', 'error_msg': str(e)}, status=500)
        else:
            return Response({'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}, status = 403)


class ViewAcademicInfo(APIView):

    def post(self, request):
        user_roll_no = request.data['roll_no'].strip()
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)

        if (user_roll_no == jwt_roll_no and userRecord.groups.filter(name='Student')) or (userRecord.groups.filter(name='Superuser')):
            try:
                student = Student.objects.get(roll_no=user_roll_no)
                academic_info = AcademicInfo.objects.get(student=student)
                response = {
                    'roll_no': academic_info.student.roll_no,
                    'tenth_percent': academic_info.tenth_percent,
                    'tenth_completion_date': academic_info.tenth_completion_date,
                    'tenth_obtained_marks': academic_info.tenth_obtained_marks,
                    'tenth_total_marks': academic_info.tenth_total_marks,
                    'twelveth_percent': academic_info.twelveth_percent,
                    'twelveth_completion_date': academic_info.twelveth_completion_date,
                    'twelveth_obtained_marks': academic_info.twelveth_obtained_marks,
                    'twelveth_total_marks': academic_info.twelveth_total_marks,
                    'diploma_percent': academic_info.diploma_percent,
                    'diploma_completion_date': academic_info.diploma_completion_date,
                    'diploma_obtained_marks': academic_info.diploma_obtained_marks,
                    'diploma_total_marks': academic_info.diploma_total_marks,
                    'sem1_pointer': academic_info.sem1_pointer,
                    'sem1_completion_date': academic_info.sem1_completion_date,
                    'sem1_obtained_marks': academic_info.sem1_obtained_marks,
                    'sem1_total_marks': academic_info.sem1_total_marks,
                    'sem2_pointer': academic_info.sem2_pointer,
                    'sem2_completion_date': academic_info.sem2_completion_date,
                    'sem2_obtained_marks': academic_info.sem2_obtained_marks,
                    'sem2_total_marks': academic_info.sem2_total_marks,
                    'sem3_pointer': academic_info.sem3_pointer,
                    'sem3_completion_date': academic_info.sem3_completion_date,
                    'sem3_obtained_marks': academic_info.sem3_obtained_marks,
                    'sem3_total_marks': academic_info.sem3_total_marks,
                    'sem4_pointer': academic_info.sem4_pointer,
                    'sem4_completion_date': academic_info.sem4_completion_date,
                    'sem4_obtained_marks': academic_info.sem4_obtained_marks,
                    'sem4_total_marks': academic_info.sem4_total_marks,
                    'sem5_pointer': academic_info.sem5_pointer,
                    'sem5_completion_date': academic_info.sem5_completion_date,
                    'sem5_obtained_marks': academic_info.sem5_obtained_marks,
                    'sem5_total_marks': academic_info.sem5_total_marks,
                    'sem6_pointer': academic_info.sem6_pointer,
                    'sem6_completion_date': academic_info.sem6_completion_date,
                    'sem6_obtained_marks': academic_info.sem6_obtained_marks,
                    'sem6_total_marks': academic_info.sem6_total_marks,
                    'sem7_pointer': academic_info.sem7_pointer,
                    'sem7_completion_date': academic_info.sem7_completion_date,
                    'sem7_obtained_marks': academic_info.sem7_obtained_marks,
                    'sem7_total_marks': academic_info.sem7_total_marks,
                    'sem8_pointer': academic_info.sem8_pointer,
                    'sem8_completion_date': academic_info.sem8_completion_date,
                    'sem8_obtained_marks': academic_info.sem8_obtained_marks,
                    'sem8_total_marks': academic_info.sem8_total_marks,
                    'cgpa': academic_info.cgpa,
                    'be_percent': academic_info.be_percent,
                    'masters_sem1_pointer': academic_info.masters_sem1_pointer,
                    'masters_sem1_completion_date': academic_info.masters_sem1_completion_date,
                    'masters_sem1_obtained_marks': academic_info.masters_sem1_obtained_marks,
                    'masters_sem1_total_marks': academic_info.masters_sem1_total_marks,
                    'masters_sem2_pointer': academic_info.masters_sem2_pointer,
                    'masters_sem2_completion_date': academic_info.masters_sem2_completion_date,
                    'masters_sem2_obtained_marks': academic_info.masters_sem2_obtained_marks,
                    'masters_sem2_total_marks': academic_info.masters_sem2_total_marks,
                    'masters_sem3_pointer': academic_info.masters_sem3_pointer,
                    'masters_sem3_completion_date': academic_info.masters_sem3_completion_date,
                    'masters_sem3_obtained_marks': academic_info.masters_sem3_obtained_marks,
                    'masters_sem3_total_marks': academic_info.masters_sem3_total_marks,
                    'masters_sem4_pointer': academic_info.masters_sem4_pointer,
                    'masters_sem4_completion_date': academic_info.masters_sem4_completion_date,
                    'masters_sem4_obtained_marks': academic_info.masters_sem4_obtained_marks,
                    'masters_sem4_total_marks': academic_info.masters_sem4_total_marks,
                    'masters_cgpa': academic_info.masters_cgpa,
                    'masters_percent': academic_info.masters_percent
                }
                return Response(response)
            except Exception as e:
                return Response({'status': 'error', 'error_msg': str(e)}, status=500)
        else:
            return Response({'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}, status = 403)


class ViewSkillSet(APIView):

    def post(self, request):
        user_roll_no = request.data['roll_no'].strip()
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)

        if (user_roll_no == jwt_roll_no and userRecord.groups.filter(name='Student')) or (userRecord.groups.filter(name='Superuser')):
            try:
                student = Student.objects.get(roll_no=user_roll_no)
                skillset = SkillSet.objects.get(student=student)
                response = {
                    'roll_no': skillset.student.roll_no,
                    'certificate_one': skillset.certificate_one,
                    'certificate_one_completion_date': skillset.certificate_one_completion_date,
                    'certificate_two': skillset.certificate_two,
                    'certificate_two_completion_date': skillset.certificate_two_completion_date,
                    'certificate_three': skillset.certificate_three,
                    'certificate_three_completion_date': skillset.certificate_three_completion_date,
                    'certificate_four': skillset.certificate_four,
                    'certificate_four_completion_date': skillset.certificate_four_completion_date,
                    'acad_achievement_one': skillset.acad_achievement_one,
                    'acad_achievement_two': skillset.acad_achievement_two,
                    'acad_achievement_three': skillset.acad_achievement_three,
                    'acad_achievement_four': skillset.acad_achievement_four,
                    'career_obj': skillset.career_obj
                }
                return Response(response)
            except Exception as e:
                return Response({'status': 'error', 'error_msg': str(e)}, status=500)
        else:
            return Response({'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}, status = 403)


class ViewExperience(APIView):

    def post(self, request):
        user_roll_no = request.data['roll_no'].strip()
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)

        if (user_roll_no == jwt_roll_no and userRecord.groups.filter(name='Student')) or (userRecord.groups.filter(name='Superuser')):
            try:
                student = Student.objects.get(roll_no=user_roll_no)
                experience = Experience.objects.get(student=student)
                response = {
                    'roll_no': experience.student.roll_no,
                    'internship_one_title': experience.internship_one_title,
                    'internship_one_description': experience.internship_one_description,
                    'internship_one_start_date': experience.internship_one_start_date,
                    'internship_one_end_date': experience.internship_one_end_date,
                    'internship_two_title': experience.internship_two_title,
                    'internship_two_description': experience.internship_two_description,
                    'internship_two_start_date': experience.internship_two_start_date,
                    'internship_two_end_date': experience.internship_two_end_date,
                    'internship_three_title': experience.internship_three_title,
                    'internship_three_description': experience.internship_three_description,
                    'internship_three_start_date': experience.internship_three_start_date,
                    'internship_three_end_date': experience.internship_three_end_date,
                    'project_one_title': experience.project_one_title,
                    'project_one_description': experience.project_one_description,
                    'project_one_start_date': experience.project_one_start_date,
                    'project_one_end_date': experience.project_one_end_date,
                    'project_two_title': experience.project_two_title,
                    'project_two_description': experience.project_two_description,
                    'project_two_start_date': experience.project_two_start_date,
                    'project_two_end_date': experience.project_two_end_date,
                    'project_three_title': experience.project_three_title,
                    'project_three_description': experience.project_three_description,
                    'project_three_start_date': experience.project_three_start_date,
                    'project_three_end_date': experience.project_three_end_date,
                    'pref_lang': experience.pref_lang,
                    'technologies': experience.technologies
                }
                return Response(response)
            except Exception as e:
                return Response({'status': 'error', 'error_msg': str(e)}, status=500)
        else:
            return Response({'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}, status = 403)


class ViewPlacementDetails(APIView):

    def post(self, request):
        user_roll_no = request.data['roll_no'].strip()
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)

        if (user_roll_no == jwt_roll_no and userRecord.groups.filter(name='Student')) or (userRecord.groups.filter(name='Superuser')):
            try:
                student = Student.objects.get(roll_no=user_roll_no)
                placement_details = PlacementDetails.objects.get(student=student)
                try:
                    offer_letter_one = placement_details.offer_letter_one.url
                except:
                    offer_letter_one = ''
                try:
                    offer_letter_two = placement_details.offer_letter_two.url
                except:
                    offer_letter_two = ''
                try:
                    offer_letter_three = placement_details.offer_letter_three.url
                except:
                    offer_letter_three = ''
                response = {
                    'roll_no': placement_details.student.roll_no,
                    'offer_letter_one': offer_letter_one,
                    'offer_letter_two': offer_letter_two,
                    'offer_letter_three': offer_letter_three,
                    'placed_org_one': placement_details.placed_org_one,
                    'placed_org_two': placement_details.placed_org_two,
                    'placed_org_three': placement_details.placed_org_three,
                    'package_one': placement_details.package_one,
                    'package_two': placement_details.package_two,
                    'package_three': placement_details.package_three,
                    'placed_company': placement_details.placed_company,
                    'placed_package': placement_details.placed_package
                }
                return Response(response)
            except Exception as e:
                return Response({'status': 'error', 'error_msg': str(e)}, status=500)
        else:
            return Response({'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}, status = 403)


class ViewOtherInfo(APIView):

    def post(self, request):
        user_roll_no = request.data['roll_no'].strip()
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)

        if (user_roll_no == jwt_roll_no and userRecord.groups.filter(name='Student')) or (userRecord.groups.filter(name='Superuser')):
            try:
                student = Student.objects.get(roll_no=user_roll_no)
                other_info = OtherInfo.objects.get(student=student)
                response = {
                    'hobbies': other_info.hobbies,
                    'pos_of_res_one': other_info.pos_of_res_one,
                    'pos_of_res_two': other_info.pos_of_res_two,
                    'pos_of_res_three': other_info.pos_of_res_three,
                    'pos_of_res_four': other_info.pos_of_res_four,
                    'extracuricular_one': other_info.extracuricular_one,
                    'extracuricular_two': other_info.extracuricular_two,
                    'extracuricular_three': other_info.extracuricular_three
                }
                return Response(response)
            except Exception as e:
                return Response({'status': 'error', 'error_msg': str(e)}, status=500)
        else:
            return Response({'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}, status = 403)


class Notifications(APIView):

    def getNotificationObject(self, notification):
        object = {
            'batch': notification.job_opening.batch,
            'valid_till': notification.job_opening.valid_till,
            'branch': notification.job_opening.branch,
            'tenth_percent': notification.job_opening.tenth_percent,
            'twelveth_percent': notification.job_opening.twelveth_percent,
            'cgpa': notification.job_opening.cgpa,
            'notice': notification.job_opening.notice,
            'package': notification.job_opening.package
        }
        return object

    def get(self, request):
        response = []
        roll_no = request.user.roll_no.strip()

        try:
            student = Student.objects.get(roll_no=roll_no)
            notifications = EligibleStudents.objects.filter(student=student)
            for notification in notifications:
                response.append(self.getNotificationObject(notification))
            return Response(response, status=200)

        except Exception as e:
            return Response({'status': 'error', 'error_msg': str(e)})