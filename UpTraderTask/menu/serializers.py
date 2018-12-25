from menu.models import Menu, Option
from rest_framework import  serializers
from rest_framework_recursive.fields import RecursiveField 


class OptionSerializer(serializers.ModelSerializer):
    """
    Инкапсулируем id и названия опций.
    """
    class Meta:
        model = Option
        fields = ['checked', 'expanded']

class MenuSerializer(serializers.ModelSerializer):
    """
    Сериализуем дерево наследовательности всех записей модели Menu
    через поле RecursiveField
    """
    children = RecursiveField(many=True, read_only=True)
    state = OptionSerializer() # вызываем сериализованные параметры state
    
    class Meta:
        model = Menu
        depth = 10
        fields = [
            'name',
            'slug',
            'state',
            'children',
        ]

