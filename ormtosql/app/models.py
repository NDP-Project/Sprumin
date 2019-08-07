from django.db import models


# Create your models here.
class User(models.Model):
	SEX = (
		('Male', 'MALE'),
		('Female', 'FEMALE')
	)

	idx = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64, null=True, blank=True)
	age = models.IntegerField(default=0)
	sex = models.CharField(choices=SEX, default="Male", max_length=8)
	info = models.TextField(default="")
	created_at = models.DateTimeField(auto_now_add=True)
