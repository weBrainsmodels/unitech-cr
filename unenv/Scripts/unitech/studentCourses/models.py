from django.db import models

# Create your models here.


class Session(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Academic Session'


class Semester(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Academic Semester'


class DepartmentAlocation(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Add Allocation'


class AcademicCourses(models.Model):
    course_Title = models.CharField(max_length=200)
    course_Code = models.CharField(max_length=15)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    credit_Hour = models.CharField(max_length=15)
    allocate_Course = models.ForeignKey(DepartmentAlocation, on_delete=models.CASCADE, default=False)

    def __str__(self):
        # return (self.course_Title, self.course_Code, self.semester, self.credit_Hour, self.allocate_Course)

          return self.course_Title + " ‖ " + self.course_Code +" ‖ " + self.credit_Hour

    class Meta:
        verbose_name_plural = 'Add Academic Course'