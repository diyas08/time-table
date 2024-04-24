from rest_framework import serializers
from .models import TeacherModel, TableModel


class TeacherSRL(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = "__all__"


class StudentSrl(serializers.ModelSerializer):
    class Meta:
        model = TableModel
        fields = "__all__"



