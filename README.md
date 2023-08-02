# Django

      python manage.py runserver

## การสร้าง admin 
    python manage.py createsuperuser

## การสร้าง app_model
    python manage.py startapp

## การเริ่ม project ของ app_model
    python manage.py startproject
    
## การสร้าง models ใน app_model
``` python
from django.db import models

prefix_choices = (
    (1, "นาย"),
    (2, "นางสาว"),
    (3, "นาง"),
)


class Student(models.Model):
    std_id = models.IntegerField()
    prefix = models.IntegerField(choices=prefix_choices, default=1)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Student s"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("Student_detail", kwargs={"pk": self.pk})
 ```
