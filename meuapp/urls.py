from django.urls import path
from meuapp.views import index, cadastro_de_empresa, cadastro_de_cargos, cadastro_de_colaborador, jornada_de_trabalho, verificar_registro_de_ponto, relatorio_de_ponto, calculo_folha_de_pagamento, folha_de_pagamento, ferias

urlpatterns = [
    path('', index, name='index'),
    path('cadastro_de_empresa/', cadastro_de_empresa, name="cadastro_de_empresa"),
    path('cadastro_de_cargos/', cadastro_de_cargos, name='cadastro_de_cargos'),
    path('cadastro_de_colaborador/', cadastro_de_colaborador, name='cadastro_de_colaborador'),
    path('jornada_de_trabalho/', jornada_de_trabalho, name='jornada_de_trabalho'),
    path('verificar_registro_de_ponto/', verificar_registro_de_ponto, name='verificar_registro_de_ponto'),
    path('relatorio_de_ponto/', relatorio_de_ponto, name='relatorio_de_ponto'),
    path('calculo_folha_de_pagamento/', calculo_folha_de_pagamento, name='calculo_folha_de_pagamento'),
    path('folha_de_pagamento/', folha_de_pagamento, name='folha_de_pagamento'),
    path('ferias/', ferias, name='ferias'),
]