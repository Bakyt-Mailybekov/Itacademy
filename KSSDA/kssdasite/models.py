from django.db import models
from django.utils import timezone

class Alumni(models.Model):
	first_name_alumni = models.CharField(max_length=32, primary_key=True, null=False)
	last_name_alumni = models.CharField(max_length=32)
	description_alumni = models.TextField(blank=True, null=True)
	email_alumni = models.EmailField(max_length=50, blank=True, null=True)
	phone_number_alumni = models.CharField(max_length=32, blank=True, null=True)
	github_link_alumni = models.URLField(blank=True, null=True)
	picture_alumni = models.ImageField(upload_to='', max_length=255, blank=True, null=True)

	def __str__(self):
		return self.last_name_alumni


class Project(models.Model):
	name_project = models.CharField(max_length=255, primary_key=True, null=False)
	description_project = models.TextField(blank=True, null=True)
	picture_project = models.ImageField(upload_to='', max_length=50, blank=True, null=True)
	#alumni_id = models.ForeignKey(Alumni, on_delete=CASCADE)

