from django.test import TestCase
from weatherManager.models import City, Temperature
from django.urls import reverse




class CityListViewTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		number_of_city = 13
		for city_num in range(number_of_city):
			City.objects.create(city = 'Pyatigorsk %s' % city_num)

	def test_view_url_exists_at_desired_location(self): 
		resp = self.client.get('/city/') 
		self.assertEqual(resp.status_code, 200)


class TemperatureListViewTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		number_of_city = 13
		for city_num in range(number_of_city):
			City.objects.create(city = 'Pyatigorsk %s' % city_num)

	def test_view_url_exists_at_desired_location(self): 
		resp = self.client.get('/temperature/1/') 
		self.assertEqual(resp.status_code, 200)

