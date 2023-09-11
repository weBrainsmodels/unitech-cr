from django.contrib import admin

# Register your models here.

from .models import CreateQuestion
from .models import Department
from .models import Course
from .models import Code




admin.site.register(CreateQuestion)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Code)