from django.db import models

# Create your models here.

class Manager(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
	return self.name
   
class Group(models.Model):
    name = models.CharField(max_length=200) 
    def __unicode__(self):
	return self.name

class Employee(models.Model):
    name = models.CharField(max_length=200)
    manager = models.ForeignKey(Manager);
    start_date = models.DateField('date joined')
    end_date = models.DateField(null=True)
    group  = models.ForeignKey(Group)

    def __unicode__(self):
	return self.name

class Activity(models.Model):
    name = models.CharField(max_length=200)
    colour = models.CharField(max_length=20)
    def __unicode__(self):
	return self.name

class Schedule(models.Model):
    day = models.DateField('date started')
    employee = models.ForeignKey(Employee)
    activity = models.ForeignKey(Activity)
	
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
