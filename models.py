from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
#create your user model here

class UserAccount(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    balance= models.DecimalField(max_digits=32, decimal_places=16)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class Transfer(models.Model):
    initiated_by= models.ForeignKey(User, on_delete=models.CASCADE, related_name="initiated transaction")
    transfer_to= models.ForeignKey(User,on_delete=models.CASCADE, related_name="received transfer")
    amount= models.DecimalField(max_digits=32, decimal_places=16)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


class Venue(models.Model):
    name=models.CharField('Venue name'max_length=120)
    address=models.charField(max_length=120)
    zip_code=models.charField('Zip code', max_length=30)
    phone=models.CharField('Contact phone',max_length=20)
    web= models.URLField('Website Address')
    email_address= models.EmailField('Email address')









class Event(models.Model):
    name= models.CharField('Event Name', max_length=120)
    event_date= models.DateTimeField('Event Date')
    venue=  models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)#now these two tables are connected so that when we call
    manager= models.CharField('Event Name', max_length=120)  #Event.venue, and this will make us available all the information about Venue.
                                                             #When we call Event.venue.zip_code, it will give us zip_code from Venue table
    description= models.TextField(blank=False)
    attendees= models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name

class MyClubUser(models.Model):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    email= models.EmailField('User email')

    def __str__(self):
      return self.first_name + '' +self.last_name+''+self.email
    
