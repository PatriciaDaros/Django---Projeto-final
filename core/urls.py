from django.urls import path, include

from .views import (home, 
                    listar_pessoas, 
                    listar_veiculos, 
                    listar_mov_rot, 
                    listar_mensalistas, 
                    listar_mov_mensalistas, 
                    pessoa_nova,
                    veiculo_novo,
                    movmen_novo,
                    movrot_novo,
                    mensalista_novo,
                    update_pessoa,
                    update_mov_rot,
                    update_veiculo,
                    update_mov_men,
                    update_mensalista,
                    delete_pessoa,
                    delete_veiculo,
                    delete_mov_rot,
                    delete_mov_men,
                    delete_mensalista,
                    logar,
                    )


urlpatterns = [
    path('', home, name='home'),  
    path('logar/', logar, name='logar'),  
    
    path('listar_pessoas', listar_pessoas, name='listar_pessoas'),  
    path('listar_veiculos', listar_veiculos, name='listar_veiculos'), 
    path('listar_mov_rot', listar_mov_rot, name='listar_mov_rot'), 
    path('listar_mensalistas', listar_mensalistas, name='listar_mensalistas'), 
    path('listar_mov_mensalistas', listar_mov_mensalistas, name='listar_mov_mensalistas'),   
    
    path('pessoa_nova', pessoa_nova, name='pessoa_nova'),  
    path('veiculo_novo', veiculo_novo, name='veiculo_novo'),    
    path('movmen_novo', movmen_novo, name='movmen_novo'),  
    path('movrot_novo', movrot_novo, name='movrot_novo'), 
    path('mensalista_novo', mensalista_novo, name='mensalista_novo'),  

    path('update_pessoa/<int:id>', update_pessoa, name='update_pessoa'), 
    path('update_veiculo/<int:id>', update_veiculo, name='update_veiculo'), 
    path('update_mov_rot/<int:id>', update_mov_rot, name='update_mov_rot'), 
    path('update_mov_men/<int:id>', update_mov_men, name='update_mov_men'), 
    path('update_mensalista/<int:id>', update_mensalista, name='update_mensalista'), 

    path('delete_pessoa/<int:id>', delete_pessoa, name='delete_pessoa'), 
    path('delete_veiculo/<int:id>', delete_veiculo, name='delete_veiculo'), 
    path('delete_mov_rot/<int:id>', delete_mov_rot, name='delete_mov_rot'), 
    path('delete_mov_men/<int:id>', delete_mov_men, name='delete_mov_men'), 
    path('delete_mensalista/<int:id>', delete_mensalista, name='delete_mensalista'), 

]