from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class YoutubeVideos(models.Model):

	title = models.CharField(max_length=60)
	link = models.CharField(max_length=300)
	def __str__(self):
		return self.title
class AboutGuitar(models.Model):
	title = models.CharField(max_length=60)
	overview = models.TextField(blank=True)
	image = models.ImageField(upload_to='guitar', blank=True)
	def __str__(self):
		return self.title

class Batches(models.Model):
	batch_name = models.CharField(max_length=60)
	batch_datetime = models.DateTimeField()
	CATEGORY_DAYS = (('Monday','Monday',), ('Tuesday','Tuesday'), ('Wednesday','Wednesday'), ('Thursday','Thursday'), ('Friday','Friday'), ('Saturday','Saturday'), ('Sunday','Sunday'))
   	
	days = models.CharField(max_length=15, choices=CATEGORY_DAYS) 
	details = models.CharField(max_length=60)
	def __str__(self):
		return self.batch_name

class Feestructure(models.Model):
	Programmes_name = models.CharField(max_length=50)
	Days_per_week = models.CharField(max_length=50)
	Class_duration = models.CharField(max_length=50)
	fees = models.CharField(max_length=50)
	CATEGORY_Certification = (('Yes','Yes',), ('No','No'))
	certification = models.CharField(max_length=15, choices=CATEGORY_Certification)
	def __str__(self):
		return self.Programmes_name

class Buyguitar(models.Model):

	title = models.CharField(max_length=60)
	amount = models.CharField(max_length=60)
	details = models.CharField(max_length=60)
	overview = models.TextField(blank=True)
	image = models.ImageField(upload_to='guitar', blank=True)
	def __str__(self):
		return self.title
		
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField('date published')
    def __str__(self):
    	return self.title