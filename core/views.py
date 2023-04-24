from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import (Pessoa, Veiculo, MovMensalista, Mensalista, movRotativo)
from .forms import (PessoaForm, VeiculoForm, movRotativoForm, MensalistaForm, MovMensalistaForm)
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse

def home(request):
    # mensagem = "Olá mundo"
    return render(request, 'core/index.html') 

def logar(request):
    if request.method == "GET":
        return render(request, 'login.html') 
    
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = auth.authenticate(username=username, password=senha)

        if not user:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return render(request, 'login.html') 
        
        # messages.add_message(request, constants.SUCCESS, 'Válido')
        auth.login(request, user)
        return redirect(reverse('listar_pessoas')) 

@login_required
def listar_pessoas(request):
    pessoa = Pessoa.objects.all()
    form  = PessoaForm()
    data = {'pessoas' : pessoa, 'form': form}
    
    return render(request, 'core/listarPessoas.html', data) 

@login_required
def pessoa_nova(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save() 
        
    return redirect('listar_pessoas')

@login_required
def update_pessoa(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save() 
            return redirect('listar_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)

@login_required
def delete_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('listar_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'pessoa': pessoa})


@login_required
def listar_veiculos(request):
    veiculo = Veiculo.objects.all()
    form  = VeiculoForm()
    data = {'veiculos' : veiculo, 'form': form}
    
    return render(request, 'core/listarVeiculos.html', data) 

@login_required
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    return redirect('listar_veiculos')

@login_required
def update_veiculo(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save() 
            return redirect('listar_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)

@login_required
def delete_veiculo(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('listar_veiculos')
    else:
        return render(request, 'core/delete_veiculo.html', {'veiculo': veiculo})

@login_required
def listar_mov_rot(request):
    mov_rot = movRotativo.objects.all()
    form  = movRotativoForm()
    data = {'mov_rot' : mov_rot, 'form': form}
    
    return render(request, 'core/listarmov_rot.html', data) 

@login_required
def movrot_novo(request):
    form = movRotativoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        
    return redirect('listar_mov_rot')

@login_required
def update_mov_rot(request, id):
    data = {}
    mov_rot = movRotativo.objects.get(id=id)
    form = movRotativoForm(request.POST or None, instance=mov_rot)
    data['mov_rot'] = mov_rot
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save() 
            return redirect('listar_mov_rot')
    else:
        return render(request, 'core/update_mov_rot.html', data)

@login_required
def delete_mov_rot(request, id):
    mov_rot = movRotativo.objects.get(id=id)
    if request.method == 'POST':
        mov_rot.delete()
        return redirect('listar_mov_rot')
    else:
        return render(request, 'core/delete_mov_rot.html', {'mov_rot': mov_rot})

@login_required
def listar_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form  = MensalistaForm()
    data = {'mensalistas' : mensalistas, 'form': form}
    
    return render(request, 'core/listarmensalistas.html', data) 

@login_required
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        
    return redirect('listar_mensalistas')

@login_required
def update_mensalista(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save() 
            return redirect('listar_mensalistas')
    else:
        return render(request, 'core/update_mensalistas.html', data)

@login_required
def delete_mensalista(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('listar_mensalistas')
    else:
        return render(request, 'core/delete_mensalistas.html', {'mensalista': mensalista})

@login_required
def listar_mov_mensalistas(request):
    pessoas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'pessoas' : pessoas, 'form' : form}
    
    return render(request, 'core/listarmovmensalistas.html', data) 

@login_required
def movmen_novo(request):
    form = MovMensalistaForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        
    return redirect('listar_mov_mensalistas')

@login_required
def update_mov_men(request, id):
    data = {}
    mov_men = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=mov_men)
    data['mov_men'] = mov_men
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save() 
            return redirect('listar_mov_mensalistas')
    else:
        return render(request, 'core/update_mov_men.html', data)
    
@login_required
def delete_mov_men(request, id):
    mov_men = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        mov_men.delete()
        return redirect('listar_mov_mensalistas')
    else:
        return render(request, 'core/delete_mov_men.html', {'mov_men': mov_men})