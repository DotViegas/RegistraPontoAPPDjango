from django.shortcuts import render

def index(request):
    return render(request, "meuapp/index.html")

def cadastro_de_empresa(request):
    return render(request, "meuapp/cadastro_de_empresa.html")

def cadastro_de_cargos(request):
    return render(request, "meuapp/cadastro_de_cargos.html")

def cadastro_de_colaborador(request):
    return render(request, "meuapp/cadastro_de_colaborador.html")

def jornada_de_trabalho(request):
    return render(request, "meuapp/jornada_de_trabalho.html")

def verificar_registro_de_ponto(request):
    return render(request, "meuapp/verificar_registro_de_ponto.html")

def relatorio_de_ponto(request):
    return render(request, "meuapp/relatorio_de_ponto.html")

def calculo_folha_de_pagamento(request):
    return render(request, "meuapp/calculo_folha_de_pagamento.html")

def folha_de_pagamento(request):
    return render(request, "meuapp/folha_de_pagamento.html")

def ferias(request):
    return render(request, "meuapp/ferias.html")