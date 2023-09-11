from django.contrib import admin

# Register your models here.
from .models import AcademicCourses
from .models import Session
from .models import Semester
from .models import DepartmentAlocation




admin.site.register(AcademicCourses)
admin.site.register(Session)
admin.site.register(Semester)
admin.site.register(DepartmentAlocation)
