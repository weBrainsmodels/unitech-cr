from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Department'


class Course(models.Model):
    course_Title = models.CharField(max_length=200)

    def __str__(self):
        return self.course_Title

    class Meta:
        verbose_name_plural = 'Course'


class Code(models.Model):
    course_Code = models.CharField(max_length=200)

    def __str__(self):
        return self.course_Code

    class Meta:
        verbose_name_plural = 'Course Code'




class CreateQuestion(models.Model):
    name_of_Department = models.ForeignKey(Department, on_delete=models.CASCADE, default=False)
    course_title = models.ForeignKey(Course, on_delete=models.CASCADE, default=False)
    course_Code = models.ForeignKey(Code, on_delete=models.CASCADE, default=False)
    test_Question = models.CharField(max_length=200, blank=False)
    option_A = models.CharField(max_length=200, blank=False)
    option_B = models.CharField(max_length=200, blank=False)
    option_C = models.CharField(max_length=200, blank=False)
    option_D = models.CharField(max_length=200, blank=False)
    marks = models.CharField(max_length=200, blank=False)
    correct_Answer = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.test_Question

    class Meta:
        verbose_name_plural = 'Question Bank'


