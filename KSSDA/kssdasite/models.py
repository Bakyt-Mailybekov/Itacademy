from django.db import models
from django.utils import timezone

class Year(models.Model):
	YEAR_CHOICES = (
		('2016-2017', '2016-2017'),
		('2017-2018', '2017-2018'),
		('2018-2019', '2018-2019'),
		('2019-2020', '2019-2020'),
	)
	year = models.CharField(max_length=50, choices = YEAR_CHOICES)

	def __str__(self):
		return self.year


class Language(models.Model):
	name_language = models.CharField(max_length=50, primary_key=True, null=False)
	year_language = models.ForeignKey(Year, on_delete=models.CASCADE)

	def __str__(self):
		return self.name_language


class Project(models.Model):
	name_project = models.CharField(max_length=255, primary_key=True, null=False)
	description_project = models.TextField(blank=True, null=True)
	picture_project = models.ImageField(upload_to='', max_length=50, blank=True, null=True)
	year_project = models.ForeignKey(Year, default="", on_delete=models.CASCADE)
	language_project = models.ForeignKey(Language, default="", on_delete=models.CASCADE)

	def __str__(self):
		return self.name_project



class Alumni(models.Model):
	class Meta:
		verbose_name_plural = 'Alumni'
	first_name_alumni = models.CharField(max_length=32, primary_key=True, null=False)
	last_name_alumni = models.CharField(max_length=32)
	picture_alumni = models.ImageField(upload_to='', max_length=255, blank=True, null=True)
	description_alumni = models.TextField(blank=True, null=True)
	email_alumni = models.EmailField(max_length=50, blank=True, null=True)
	phone_number_alumni = models.CharField(max_length=32, blank=True, null=True)
	github_link_alumni = models.URLField(blank=True, null=True)
	cv_alumni = models.FileField(upload_to='docs/', default="")
	project_alumni = models.ForeignKey(Project, default="", on_delete=models.CASCADE)


	def __str__(self):
		return self.first_name_alumni + " " + self.last_name_alumni


