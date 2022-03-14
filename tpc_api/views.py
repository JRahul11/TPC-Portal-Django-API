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
    roll_no = request.data['roll_no']
    certificate_one = request.FILES['certificate_one']
    certificate_two = request.FILES['certificate_two']
    certificate_three = request.FILES['certificate_three']
    certificate_four = request.FILES['certificate_four']
    acad_achievement_one = request.data['acad_achievement_one']
    acad_achievement_two = request.data['acad_achievement_two']
    acad_achievement_three =request.data['acad_achievement_three']
    acad_achievement_four =request.data['acad_achievement_four']
    career_obj = request.data['career_obj']
    try:
        student = Student.objects.get(roll_no=roll_no)
    except Exception as e:
        return Response({'status': 'error', 'error_msg': str(e)})
    try:
        SkillSet.objects.get(student=student).delete()
    except:
        pass

    SkillSet.objects.create(student=student, certificate_one = certificate_one,career_obj = career_obj,
                            certificate_two = certificate_two,certificate_three = certificate_three,
                            certificate_four=certificate_four,acad_achievement_four=acad_achievement_four,
                            acad_achievement_one=acad_achievement_one , acad_achievement_two = acad_achievement_two,acad_achievement_three= acad_achievement_three
                                )
    return Response({'status': 'success'})


@api_view(['POST'])
def addExperience(request):
    roll_no = request.data['roll_no']
    internship_one = request.data['internship_one']
    internship_two = request.data['internship_two']
    internship_three = request.data['internship_three']
    project_one = request.data['project_one']
    project_two = request.data['project_two']
    project_three = request.data['project_three']
    pref_lang = request.data['pref_lang']
    technologies = request.data['technologies']
    try:
        student = Student.objects.get(roll_no=roll_no)
    except Exception as e:
        return Response({'status': 'error', 'error_msg': str(e)})
    try:
        Experience.objects.get(student=student).delete()
    except:
        pass

    Experience.objects.create(student=student, internship_one=internship_one, internship_two=internship_two, internship_three=internship_three, project_one=project_one, project_two=project_two,
                                project_three=project_three, pref_lang=pref_lang, technologies=technologies
                                )
    return Response({'status': 'success'})
    


@api_view(['POST'])
def addPlacementDetails(request):
    roll_no = request.data['roll_no']
    offer_letter_one = request.FILES['offer_letter_one']
    offer_letter_two = request.FILES['offer_letter_two']
    placed_org_one = request.data['placed_org_one']
    placed_org_two = request.data['placed_org_two']
    package_one = request.data['package_one']
    package_two = request.data['package_two']

    try:
        student = Student.objects.get(roll_no=roll_no)
    except Exception as e:
        return Response({'status': 'error', 'error_msg': str(e)})

    try:
        PlacementDetails.objects.get(student=student).delete()
    except:
        pass

    PlacementDetails.objects.create( student = student, offer_letter_one = offer_letter_one, offer_letter_two = offer_letter_two,
         placed_org_one = placed_org_one, placed_org_two=placed_org_two, package_one= package_one, package_two= package_two)
    return Response({'status': 'success'})


@api_view(['POST'])
def addOtherInfo(request):
    pass
