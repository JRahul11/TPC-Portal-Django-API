from django.contrib.auth.models import Group


class CustomGroups:

    def getOrCreateGroups():
        studentGroup = Group.objects.get_or_create(name ='Student')
        superuserGroup = Group.objects.get_or_create(name='Superuser')
        companyGroup = Group.objects.get_or_create(name='Company')
