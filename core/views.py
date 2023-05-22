from django.shortcuts import render, redirect
from .models import Pessoa

def home(request):
    pessoa = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas":pessoa})

def salvar(request):
    vnome = request.POST.get("nome")
    Pessoa.objects.create(nome=vnome)
    pessoa = Pessoa.objects.all()
    return render (request, "index.html", {"pessoas":pessoa})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render (request, "update.html", {"pessoas":pessoa})

def update(request, id):
    vnome = request.POST.get("nome")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = vnome
    pessoa.save()
    return redirect (home)

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect (home)