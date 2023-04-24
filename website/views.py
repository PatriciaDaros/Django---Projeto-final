from django.shortcuts import render
from .models import contato

def home(request):
    return render(request, 'website/index.html')

def contato_ol(request):
    # if request.method == "POST":
    #     # email = request.POST.get('email')
    #     nome = request.POST.get('nome')
    #     sobrenome = request.POST.get('sobrenome')
    #     # mensagem = request.POST.get('mensagem')
    #     # recebernoticias = True if request.POST.get('recebernoticias') == 'on' else 'false'
        
    #     Contato = contato(
    #         # email = request.email,
    #         nome = request.nome,
    #         sobrenome = request.sobrenome,
    #         # mensagem = request.mensagem,
    #         # recebernoticias = request.recebernoticias,
    #     )
        
    #     Contato.save()
    #     mensagem = 'Contato realizado com sucesso'
        
    # else:
    #     mensagem = ''
    
    return render(request, 'website/contato.html')

def contato(request):
    email = request.POST.get('email')
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    mensagem = request.POST.get('inputAssunto')
    recebernoticias = request.POST.get('recebernoticias')
    
    print(email)
    print(nome)
    print(sobrenome)
    print(mensagem)
    print(recebernoticias)
    
    return render(request, 'website/contato.html')

def contatos_old(request):
    if request.method == "GET":
        return render(request, 'website/contatos.html')

    if request.method == "POST":
        try:
            Contato_dic = {}
            
            Contato_dic['email'] = request.POST.get('email')
            Contato_dic['nome'] = request.POST.get('nome')
            Contato_dic['sobrenome'] = request.POST.get('sobrenome')
            Contato_dic['mensagem'] = request.POST.get('mensagem')
            Contato_dic['recebernoticias'] = True if request.POST.get('recebernoticias') == 'on' else False
            
            Contato_dic.objects.create(**contato)
            
        except Exception as e:
            info = str(e)
        else:
            info = 'Contato salvo com sucesso'
            
        return render(request, 'website/contatos.html', {'info': info})
        

def contatos(request):
    if request.method == "GET":
        return render(request, 'website/contatos.html')

    if request.method == "POST":
            
        # email = request.POST.get('email')
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        mensagem = request.POST.get('mensagem')
        # recebernoticias = True if request.POST.get('recebernoticias') == 'on' else False

        Contato = contato(
            nome = nome,
            sobrenome = sobrenome,
            mensagem = mensagem
            # recebernoticias = recebernoticias,
            # email = email,
        )
        
        Contato.save()
        
        # info = 'Cadastro Realizado com sucesso'
            
    return render(request, 'website/contatos.html')
        

def servico(request):
    return render(request, 'website/servico.html')