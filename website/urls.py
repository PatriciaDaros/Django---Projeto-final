from django.urls import path
from .views import home, servico, contato, contatos

urlpatterns = [
    path('', home , name="website_home"),
    path('contato/', contato , name="contato"),
    path('contatos/', contatos , name="contatos"),
    path('servico/', servico , name="servico"),
]