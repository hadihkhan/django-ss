from django.db import models

class Students(models.Model):
    gender = models.BooleanField()
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    Other_student_details = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class HomeWork(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    homework_title = models.CharField(max_length=200)
    homework_content = models.TextField()
    grade = models.CharField(max_length=200)
    other_homework_details = models.TextField()

    def __str__(self):
        return self.homework_title


class Reports(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    report_title = models.CharField(max_length=200)
    report_content = models.TextField()
    teacher_comments = models.TextField()
    other_report_details = models.TextField()

    def __str__(self):
        return self.report_title


class Addresses(models.Model):
    address_details = models.TextField()


class Parents(models.Model):
    gender = models.BooleanField()
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    other_parental_details = models.TextField()


class PatrentAddress(models.Model):
    address_id = models.ForeignKey(Addresses, on_delete=models.CASCADE)
    date_address_from = models.DateField()
    date_address_to = models.DateField()


class Subjects(models.Model):
    subjact_name = models.TextField()


class Schools (models.Model):
    address_id = models.ForeignKey(Addresses, on_delete=models.CASCADE)
    school_name = models.TextField()
    school_principle = models.CharField(max_length=200)
    other_school_details = models.TextField()


class Student_Address(models.Model):
    address_id = models.ForeignKey(Addresses, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    address_details = models.TextField()


class Student_parent (models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    parent_id = models.ForeignKey(Parents, on_delete=models.CASCADE)


class Families(models.Model):
    head_of_family_parent_id = models.ForeignKey(Parents, on_delete=models.CASCADE)
    family_name = models.CharField(max_length=200)


class Family_member (models.Model):
    family_id = models.ForeignKey(Families, on_delete=models.CASCADE)
    parent_or_student_member = models.CharField(max_length=200)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    parent_id = models.ForeignKey(Parents, on_delete=models.CASCADE)

class Teachers(models.Model):
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE)
    gender = models.BooleanField()
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    other_teacher_details =models.TextField()


class Classes(models.Model):
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    class_code = models.CharField(max_length=200)
    class_name  = models.CharField(max_length=200)
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return self.class_code + ' - ' + self.class_name


class Student_class(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()










