from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from menu.models import Menu, Post
from menu.serializers import MenuSerializer

class MenuView(ListView):
    model = Menu
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MenuView, self).get_context_data(*args, **kwargs)
        context['menu_view'] = self.model.objects.all()
        return context

class MenuViewDetail(DetailView):
    """
    Детализация статей.
    """
    model = Menu
    template = 'content.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(MenuViewDetail, self).get_context_data(*args, **kwargs)
        slug = self.kwargs['slug'].split('/')
        t_id = self.get_object().pk
        context['menu_view'] = self.model.objects.all()
        context['instance'] = Post.objects.filter(id=t_id)
        return context

class MenuApiView(APIView): 
    """
    APIView для сериализованных данных категорий меню. 
    """
    model = Menu
    
    def get(self, request):
        menu_item  = self.model.objects.root_nodes() # собираем корешки
        serializer = MenuSerializer(menu_item, many=True) # собираем сериализацию через экземпляр
        return Response({'data': serializer.data}) # отправляем на клиент json




