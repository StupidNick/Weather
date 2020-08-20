from django.test import TestCase

from weatherManager.models import City, Temperature


class CityModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        City.objects.create(city = 'Boston')

    def test_city_label(self):
        city = City.objects.get(id = 1)
        name_city = city._meta.get_field('city').verbose_name
        self.assertEquals(name_city, 'Город')

    def test_city_max_length(self):
        city = City.objects.get(id = 1)
        max_length = city._meta.get_field('city').max_length
        self.assertEquals(max_length, 50)




class TemperatureModelTest(TestCase):

    @classmethod
    def setUp(self):
        Temperature.objects.create(id = 1, temperature = '22', date = '2020-05-05', cityes_id = '1')
        print("setUpTestData: Run once to set up non-modified data for all class methods.")

    def tearDown(self):
        Temperature.objects.get(id = 1).delete()

    def test_temperature_label(self):
        temperature = Temperature.objects.get(id = 1)
        temperature_data = temperature._meta.get_field('temperature').verbose_name
        self.assertEquals(temperature_data, 'Температура')

    def test_temperature_max_length(self):
        temperature = Temperature.objects.get(id = 1)
        max_length = temperature._meta.get_field('temperature').max_length
        self.assertEquals(max_length, 2)


