from django.db import models
from django.utils import timezone

class Project(models.Model):
    id=models.IntegerField(primary_key=True)
    project_name=models.CharField(max_length=100)
    text=models.TextField(max_length=256)
    translated_to_language=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True,db_index=True)
    updated_at = models.DateTimeField(db_index=True, auto_now=True)
    class Meta:
        verbose_name='Project'
        verbose_name_plural='Project'
        db_table='Projects'
class Order(models.Model):
    option=(
        ("new","New"),
        (" in-process","In-Process"),
        ("complete","Complete")
    )
    id=models.IntegerField(primary_key=True)
    project_id=models.ForeignKey(Project,on_delete=models.CASCADE)
    status=models.CharField(choices=option,default='new',max_length=100)
    translated_tex=models.CharField(max_length=200)
    created_at = models.DateTimeField( auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(db_index=True, auto_now=True)
    class Meta:
        verbose_name='Order'
        verbose_name_plural='Order'




class Register(models.Model):
    id=models.IntegerField(primary_key=True)
    firstname=models.CharField(max_length=200)
    latname = models.EmailField(max_length=200)
    email = models.CharField(max_length=30)
    username=models.CharField(max_length=100,blank=True,null=True)
    date_of_birth=models.DateField(max_length=20)
    mobile_number=models.BigIntegerField()
    password=models.CharField(max_length=20)

