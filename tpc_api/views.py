from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *


@api_view(['POST'])
def addStudent(request):
    roll_no = request.data['roll_no']
    first_name = request.data['first_name']
    middle_name = request.data['middle_name']
    last_name = request.data['last_name']
    email = request.data['email']
    phone_number = request.data['phone_number']
    gender = request.data['gender']
    github = request.data['github']
    linkedin = request.data['linkedin']
    no_of_offers = request.data['no_of_offers']
    password = request.data['password']
    photo = request.FILES['photo']
    department = request.data['department']
    batch = request.data['batch']
    rait_email = request.data['rait_email']

    try:
        Student.objects.create(
            roll_no=roll_no, first_name=first_name, middle_name=middle_name, last_name=last_name, email=email, phone_number=phone_number, gender=gender, github=github, linkedin=linkedin, no_of_offers=no_of_offers, password=password, photo=photo, department=department, batch=batch, rait_email=rait_email
        )
        context = {'status': 'success'}
    except Exception as e:
        context = {'status': 'error', 'error_msg': str(e)}
    finally:
        return Response(context)


@api_view(['POST'])
def addAcademicInfo(request):
    roll_no = request.data['roll_no']
    tenth_percent = request.data['tenth_percent']
    twelveth_percent = request.data['twelveth_percent']
    sem1_pointer = request.data['sem1_pointer']
    sem2_pointer = request.data['sem2_pointer']
    sem3_pointer = request.data['sem3_pointer']
    sem4_pointer = request.data['sem4_pointer']
    sem5_pointer = request.data['sem5_pointer']
    sem6_pointer = request.data['sem6_pointer']
    sem7_pointer = request.data['sem7_pointer']
    sem8_pointer = request.data['sem8_pointer']
    cgpa = request.data['cgpa']
    be_percent = request.data['be_percent']

    try:
        student = Student.objects.get(roll_no=roll_no)
    except Exception as e:
        return Response({'status': 'error', 'error_msg': str(e)})
    try:
        AcademicInfo.objects.get(student=student).delete()
    except:
        pass

    AcademicInfo.objects.create(student=student, tenth_percent=tenth_percent, twelveth_percent=twelveth_percent, sem1_pointer=sem1_pointer, sem2_pointer=sem2_pointer, sem3_pointer=sem3_pointer,
                                sem4_pointer=sem4_pointer, sem5_pointer=sem5_pointer, sem6_pointer=sem6_pointer, sem7_pointer=sem7_pointer, sem8_pointer=sem8_pointer, cgpa=cgpa, be_percent=be_percent
                                )
    return Response({'status': 'success'})


@api_view(['POST'])
def addSkillSet(request):
    pass


@api_view(['POST'])
def addExperience(request):
    pass


@api_view(['POST'])
def addPlacementDetails(request):
    pass


@api_view(['POST'])
def addOtherInfo(request):
    pass
