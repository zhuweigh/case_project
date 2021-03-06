from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django.core.urlresolvers import reverse
from django.utils import timezone
from parler.models import TranslatableModel, TranslatedFields
#class Content(models.Model):
class Content(models.Model):
	SEX_CHOICE = (
		('女','FM'),
		('男','M'),	
	)
	title = models.CharField(verbose_name='医院',max_length=30)
	sex = models.CharField(choices=SEX_CHOICE,max_length=20)
	age = models.CharField(max_length=2)
	name = models.CharField(max_length=10,verbose_name='姓名')
	date_of_birth = models.DateField(verbose_name='生日')
	job = models.CharField(max_length=20,verbose_name='职业')
	address = models.CharField(verbose_name='住址或单位',max_length=40)
	description = models.TextField()
	result = models.CharField(max_length=3)
	doctor = models.CharField(max_length=20,verbose_name='主治医师')
	#created = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name 
	def get_absolute_url(self):
		return reverse('case:case_detail',args=[self.id])		
	def get_id(self):
		return reverse('case:show_pdf',args=[self.id])
