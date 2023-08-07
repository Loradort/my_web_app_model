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
## 📕6. [views.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/views.py) 

>**❗️ พื้นที่สำหรับการ functions ต่างๆไปยัง ทั้งในส่วนของการเรียกใช้ [template](https://github.com/Lynnn01/MyWebappModel/tree/main/templates) และการสร้าง functions ต่างๆ เพื่อใช้ในการเรียกใช้งาน โดยจะมีการเรียกใช้จาก [urls.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/urls.py)**

```py
from django.shortcuts import render
from . import models

def Home(request):
    context = {}
    students = models.Student.objects.all().order_by("-id")

    for student in students:
        student.prefix_str = getModelChoice(student.prefix, models.prefix_choices)

    context["students"] = students

    return render(request, "index.html", context)

def About(request):
    return render(request, "about.html")

def Contact(request):
    return render(request, "contact.html")
```

>**🔺 functions ที่มีการเรียกใช้ style จาก [template](https://github.com/Lynnn01/MyWebappModel/tree/main/templates) แล้วจะมีใช้ return เพื่อส่งออกค่า ซึ่งในส่วนนี้จะมีการเรียกใช้งานจาก [urls.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/urls.py)**


>**🔻 StudentDetails เป็น function ที่จะถูกเรียกใช้จาก [urls.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/urls.py) ในส่วนแรก และมีการส่งค่าไปยัง [details.html](https://github.com/Lynnn01/MyWebappModel/blob/main/templates/details.html) เป็นส่วนต่อไป**

```py
def StudentDetails(request, id):
    context = {}
    students = models.Student.objects.filter(id=id)
    for student in students:
        student.prefix_str = getModelChoice(student.prefix, models.prefix_choices)
        context["student"] = student
    return render(request, "details.html", context)
```
>**🔺 จุดสังเกตุที่เห็นได้ชัดของ functions นี้คือมีการใช้ filter ในการค้นหาข้อมูลในส่วนของ ID และมีการใช้ functions getModelChoice เพื่อการเปลี่ยนค่า prefix จากตัวเลข เป็นตัวอักษร**

>**🔻 getModelChoice เป็น function เพื่อใช้ในการเปลี่ยนค่า prefix จากตัวเลข เป็นตัวอักษร ซึ่งค่าของ prefix นั้นจะถูกดึงข้อมูลมาจาก [model.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/models.py)**

```py
def getModelChoice(num, choices):
    for choice in choices:
        if choice[0] == num:
            return choice[1]
```
>**🔺 จุดสังเกตุที่เห็นได้ชัดของ function นี้คือมีการใช้ for loop ในการวนซ้ำ และใช้ if เพื่อเช็คข้อมูลของ prefix ที่เป็นตัวเลขทีละค่า จากนั้นจะมีการใช้ return เพื่อส่งข้อมูลของ prefix ที่เป็นตัวอักษรออกไป**

## 📕7. [model.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/models.py)
>**❗️ การสร้างตารางสำหรับการเก็บข้อมูลบนพื้นฐานของ db.sqlite3**

```py
from  django.db  import  models

prefix_choices  = (

(1, "นาย"),

(2, "นางสาว"),

(3, "นาง"),

)
```
>**🔺 prefix_choices จะมีการเก็บค่าข้อมูลในตารางแบบตัวเลขจาก pointer ที่ 0 แต่หลังจาก function getModelChoice มีการดึงค่าไปใช้ จะกระบวนการที่จะดึงค่าจาก pointer ที่ 1 มาใช้แทน**

```py
class  Student(models.Model):

	std_id  =  models.IntegerField()

	prefix  =  models.IntegerField(choices=prefix_choices, default=1)

	name  =  models.CharField(max_length=255)

	lastname  =  models.CharField(max_length=255)

	phone  =  models.CharField(max_length=15)

	address  =  models.TextField()


	class  Meta:

	verbose_name  =  "Student"

	verbose_name_plural  =  "Students"


	def  __str__(self):

	return  self.name


	def  get_absolute_url(self):

	return  reversed("Student_detail", kwargs={"pk": self.pk})
```
>**🔺 Clss Student เพื่อใช้เก็บข้อมูลเกี่ยวกับนักศึกษา**

```py
class Major(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Major"
        verbose_name_plural = "Majors"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("Major_detail", kwargs={"pk": self.pk})
```
>**🔺 Clss Major ใช้สำหรับเก็บข้อมูลคณะของนักศึกษา**

## 📕8. [urls.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/urls.py)

```py
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home, name='home'),
    path('about',views.About,   name='about'),
    path('contact',views.Contact,   name='contact'),
    path('details/<int:id>', views.StudentDetails, name='details'),
]
```