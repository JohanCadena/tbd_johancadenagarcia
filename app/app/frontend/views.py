from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Articulo, Categoria


# Create your views here.
class IndexView(TemplateView):
    model = Articulo
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Articulos'
        context['articuloList'] = Articulo.objects.all()
        return context       

class TelefoniaView(TemplateView):
    model = Articulo
    template_name = 'telefonia.html'

    def get_context_data(self, **kwargs):
        context = super(TelefoniaView, self).get_context_data(**kwargs)
        context['title'] = 'Articulos'
        context['articuloList'] = Articulo.objects.all()
        return context  