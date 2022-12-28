from django.db import models

# Create your models here.


class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=50)
    course_ratings = models.FloatField(default=0)
    course_reviews = models.CharField(max_length=2000, blank=True)


    def __str__(self):
        return self.course_name


class Students(models.Model):
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=250)
    course_enrolled = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name

