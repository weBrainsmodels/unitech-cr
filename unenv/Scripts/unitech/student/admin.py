from django.contrib import admin
from .models import StudentBioData
from .models import Nationality
from .models import State
from .models import LocalGovernment
from .models import Village
from .models import Level
# from .models import Matriculation

# Register your models here.


admin.site.register(StudentBioData)
admin.site.register(Nationality)
admin.site.register(State)
admin.site.register(LocalGovernment)
admin.site.register(Village)
admin.site.register(Level)
# admin.site.register(Matriculation)