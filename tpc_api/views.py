import requests
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *


def getData(request, field, Decimal=False, Integer=False, File=False):
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
    no_of_offers = int(request.data['no_of_offers'])
    password = request.data['password']
    photo = request.FILES['photo']
    department = request.data['department']
    batch = int(request.data['batch'])
    rait_email = request.data['rait_email']

    try:
        student = Student.objects.get(roll_no=roll_no)
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
        student.save(update_fields=['first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'gender',
                     'github', 'linkedin', 'no_of_offers', 'password', 'photo', 'department', 'batch', 'rait_email'])
        context = {'status': 'Student Record Updated'}
    except:
        Student.objects.create(roll_no=roll_no, first_name=first_name, middle_name=middle_name, last_name=last_name, email=email, phone_number=phone_number, gender=gender,
                               github=github, linkedin=linkedin, no_of_offers=no_of_offers, password=password, photo=photo, department=department, batch=batch, rait_email=rait_email)
        context = {'status': 'Student Record Added'}
    finally:
        return Response(context)


@api_view(['POST'])
def addAcademicInfo(request):
    roll_no = request.data['roll_no']
    tenth_percent = request.data['tenth_percent']
    twelveth_percent = request.data['twelveth_percent']
    sem1_pointer = float(request.data['sem1_pointer'])
    sem2_pointer = float(request.data['sem2_pointer'])
    sem3_pointer = float(request.data['sem3_pointer'])
    sem4_pointer = float(request.data['sem4_pointer'])
    sem5_pointer = getData(request, 'sem5_pointer', Decimal=True)
    sem6_pointer = getData(request, 'sem6_pointer', Decimal=True)
    sem7_pointer = getData(request, 'sem7_pointer', Decimal=True)
    sem8_pointer = getData(request, 'sem8_pointer', Decimal=True)
    cgpa = request.data['cgpa']
    be_percent = request.data['be_percent']

    try:
        student = Student.objects.get(roll_no=roll_no)
    except Exception as e:
        return Response({'status': 'Student does not exist', 'error_msg': str(e)})

    try:
        academicRecord = AcademicInfo.objects.get(student=student)
        academicRecord.tenth_percent = tenth_percent
        academicRecord.twelveth_percent = twelveth_percent
        academicRecord.sem1_pointer = sem1_pointer
        academicRecord.sem2_pointer = sem2_pointer
        academicRecord.sem3_pointer = sem3_pointer
        academicRecord.sem4_pointer = sem4_pointer
        academicRecord.sem5_pointer = sem5_pointer
        academicRecord.sem6_pointer = sem6_pointer
        academicRecord.sem7_pointer = sem7_pointer
        academicRecord.sem8_pointer = sem8_pointer
        academicRecord.cgpa = cgpa
        academicRecord.be_percent = be_percent
        academicRecord.save(update_fields=['tenth_percent', 'twelveth_percent', 'sem1_pointer', 'sem2_pointer', 'sem3_pointer',
                            'sem4_pointer', 'sem5_pointer', 'sem6_pointer', 'sem7_pointer', 'sem8_pointer', 'cgpa', 'be_percent'])
        context = {'status': 'Academic Record Updated'}
    except:
        AcademicInfo.objects.create(student=student, tenth_percent=tenth_percent, twelveth_percent=twelveth_percent, sem1_pointer=sem1_pointer, sem2_pointer=sem2_pointer, sem3_pointer=sem3_pointer,
                                    sem4_pointer=sem4_pointer, sem5_pointer=sem5_pointer, sem6_pointer=sem6_pointer, sem7_pointer=sem7_pointer, sem8_pointer=sem8_pointer, cgpa=cgpa, be_percent=be_percent)
        context = {'status': 'Academic Record Added'}
    finally:
        return Response(context)


