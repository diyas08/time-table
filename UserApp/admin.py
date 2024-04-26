from django.contrib import admin
from .models import TeacherModel, TableModel, CallTimes

admin.site.register(TeacherModel)
admin.site.register(TableModel)
admin.site.register(CallTimes)
