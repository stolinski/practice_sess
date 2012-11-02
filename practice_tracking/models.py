from django.db import models
from django.contrib.auth.models import User

# What type of move (footwork, combo, power...)
class MoveClass(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name

class ParentMove(models.Model):
	name = models.CharField(max_length=30)
	move_classification = models.ForeignKey(MoveClass)

	def __unicode__(self):
		return self.name

# Create your models here.
class Move(models.Model):
	name = models.CharField(max_length=60)
	value = models.PositiveIntegerField()
	parent = models.ManyToManyField(ParentMove)
	move_classification = models.ForeignKey(MoveClass)
 
	def __unicode__(self):
		return self.name

class Sesh(models.Model):
	date = models.DateField()
	moves = models.ManyToManyField(Move)

	def __unicode__(self):
		return self.name

class UserProfile(models.Model):
	#connects to user
	user = models.OneToOneField(User)

	#extra fields for user
	value = models.PositiveIntegerField(default=0)
	moves = models.ManyToManyField(Move)
	bboyname = models.CharField(max_length=30)
	crew = models.CharField(max_length=30)
    
	def __unicode__(self):
		return self.name
    