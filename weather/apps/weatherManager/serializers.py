from rest_framework import serializers
from .models import City, Temperature
from django.contrib.auth.models import User, Group




class CitySerializer(serializers.ModelSerializer):  
    class Meta:
        model = City
        fields = ('id', 'city')

    def create(self, validated_data):
    	return City.objects.create(**validated_data)

    def update(self, instance, validated_data):
    	instance.city = validated_data.get('city', instance.city)
    	instance.save()
    	return instance


class TemperatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Temperature
        fields = ('id', 'temperature', 'date', 'cityes_id')

    def create(self, validated_data):
        # view = self.context.get('view')
        # cityes_id = view.kwargs['cityes_id'] if view else None
        # if not cityes_id:
        #     raise NotFound('City with given id does not exist.')
        # temperature = Temperature.objects.create(temperature=Temperature.objects.get(cityes_id=cityes_id), **validated_data)
        # return temperature

        # temperature = validated_data['temperature']
        # date = validated_data['date']
        # cityes_id = Temperature.objects.get(cityes_id = cityes_id)
        # return Temperature.objects.create(cityes_id = cityes_id, date = date, temperature = temperature)
        temperature = Temperature.objects.get(cityes_id = cityes_id)
        Temperature.save()
        return Temperature.objects.create(cityes_id = cityes_id)



    def update(self, instance, validated_data):
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.save()
        return instance





class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')



		