from rest_framework import serializers

from hic.cita.models import Event, EventExtendedProp

# class EventExtendedPropSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EventExtendedProp
#         fields = '__all__'


class EventoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='titulo')
    start = serializers.DateTimeField(source='hora_inicio')
    end = serializers.DateTimeField(source='hora_fin')
    backgroundColor = serializers.CharField(source='color')
    class Meta:
        model = Event
        fields = ['title', 'start', 'end', 'backgroundColor', 'extendedProps']
        depth = 1
