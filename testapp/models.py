from django.db import models
 
class Password(models.Model):
    password = models.CharField(max_length=100)
    login = models.OneToOneField('Login')
 
    class Meta:
        db_table = 'passwords'
  
class Login(models.Model):
    login = models.CharField(max_length=100, unique=True)
 
    class Meta:
        db_table = 'logins'
 
gender = (
    ('m', 'man'),
    ('w', 'woman'),
)
 
class CustomUser(models.Model):
    login = models.OneToOneField(Login)
    password = models.OneToOneField(Password)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=5, choices=gender)
 
    class Meta:
        db_table = 'custom_user'
 
class Achievement(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField(blank=True)
    login = models.ForeignKey(Login)
 
    class Meta:
        db_table = 'achievement'