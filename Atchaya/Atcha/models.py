


from django.db import models
from django.contrib import admin
class Football (models.Model):
    name=models.CharField(max_length=15)
    age=models.IntegerField()
    dob=models.DateField()
    score=models.IntegerField()
    no_of_goals=models.IntegerField()
    no_of_teams=models.IntegerField()
class FootballAdmin(admin.ModelAdmin):
    list_display=["name","age","dob","score","no_of_goals","no_of_teams"]


