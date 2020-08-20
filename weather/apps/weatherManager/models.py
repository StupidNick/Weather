from django.db import models


class City(models.Model):
	city = models.CharField('Город', max_length = 50)

	def __str__(self):
		return self.city

	class Meta:
		verbose_name = 'Город'
		verbose_name_plural = 'Города'


class Temperature(models.Model):
	cityes = models.ForeignKey(City, related_name = 'City', on_delete = models.CASCADE)
	temperature = models.CharField('Температура', max_length = 2)
	date = models.DateField('Дата')
	
	def __str__(self):
		return self.temperature

	class Meta:
		verbose_name = 'Температура'
		verbose_name_plural = 'Температура'


