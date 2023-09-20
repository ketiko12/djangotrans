from django import models

#create your models here
class Student(models.Model):
    name= models.CharField(max_length=70)
    email= models.EmailField(max_length=45)
    password= models.CharField(max_length=34)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})