from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from .models import *

# Create your views here.

def cadastrar_carros(request, template_name='carro_form.html'):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('carro_list')
    return render(request, template_name, {'form': form})

def listar_carros(request, template_name='carro_list.html'):
    query = request.GET.get('busca')
    if query:
        carro = CarroModel.objects.filter(modelo__icontains=query)
    else:
        carro = CarroModel.objects.all()
    return render(request, template_name, {'carros': carro})

def editar_carro(request, pk, template_name='carro_form.html'):
    carro = CarroModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('carro_list')
    else:
        form = CarroForm(instance=carro)
    return render(request, template_name, {'form': form})

def delete_carro(request, pk, template_name='carro_delete.html'):
    carro = CarroModel.objects.get(pk=pk)
    if request.method == 'POST':
        carro.delete()
        return redirect('carro_list')
    return render(request, template_name, {'form': carro})