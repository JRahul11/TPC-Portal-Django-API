from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from company.models import JobOpening


class CustomManager(BaseUserManager):

    def create_superuser(self, rait_email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        
        if other_fields.get('is_staff') is not True or other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True and is_superuser=True')
        
        return self.create_user(rait_email, password, **other_fields)

    def create_user(self, rait_email, password, **other_fields):
        
        if not rait_email:
            raise ValueError(_('You should provide a RAIT email address'))
        
        rait_email = self.normalize_email(rait_email)
        user = self.model(rait_email=rait_email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class Student(AbstractBaseUser, PermissionsMixin):
    gender_choices = (
        ('M', 'M'),
        ('F', 'F')
    )

    roll_no = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True, unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender_choices, null=True, blank=True)
    github = models.CharField(max_length=50, null=True, blank=True)
    linkedin = models.CharField(max_length=50, null=True, blank=True)
    no_of_offers = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=100, default="dypatil@123")
    photo = models.CharField(max_length=100, null=True, blank=True)
    # photo = models.ImageField(upload_to='studentPhoto', default=None, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    batch = models.IntegerField(null=True, blank=True)
    rait_email = models.CharField(max_length=50, null=True, blank=True, unique=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomManager()
    
    USERNAME_FIELD  = 'rait_email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.roll_no

    class Meta:
        verbose_name_plural = "Student"
        db_table = "students"


class AcademicInfo(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True, db_column='roll_no')
    # SSC
    tenth_percent = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    tenth_completion_date = models.CharField(max_length=20, null=True, blank=True)
    tenth_obtained_marks = models.PositiveIntegerField(null=True, blank=True)
    tenth_total_marks = models.PositiveIntegerField(null=True, blank=True)
    # HSC
    twelveth_percent = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    twelveth_completion_date = models.CharField(max_length=20, null=True, blank=True)
    twelveth_obtained_marks = models.PositiveIntegerField(null=True, blank=True)
    twelveth_total_marks = models.PositiveIntegerField(null=True, blank=True)
    # Diploma
    diploma_percent = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    diploma_completion_date = models.CharField(max_length=20, null=True, blank=True)
    diploma_obtained_marks = models.PositiveIntegerField(null=True, blank=True)
    diploma_total_marks = models.PositiveIntegerField(null=True, blank=True)
    # Degree
    sem1_pointer = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sem1_completion_date = models.CharField(max_length=20, null=True, blank=True)
    sem1_obtained_marks = models.PositiveIntegerField(null=True, blank=True)
    sem1_total_marks = models.PositiveIntegerField(null=True, blank=True)
    sem2_pointer = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sem2_completion_date = models.CharField(max_length=20, null=True, blank=True)
    sem2_obtained_marks = models.PositiveIntegerField(null=True, blank=True)
    sem2_total_marks = models.PositiveIntegerField(null=True, blank=True)
    sem3_pointer = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sem3_completion_date = models.CharField(max_length=20, null=True, blank=True)
    sem3_obtained_marks = models.PositiveIntegerField(null=True, blank=True)
    sem3_total_marks = models.PositiveIntegerField(null=True, blank=True)
    sem4_pointer = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sem4_completion_date = models.CharField(max_length=20, null=True, blank=True)
    sem4_obtained_marks = models.PositiveIntegerField(null=True, blank=True)
    sem4_total_marks = models.PositiveIntegerField(null=True, blank=True)
    sem5_pointer = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sem5_completion_date = models.CharField(max_length=20, null=True, blank=True)
    sem5_obtained_marks = models.PositiveIntegerField(null=True, blank=True)
    sem5_total_marks = models.PositiveIntegerField(null=True, blank=True)
    sem6_pointer = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sem6_completion_date = models.CharField(max_length=20, null=True, blank=True)
    sem6_obtained_marks = models.PositiveIntegerField(null=True, blank=True)
    sem6_total_marks = models.PositiveIntegerField(null=True, blank=True)
    sem7_pointer = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sem7_completion_date = models.CharField(max_length=20, null=True, blank=True)
    sem7_obtained_marks = models.PositiveIntegerField(null=True, blank=True)
    sem7_total_marks = models.PositiveIntegerField(null=True, blank=True)
    sem8_pointer = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sem8_completion_date = models.CharField(max_length=20, null=True, blank=True)
    sem8_obtained_marks = models.PositiveIntegerField(null=True, blank=True)
    sem8_total_marks = models.PositiveIntegerField(null=True, blank=True)
    cgpa = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    be_percent = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    # Masters 
    masters_sem1_pointer = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    masters_sem1_completion_date = models.CharField(max_length=20, null=True, blank=True)
    masters_sem1_obtained_marks = models.PositiveIntegerField(null=True, blank=True)
    masters_sem1_total_marks = models.PositiveIntegerField(null=True, blank=True)
    masters_sem2_pointer = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    masters_sem2_completion_date = models.CharField(max_length=20, null=True, blank=True)
    masters_sem2_obtained_marks = models.PositiveIntegerField(null=True, blank=True)
    masters_sem2_total_marks = models.PositiveIntegerField(null=True, blank=True)
    masters_sem3_pointer = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    masters_sem3_completion_date = models.CharField(max_length=20, null=True, blank=True)
    masters_sem3_obtained_marks = models.PositiveIntegerField(null=True, blank=True)
    masters_sem3_total_marks = models.PositiveIntegerField(null=True, blank=True)
    masters_sem4_pointer = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    masters_sem4_completion_date = models.CharField(max_length=20, null=True, blank=True)
    masters_sem4_obtained_marks = models.PositiveIntegerField(null=True, blank=True)
    masters_sem4_total_marks = models.PositiveIntegerField(null=True, blank=True)
    masters_cgpa = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    masters_percent = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    # kt
    livekt = models.IntegerField(null=True, blank=True)
    deadkt = models.IntegerField(null=True, blank=True)
    gap = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.student.roll_no

    class Meta:
        verbose_name_plural = "Student Academic Info"
        db_table = "academic_info"


class SkillSet(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True, db_column='roll_no')
    # Certification 1
    certificate_one = models.CharField(max_length=200, null=True, blank=True)
    certificate_one_completion_date = models.CharField(max_length=20, null=True, blank=True)
    # Certification 2
    certificate_two = models.CharField(max_length=200, null=True, blank=True)
    certificate_two_completion_date = models.CharField(max_length=20, null=True, blank=True)
    # Certification 3
    certificate_three = models.CharField(max_length=200, null=True, blank=True)
    certificate_three_completion_date = models.CharField(max_length=20, null=True, blank=True)
    # Certification 4
    certificate_four = models.CharField(max_length=200, null=True, blank=True)
    certificate_four_completion_date = models.CharField(max_length=20, null=True, blank=True)
    # Academic Achievements
    acad_achievement_one = models.CharField(max_length=200, null=True, blank=True)
    acad_achievement_two = models.CharField(max_length=200, null=True, blank=True)
    acad_achievement_three = models.CharField(max_length=200, null=True, blank=True)
    acad_achievement_four = models.CharField(max_length=200, null=True, blank=True)
    career_obj = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.student.roll_no

    class Meta:
        verbose_name_plural = "Student SkillSet"
        db_table = "student_skillset"


class Experience(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True, db_column='roll_no')
    # Internship 1
    internship_one_title = models.CharField(max_length=100, null=True, blank=True)
    internship_one_description = models.CharField(max_length=1000, null=True, blank=True)
    internship_one_start_date = models.CharField(max_length=20, null=True, blank=True)
    internship_one_end_date = models.CharField(max_length=20, null=True, blank=True)
    # Internship 2
    internship_two_title = models.CharField(max_length=100, null=True, blank=True)
    internship_two_description = models.CharField(max_length=1000, null=True, blank=True)
    internship_two_start_date = models.CharField(max_length=20, null=True, blank=True)
    internship_two_end_date = models.CharField(max_length=20, null=True, blank=True)
    # Internship 3
    internship_three_title = models.CharField(max_length=100, null=True, blank=True)
    internship_three_description = models.CharField(max_length=1000, null=True, blank=True)
    internship_three_start_date = models.CharField(max_length=20, null=True, blank=True)
    internship_three_end_date = models.CharField(max_length=20, null=True, blank=True)
    # Project 1
    project_one_title = models.CharField(max_length=100, null=True, blank=True)
    project_one_description = models.CharField(max_length=1000, null=True, blank=True)
    project_one_start_date = models.CharField(max_length=20, null=True, blank=True)
    project_one_end_date = models.CharField(max_length=20, null=True, blank=True)
    # Project 2
    project_two_title = models.CharField(max_length=100, null=True, blank=True)
    project_two_description = models.CharField(max_length=1000, null=True, blank=True)
    project_two_start_date = models.CharField(max_length=20, null=True, blank=True)
    project_two_end_date = models.CharField(max_length=20, null=True, blank=True)
    # Project 3
    project_three_title = models.CharField(max_length=100, null=True, blank=True)
    project_three_description = models.CharField(max_length=1000, null=True, blank=True)
    project_three_start_date = models.CharField(max_length=20, null=True, blank=True)
    project_three_end_date = models.CharField(max_length=20, null=True, blank=True)

    pref_lang = models.CharField(max_length=50, null=True, blank=True)
    technologies = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.student.roll_no

    class Meta:
        verbose_name_plural = "Student Experience"
        db_table = "student_experience"


class PlacementDetails(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True, db_column='roll_no')
    # Offer Letters
    offer_letter_one = models.BinaryField(null=True, blank=True, editable=True)
    offer_letter_two = models.BinaryField(null=True, blank=True, editable=True)
    offer_letter_three = models.BinaryField(null=True, blank=True, editable=True)
    # offer_letter_one = models.ImageField(upload_to='offerLetter', default=None, blank=True)
    # offer_letter_two = models.ImageField(upload_to='offerLetter', default=None, blank=True)
    # offer_letter_three = models.ImageField(upload_to='offerLetter', default=None, blank=True)
    # Organizations Options
    placed_org_one = models.CharField(max_length=100, null=True, blank=True)
    placed_org_two = models.CharField(max_length=100, null=True, blank=True)
    placed_org_three = models.CharField(max_length=100, null=True, blank=True)
    # Packages Options
    package_one = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)
    package_two = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)
    package_three = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)
    # Selected Organization
    placed_company = models.CharField(max_length=50, null=True, blank=True)
    placed_package = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)

    def __str__(self):
        return self.student.roll_no

    class Meta:
        verbose_name_plural = "Student Placement Detail"
        db_table = "student_placement_details"


class OtherInfo(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True, db_column='roll_no')
    hobbies = models.CharField(max_length=1000, null=True, blank=True)
    # Position of Responsibility
    pos_of_res_one = models.CharField(max_length=100, null=True, blank=True)
    pos_of_res_two = models.CharField(max_length=100, null=True, blank=True)
    pos_of_res_three = models.CharField(max_length=100, null=True, blank=True)
    pos_of_res_four = models.CharField(max_length=100, null=True, blank=True)
    # Extracurricular Activities
    extracuricular_one = models.CharField(max_length=500, null=True, blank=True)
    extracuricular_two = models.CharField(max_length=500, null=True, blank=True)
    extracuricular_three = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.student.roll_no

    class Meta:
        verbose_name_plural = "Student Other Info"
        db_table = "other_info"


class Admin(models.Model):
    user_name = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name_plural = "Admin"
        db_table = "admins"


class EligibleStudents(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='roll_no')
    job_opening = models.ForeignKey(JobOpening, on_delete=models.CASCADE, db_column='job_id')

    def __str__(self):
        return self.student.roll_no + ' ' + str(self.job_opening.job_id)

    class Meta:
        verbose_name_plural = "Eligible Students"
        db_table = "eligible_students"