@api_view(['POST'])
def addSkillSet(request):
    roll_no = request.data['roll_no']
    certificate_one = getData(request, 'certificate_one', File=True)
    certificate_two = getData(request, 'certificate_two', File=True)
    certificate_three = getData(request, 'certificate_three', File=True)
    certificate_four = getData(request, 'certificate_four', File=True)
    acad_achievement_one = getData(request, 'acad_achievement_one')
    acad_achievement_two = getData(request, 'acad_achievement_two')
    acad_achievement_three = getData(request, 'acad_achievement_three')
    acad_achievement_four = getData(request, 'acad_achievement_four')
    career_obj = request.data['career_obj']

    try:
        student = Student.objects.get(roll_no=roll_no)
    except Exception as e:
        return Response({'status': 'Student does not exist', 'error_msg': str(e)})

    try:
        skillsetRecord = SkillSet.objects.get(student=student)
        skillsetRecord.certificate_one = certificate_one
        skillsetRecord.certificate_two = certificate_two
        skillsetRecord.certificate_three = certificate_three
        skillsetRecord.certificate_four = certificate_four
        skillsetRecord.acad_achievement_one = acad_achievement_one
        skillsetRecord.acad_achievement_two = acad_achievement_two
        skillsetRecord.acad_achievement_three = acad_achievement_three
        skillsetRecord.acad_achievement_four = acad_achievement_four
        skillsetRecord.career_obj = career_obj
        skillsetRecord.save(update_fields=['certificate_one', 'certificate_two', 'certificate_three', 'certificate_four',
                            'acad_achievement_one', 'acad_achievement_two', 'acad_achievement_three', 'acad_achievement_four', 'career_obj'])
        context = {'status': 'SkillSet Record Updated'}
    except:
        SkillSet.objects.create(student=student, certificate_one=certificate_one, certificate_two=certificate_two, certificate_three=certificate_three, certificate_four=certificate_four,
                                acad_achievement_four=acad_achievement_four, acad_achievement_one=acad_achievement_one, acad_achievement_two=acad_achievement_two, acad_achievement_three=acad_achievement_three, career_obj=career_obj)
        context = {'status': 'SkillSet Record Added'}
    finally:
        return Response(context)


@api_view(['POST'])
def addExperience(request):
    roll_no = request.data['roll_no']
    internship_one = getData(request, 'internship_one')
    internship_two = getData(request, 'internship_two')
    internship_three = getData(request, 'internship_three')
    project_one = request.data['project_one']
    project_two = getData(request, 'project_two')
    project_three = getData(request, 'project_three')
    pref_lang = request.data['pref_lang']
    technologies = request.data['technologies']

    try:
        student = Student.objects.get(roll_no=roll_no)
    except Exception as e:
        return Response({'status': 'Student does not exist', 'error_msg': str(e)})

    try:
        experienceRecord = Experience.objects.get(student=student)
        experienceRecord.internship_one = internship_one
        experienceRecord.internship_two = internship_two
        experienceRecord.internship_three = internship_three
        experienceRecord.project_one = project_one
        experienceRecord.project_two = project_two
        experienceRecord.project_three = project_three
        experienceRecord.pref_lang = pref_lang
        experienceRecord.technologies = technologies
        experienceRecord.save(update_fields=['internship_one', 'internship_two', 'internship_three',
                              'project_one', 'project_two', 'project_three', 'pref_lang', 'technologies'])
        context = {'status': 'Experience Record Updated'}
    except:
        Experience.objects.create(student=student, internship_one=internship_one, internship_two=internship_two, internship_three=internship_three,
                                  project_one=project_one, project_two=project_two, project_three=project_three, pref_lang=pref_lang, technologies=technologies)
        context = {'status': 'Experience Record Added'}
    finally:
        return Response(context)


