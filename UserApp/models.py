from django.db import models
import os


class TeacherModel(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class TableModel(models.Model):
    name = models.ForeignKey(TeacherModel, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="uploads/teacher/", null=False)

    def __str__(self):
        return self.name


class CallTimes(models.Model):
    CHOICES = (
        ("Понедельник, Вторник, Среда, Суббота", "Понедельник, Вторник, Среда, Суббота"),
        ("Четверг", "Четверг"),
        ("Пятница","Пятница")
    )
    hafta_kuni = models.CharField(choices=CHOICES, max_length=225)
    time_photo = models.ImageField(upload_to="uploads/calltimes/")

    def __str__(self):
        return self.hafta_kuni
