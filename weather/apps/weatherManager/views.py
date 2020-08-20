from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, generics
from weatherManager.serializers import UserSerializer, GroupSerializer, CitySerializer, TemperatureSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse
from .models import City, Temperature
from .filters import DateFilter
from django_filters import rest_framework as filters
import django_filters




class CityList(generics.ListCreateAPIView):
	model = City
	queryset = City.objects.all()
	serializer_class = CitySerializer


class CityDetail(APIView):

	def get_object(self, city_id):
		try:
			return City.objects.get(id = city_id)
		except City.DoesNotExist:
			raise Http404

	def get(self, request, city_id):
		city = self.get_object(city_id)
		serializer = CitySerializer(city)
		return Response(serializer.data)

	def update(self, request, city_id):
		city = self.get_object(city_id)
		serializer = CitySerializer(city, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(city.data)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def delete(self, request, city_id):
		city = self.get_object(city_id)
		city.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)







class TempList(generics.ListAPIView):
	serializer_class = TemperatureSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filterset_class = DateFilter

	def get_queryset(self):
		cityes_id = self.kwargs['cityes_id']
		return Temperature.objects.filter(cityes_id = cityes_id)

	def post(self, request, cityes_id):
		temperature = request.POST['temperature']
		date = request.POST['date']
		temp = Temperature.objects.create(cityes_id = cityes_id, temperature = temperature, date = date)
		serializer = TemperatureSerializer(Temperature.objects.filter(cityes_id = cityes_id))
		return Response('Temperature added!')



class TempDetail(generics.ListAPIView):
	serializer_class = TemperatureSerializer

	def get_object(self, city_id):
		try:
			return Temperature.objects.get(id = city_id)
		except Temperature.DoesNotExist:
			raise Http404

	def get(self, request, cityes_id, temp_id):
		temperature = self.get_object(temp_id)
		serializer = TemperatureSerializer(temperature)
		return Response(serializer.data)

	def put(self, request, temp_id, cityes_id):
		temp = self.get_object(temp_id)
		serializer = TemperatureSerializer(temp, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(temp)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def delete(self, request, temp_id, cityes_id):
		temp = self.get_object(temp_id)
		temp.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)




	





'''
Все что ниже было сделано для html шаблонов
'''
def index(request):
	cityes_list = City.objects.all()
	return render(request, 'weatherManager/list.html', {'cityes_list': cityes_list})


def detail(request, city_id):
	try:
		a = City.objects.get( id = city_id )
	except:
		raise Http404("Этот город пока отсутсвует в нашем списке, добавьте его!")
	temperature_data = a.temperature_set.order_by('-id')
	return render(request, 'weatherManager/detail.html', {'weather': a, 'temperature_data': temperature_data})


def add_temperature(request, city_id):
	try:
		a = City.objects.get( id = city_id )
	except:
		raise Http404("Этот город пока отсутсвует в нашем списке, добавьте его!")
	a.temperature_set.create(temperature = request.POST['temperature'], date = request.POST['date'])
	return HttpResponseRedirect( reverse('weatherManager:detail', args = (a.id,)) )


def add_city(request):
	if request.user.is_authenticated and request.user.groups.filter(name = 'Админ').exists():
		return render(request, 'weatherManager/add_city.html', {})
	else:
		return HttpResponse('Вы не авторизованы или имеете статус "Чмо" и не можете добавлять города(Сорян)')


def create_city(request):
	if request.method == 'POST':
		if City.objects.filter(city = request.POST['city']):
			return HttpResponse("Мы уже знаем про твой город, поищи его в списке <br><br><a href='/weather/'>Ищи здесь</a>")
		else:
			a = City(city = request.POST.get('city'))
			a.save()
			return HttpResponseRedirect(reverse('weatherManager:index',))


def filter_temperature(request, city_id):
	try:
		a = City.objects.get( id = city_id )
	except:
		raise Http404("Этот город пока отсутсвует в нашем списке, добавьте его!")

	if not request.POST['data_filter1'] and not request.POST['data_filter2'] and not request.POST['data_filter3']:
		return HttpResponseRedirect(reverse('weatherManager:detail', args = (a.id,)))

	elif request.POST['data_filter1']:
		b = Temperature.objects.filter(date = request.POST['data_filter1'])
		return render(request, 'weatherManager/detail.html', {'weather': a, 'filter1': b})

	elif request.POST['data_filter2'] and request.POST['data_filter3']:
		b = Temperature.objects.filter(date__range = (request.POST['data_filter2'], request.POST['data_filter3']))
		return render(request, 'weatherManager/detail.html', {'weather': a, 'filter1': b})

	elif request.POST['data_filter2'] and not request.POST['data_filter3'] or not request.POST['data_filter2'] and request.POST['data_filter3']:
		return HttpResponse("<h1>Ты думаешь что я тебя не переиграю, что я тебя не уничтожу?..</h1>")

def edit_temperature(request, temp_id):
	try:
		b = Temperature.objects.get( id = temp_id )
	except:
		raise Http404("Мы не знаем такой температуры и ты не можешь!!!")
	return render(request, 'weatherManager/edit_temperature.html', {'weather': b,})


def edit(request, temp_id):
	try:
		b = Temperature.objects.get( id = temp_id )
	except:
		raise Http404("Мы не знаем такой температуры и ты не можешь!!!")
	if request.method == 'POST':
		b.temperature = request.POST.get("temperature")
		b.save()
		return HttpResponseRedirect(reverse('weatherManager:index'))