@api_view(['POST'])
def addPlacementDetails(request):
    roll_no = request.data['roll_no']
    offer_letter_one = getData(request, offer_letter_one, File=True)
    offer_letter_two = getData(request, offer_letter_two, File=True)
    placed_org_one = getData(request, placed_org_one)
    placed_org_two = getData(request, placed_org_two)
    package_one = getData(request, package_one, Decimal=True)
    package_two = getData(request, package_two, Decimal=True)

    try:
        student = Student.objects.get(roll_no=roll_no)
    except Exception as e:
        return Response({'status': 'Student does not exist', 'error_msg': str(e)})

    try:
        placementRecord = PlacementDetails.objects.get(student=student)
        placementRecord.offer_letter_one = offer_letter_one
        placementRecord.offer_letter_two = offer_letter_two
        placementRecord.placed_org_one = placed_org_one
        placementRecord.placed_org_two = placed_org_two
        placementRecord.package_one = package_one
        placementRecord.package_two = package_two
        placementRecord.save(update_fields=['offer_letter_one', 'offer_letter_two',
                             'placed_org_one', 'placed_org_two', 'package_one', 'package_two'])
        context = {'status': 'Placement Record Updated'}
    except:
        PlacementDetails.objects.create(student=student, offer_letter_one=offer_letter_one, offer_letter_two=offer_letter_two,
                                        placed_org_one=placed_org_one, placed_org_two=placed_org_two, package_one=package_one, package_two=package_two)
        context = {'status': 'Placement Record Added'}
    finally:
        return Response(context)


@api_view(['POST'])
def addOtherInfo(request):
    roll_no = request.data['roll_no']
    hobbies = request.data['hobbies']
    pos_of_res_one = getData(request, 'pos_of_res_one')
    pos_of_res_two = getData(request, 'pos_of_res_two')
    pos_of_res_three = getData(request, 'pos_of_res_three')
    pos_of_res_four = getData(request, 'pos_of_res_four')
    extracuricular_one = getData(request, 'extracuricular_one')
    extracuricular_two = getData(request, 'extracuricular_two')
    extracuricular_three = getData(request, 'extracuricular_three')

    try:
        student = Student.objects.get(roll_no=roll_no)
    except Exception as e:
        return Response({'status': 'error', 'error_msg': str(e)})

    try:
        otherRecord = OtherInfo.objects.get(student=student)
        otherRecord.hobbies = hobbies
        otherRecord.pos_of_res_one = pos_of_res_one
        otherRecord.pos_of_res_two = pos_of_res_two
        otherRecord.pos_of_res_three = pos_of_res_three
        otherRecord.pos_of_res_four = pos_of_res_four
        otherRecord.extracuricular_one = extracuricular_one
        otherRecord.extracuricular_two = extracuricular_two
        otherRecord.extracuricular_three = extracuricular_three
        otherRecord.save(update_fields=['hobbies', 'pos_of_res_one', 'pos_of_res_two', 'pos_of_res_three',
                         'pos_of_res_four', 'extracuricular_one', 'extracuricular_two', 'extracuricular_three'])
        context = {'status': 'Other Info Updated'}
    except:
        OtherInfo.objects.create(student=student, hobbies=hobbies, pos_of_res_one=pos_of_res_one, pos_of_res_two=pos_of_res_two, pos_of_res_three=pos_of_res_three,
                                 pos_of_res_four=pos_of_res_four, extracuricular_one=extracuricular_one, extracuricular_two=extracuricular_two, extracuricular_three=extracuricular_three)
        context = {'status': 'Other Info Added'}
    finally:
        return Response(context)


@api_view(['POST'])
def viewStudent(request):
    roll_no = request.data['roll_no']

    try:
        student = Student.objects.get(roll_no=roll_no)
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
        return Response({'status': 'Student does not exist', 'error_msg': str(e)})


@api_view(['POST'])
def viewAcademicInfo(request):
    roll_no = request.data['roll_no']

    try:
        student = Student.objects.get(roll_no=roll_no)
        academic_info = AcademicInfo.objects.get(student=student)
        response = {
            'roll_no': academic_info.student.roll_no,
            'tenth_percent': academic_info.tenth_percent,
            'twelveth_percent': academic_info.twelveth_percent,
            'sem1_pointer': academic_info.sem1_pointer,
            'sem2_pointer': academic_info.sem2_pointer,
            'sem3_pointer': academic_info.sem3_pointer,
            'sem4_pointer': academic_info.sem4_pointer,
            'sem5_pointer': academic_info.sem5_pointer,
            'sem6_pointer': academic_info.sem6_pointer,
            'sem7_pointer': academic_info.sem7_pointer,
            'sem8_pointer': academic_info.sem8_pointer,
            'cgpa': academic_info.cgpa,
            'be_percent': academic_info.be_percent
        }
        return Response(response)
    except Exception as e:
        return Response({'status': 'Student does not exist', 'error_msg': str(e)})


