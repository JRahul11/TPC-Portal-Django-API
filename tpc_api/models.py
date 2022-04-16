from django.db import models


class Student(models.Model):
    gender_choices = (
        ('M', 'M'),
        ('F', 'F')
    )

    roll_no = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender_choices, null=True, blank=True)
    github = models.CharField(max_length=50, null=True, blank=True)
    linkedin = models.CharField(max_length=50, null=True, blank=True)
    no_of_offers = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=50, default="dypatil@123")
    photo = models.ImageField(upload_to='studentPhoto', default=None, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    batch = models.IntegerField(null=True, blank=True)
    rait_email = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.roll_no

    class Meta:
        verbose_name_plural = "Student"
        db_table = "students"


class AcademicInfo(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
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

    def __str__(self):
        return self.student.roll_no

    class Meta:
        verbose_name_plural = "Student Academic Info"
        db_table = "academic_info"


class SkillSet(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    certificate_one = models.ImageField(upload_to='certificate', default=None, blank=True)
    certificate_two = models.ImageField(upload_to='certificate', default=None, blank=True)
    certificate_three = models.ImageField(upload_to='certificate', default=None, blank=True)
    certificate_four = models.ImageField(upload_to='certificate', default=None, blank=True)
    acad_achievement_one = models.CharField(max_length=50, null=True, blank=True)
    acad_achievement_two = models.CharField(max_length=50, null=True, blank=True)
    acad_achievement_three = models.CharField(max_length=50, null=True, blank=True)
    acad_achievement_four = models.CharField(max_length=50, null=True, blank=True)
    career_obj = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.student.roll_no

    class Meta:
        verbose_name_plural = "Student SkillSet"
        db_table = "student_skillset"


class Experience(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    internship_one = models.CharField(max_length=1000, null=True, blank=True)
    internship_two = models.CharField(max_length=1000, null=True, blank=True)
    internship_three = models.CharField(max_length=1000, null=True, blank=True)
    project_one = models.CharField(max_length=1000, null=True, blank=True)
    project_two = models.CharField(max_length=1000, null=True, blank=True)
    project_three = models.CharField(max_length=1000, null=True, blank=True)
    pref_lang = models.CharField(max_length=50, null=True, blank=True)
    technologies = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.student.roll_no

    class Meta:
        verbose_name_plural = "Student Experience"
        db_table = "student_experience"


class PlacementDetails(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    offer_letter_one = models.ImageField(upload_to='offerLetter', default=None, blank=True)
    offer_letter_two = models.ImageField(upload_to='offerLetter', default=None, blank=True)
    placed_org_one = models.CharField(max_length=50, null=True, blank=True)
    placed_org_two = models.CharField(max_length=50, null=True, blank=True)
    package_one = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)
    package_two = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)

    def __str__(self):
        return self.student.roll_no

    class Meta:
        verbose_name_plural = "Student Placement Detail"
        db_table = "student_placement_details"


class OtherInfo(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    hobbies = models.CharField(max_length=1000, null=True, blank=True)
    pos_of_res_one = models.CharField(max_length=50, null=True, blank=True)
    pos_of_res_two = models.CharField(max_length=50, null=True, blank=True)
    pos_of_res_three = models.CharField(max_length=50, null=True, blank=True)
    pos_of_res_four = models.CharField(max_length=50, null=True, blank=True)
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