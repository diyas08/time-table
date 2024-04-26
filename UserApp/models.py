from django.db import models
import os


class TeacherModel(models.Model):
    FIO_Teacher = models.CharField(max_length=15)

    def __str__(self):
        return self.FIO_Teacher


class TeacherTableModel(models.Model):
    FIO_Teacher = models.CharField(max_length=15)
    photo = models.ImageField(upload_to="uploads/teacher/", null=True)

    # class_number = models.IntegerField()
    # type_choise = (
    #     ("А", "A"),
    #     ("Б", "Б"),
    #     ("В", "В"),
    #     ("Г", "Г"),
    #     ("Д", "Д"),
    #     ("Е", "Е"),
    # )
    # class_type = models.CharField(choices=type_choise, max_length=225)

    def __str__(self):
        return self.FIO_Teacher


class StudentsTable(models.Model):
    class_number = models.IntegerField()
    type_choise = (
        ("А", "A"),
        ("Б", "Б"),
        ("В", "В"),
        ("Г", "Г"),
        ("Д", "Д"),
        ("Е", "Е"),
    )
    class_type = models.CharField(choices=type_choise, max_length=225)
    table_photo = models.ImageField(upload_to="uploads/students/")

    def __str__(self):
        return "{} {}".format(self.class_number, self.class_type)


class CallTimesModel(models.Model):
    CHOICES = (
        ("Понедельник, Вторник, Среда, Суббота", "Понедельник, Вторник, Среда, Суббота"),
        ("Четверг", "Четверг"),
        ("Пятница", "Пятница")
    )
    hafta_kuni = models.CharField(choices=CHOICES, max_length=225)
    time_photo = models.ImageField(upload_to="uploads/calltimes/")

    def __str__(self):
        return self.hafta_kuni

# class ClassNameModel(models.Model):
#     CHOICES_class = (
#         ("1 class", "1 class"),
#         ("2 class", "2 class"),
#         ("3 class", "3 class"),
#         ("4 class", "4 class"),
#         ("5 class", "5 class"),
#         ("6 class", "6 class"),
#         ("7 class", "7 class"),
#         ("8 class", "8 class"),
#         ("9 class", "9 class"),
#         ("10 class", "10 class"),
#         ("11 class", "11 class"),
#     )
#     nameclass = models.CharField(choices=CHOICES_class, max_length=30)
#     class_student = models.CharField(max_length=225)
#
#     def __str__(self):
#         return self.nameclass
#
#
# class StudentsTable(models.Model):
#     nameclass = models.ForeignKey(ClassNameModel, on_delete=models.CASCADE)
#     # class_student = models.ForeignKey(ClassNameModel, on_delete=models.CASCADE)
