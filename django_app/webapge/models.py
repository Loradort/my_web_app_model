from django.db import models

# Create your models here.
prefix_chioces = (
    (1, "นาย"),
    (2, "นางสาว"),
    (3, "นาง"),
)

class Student(models.Model):
    prefix_chioces = models.IntegerField(choices=prefix_chioces, default=1)
    std_id = models.IntegerField()
    name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)
    phone = models.CharField(max_length= 15)
    adress = models.TextField()


    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Student s"

    def __str__(self):
        return self.name + " " + self.last_name

