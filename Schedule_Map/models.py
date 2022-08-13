from django.db import models

# Create your models here.
class Courses(models.Model):
    className = models.CharField(max_length=256)
    credits = models.IntegerField()
    grade = models.CharField(max_length=5)
    overview = models.CharField(max_length=1800)
    preReqs = models.CharField(max_length=1800)
    skippable = models.BooleanField()
    classType= models.CharField(max_length=128, default="Elective")#column that im trying to add
    def __str__(self):
        return f"{self.className}: Credits {self.credits} Grade {self.grade}"

class Optii(models.Model):
    crsName = models.CharField(max_length=1024)
    provider = models.CharField(max_length=1024)
    fullfillment = models.ForeignKey(Courses,on_delete=models.CASCADE,limit_choices_to={'skippable':True},related_name="crs",blank=True)
    testing = models.CharField(max_length=128, default="No Test Required")
    def __str__(self):
        return f"{self.crsName} is provided by {self.provider}"