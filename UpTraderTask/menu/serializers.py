from menu.models import Menu, Option
from rest_framework import  serializers
from rest_framework_recursive.fields import RecursiveField 


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['checked', 'expanded']

class MenuSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True, read_only=True)
    state = OptionSerializer()
    
    class Meta:
        model = Menu
        depth = 10
        fields = [
            'name',
            'slug',
            'state',
            'children',
        ]

