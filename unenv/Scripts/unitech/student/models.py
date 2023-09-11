from django.db import models
from django.contrib.auth.models import User
from datetime import date
from datetime import datetime, timedelta

# Create your models here.
from django.utils.translation import gettext_lazy as _


class Nationality(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Nationality'


class State(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'State Of Origin'


class LocalGovernment(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Local Government Origin'


class Village(models.Model):
    village_Name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.village_Name

    class Meta:
        verbose_name_plural = 'Name Of Village'

# class Matriculation(models.Model):
#     matriculation_No = models.CharField(max_length=20)
#     matriculation_Year = models.DateTimeField
#
#     class Meta:
#             verbose_name_plural = 'Matriculation List'
#
#     def __str__(self):
#         return self.matriculation_No

class StudentBioData(models.Model):
        # user = models.OneToOneField(User, on_delete=models.CASCADE)
        matriculation_No = models.CharField(max_length=200)
        first_Name = models.CharField(max_length=200)
        sure_Name = models.CharField(max_length=200)
        other_Name = models.CharField(max_length=200)
        FRESHMAN = "FR"
        SOPHOMORE = "SO"
        JUNIOR = "JR"
        SENIOR = "SR"
        GRADUATE = "GR"
        YEAR_IN_SCHOOL_CHOICES = [
            (FRESHMAN, "Freshman"),
            (SOPHOMORE, "Sophomore"),
            (JUNIOR, "Junior"),
            (SENIOR, "Senior"),
            (GRADUATE, "Graduate"),
        ]
        year_in_school = models.CharField(
            max_length=2,
            choices=YEAR_IN_SCHOOL_CHOICES,
            default=FRESHMAN,
        )

        def is_upperclass(self):
            return self.year_in_school in {self.JUNIOR, self.SENIOR}

        gender_choice = (
            ("male", "Male"),
            ("Female", "Female"),
        )
        gender = models.CharField(max_length=10, choices=gender_choice, default=False)
        date_Of_Birth = models.DateTimeField
        phone_No = models.CharField(max_length=200)
        email = models.CharField(max_length=200)
        profile_pic = models.ImageField(upload_to='profile_pic/Student/', blank=True)
        home_Address = models.CharField(max_length=40)
        # mobile = models.CharField(max_length=20)
        # matx_No = models.ForeignKey(Admission, on_delete=models.CASCADE)
        # stream = models.CharField(max_length=50, blank=True)
        nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE)
        state = models.ForeignKey(State, on_delete=models.CASCADE)
        local_Government = models.ForeignKey(LocalGovernment, on_delete=models.CASCADE)
        village_Name = models.ForeignKey(Village, on_delete=models.CASCADE)
        mother_Maiden_name = models.CharField(max_length=200)


        def __str__(self):
            return self.first_Name + "  " + self.sure_Name +"  " + self.other_Name +" ‖ " + self.email +" ‖ " + self.matriculation_No

        class Meta:
            verbose_name_plural = 'Students Personal Information'

    # authors = models.ManyToManyField(Author)
    # number_of_comments = models.IntegerField(default=0)
    # number_of_pingbacks = models.IntegerField(default=0)
    # rating = models.IntegerField(default=5)

    # def __str__(self):
    #     return f"{self.date_Of_Birth.strftime('%d-%m-%Y')}"


    # @property
    # def get_name(self):
    #     return self.StudentBioData
    #     return self.user.first_Name + " " + self.user.sure_Name

    # @property
    # def get_instance(self):
    #     return self


class Level(models.Model):
    level = models.CharField(max_length=200)

    def __str__(self):
        return self.level

    class Meta:
        verbose_name_plural = 'Level Of Study'

# class StudentEnrolmentDetails(models.Model):

