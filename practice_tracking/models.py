from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Move(models.Model):
	name = models.CharField(max_length=60)
	value = models.PositiveIntegerField()
	parent = models.ForeignKey('ParentMove')
	move_classification = models.ForeignKey('MoveClass')

class ParentMove(models.Model):
	name = models.CharField(max_length=30)
	move_classification = models.ForeignKey('MoveClass')


class Sesh(models.Model):
	date = models.DateField()
	moves = models.ManyToManyField('Move')


class UserProfile(models.Model):
	#connects to user
	user = models.OneToOneField(User)

	#extra fields for user
	value = models.PositiveIntegerField(default=0)
	moves = models.ManyToManyField('Move')
	bboyname = models.CharField(max_length=30)
	crew = models.CharField(max_length=30)

# What type of move (footwork, combo, power...)
class MoveClass(models.Model):
	name = models.CharField(max_length=30)
    