@api_view(['POST'])
def viewSkillSet(request):
    roll_no = request.data['roll_no']

    try:
        student = Student.objects.get(roll_no=roll_no)
        skillset = SkillSet.objects.get(student=student)
        try:
            certificate_one = skillset.certificate_one.url
        except:
            certificate_one = ''
        try:
            certificate_two = skillset.certificate_two.url
        except:
            certificate_two = ''
        try:
            certificate_three = skillset.certificate_three.url
        except:
            certificate_three = ''
        try:
            certificate_four = skillset.certificate_four.url
        except:
            certificate_four = ''
        response = {
            'roll_no': skillset.student.roll_no,
            'certificate_one': certificate_one,
            'certificate_two': certificate_two,
            'certificate_three': certificate_three,
            'certificate_four': certificate_four,
            'acad_achievement_one': skillset.acad_achievement_one,
            'acad_achievement_two': skillset.acad_achievement_two,
            'acad_achievement_three': skillset.acad_achievement_three,
            'acad_achievement_four': skillset.acad_achievement_four,
            'career_obj': skillset.career_obj
        }
        return Response(response)
    except Exception as e:
        return Response({'status': 'Student does not exist', 'error_msg': str(e)})


@api_view(['POST'])
def viewExperience(request):
    roll_no = request.data['roll_no']

    try:
        student = Student.objects.get(roll_no=roll_no)
        experience = Experience.objects.get(student=student)
        response = {
            'roll_no': experience.student.roll_no,
            'internship_one': experience.internship_one,
            'internship_two': experience.internship_two,
            'internship_three': experience.internship_three,
            'project_one': experience.project_one,
            'project_two': experience.project_two,
            'project_three': experience.project_three,
            'pref_lang': experience.pref_lang,
            'technologies': experience.technologies
        }
        return Response(response)
    except Exception as e:
        return Response({'status': 'Student does not exist', 'error_msg': str(e)})


@api_view(['POST'])
def viewPlacementDetails(request):
    roll_no = request.data['roll_no']

    try:
        student = Student.objects.get(roll_no=roll_no)
        placement_details = PlacementDetails.objects.get(student=student)
        try:
            offer_letter_one = placement_details.offer_letter_one.url
        except:
            offer_letter_one = ''
        try:
            offer_letter_two = placement_details.offer_letter_two.url
        except:
            offer_letter_two = ''
        response = {
            'roll_no': placement_details.student.roll_no,
            'offer_letter_one': offer_letter_one,
            'offer_letter_two': offer_letter_two,
            'placed_org_one': placement_details.placed_org_one,
            'placed_org_two': placement_details.placed_org_two,
            'package_one': placement_details.package_one,
            'package_two': placement_details.package_two
        }
        return Response(response)
    except Exception as e:
        return Response({'status': 'Student does not exist', 'error_msg': str(e)})


@api_view(['POST'])
def viewOtherInfo(request):
    roll_no = request.data['roll_no']

    try:
        student = Student.objects.get(roll_no=roll_no)
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
        return Response({'status': 'Student does not exist', 'error_msg': str(e)})


@api_view(['POST'])
def studentLogin(request):
    pass


@api_view(['GET'])
def getAllStudents(request):
    url = "https://tpc-backend-node.herokuapp.com/filter"
    payload = ""
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return Response(response.json())


@api_view(['POST'])
def getStudentByRollNo(request):
    roll_no = request.data['roll_no']
    url = "https://tpc-backend-node.herokuapp.com/filter/" + roll_no
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return Response(response.json())


@api_view(['POST'])
def getStudentsByDept(request):
    department = request.data['department']
    url = "https://tpc-backend-node.herokuapp.com/filter/dept/" + department
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return Response(response.json())


@api_view(['POST'])
def getStudentProfile(request):
    roll_no = request.data['roll_no']
    url = "https://tpc-backend-node.herokuapp.com/filter/profile/" + roll_no
    payload = ""
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return Response(response.json())


@api_view(['POST'])
def dashboard(request):

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
