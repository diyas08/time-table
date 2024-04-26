from django.contrib import admin
from .models import TeacherModel, StudentsTable, TeacherTableModel, CallTimesModel

admin.site.register(TeacherModel)
admin.site.register(StudentsTable)
admin.site.register(TeacherTableModel)
admin.site.register(CallTimesModel)
