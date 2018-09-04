from django.db import models
class user(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length = 32)
class user_info(models.Model):
     Name=models.CharField(max_length=200)
     Contact=models.CharField(max_length=200)
     Email=models.CharField(max_length=200)
     Lead_from=models.CharField(max_length=200)
     Called_by=models.CharField(max_length=200)
     Course=models.CharField(max_length=200)
     Interview_type=models.CharField(max_length=200)
     Education=models.CharField(max_length=200)
     Specialization=models.CharField(max_length=200)
     year_of_passing=models.IntegerField()
     fresher_experience=models.CharField(max_length=200)
     Time_in=models.TimeField()
     Time_out=models.TimeField()
class File(models.Model):

    filepath= models.FileField(upload_to='files/', null=False, verbose_name="")

def __str__(self):
        return str(self.filepath)

    # def __str__(self):
         #return self.Name
