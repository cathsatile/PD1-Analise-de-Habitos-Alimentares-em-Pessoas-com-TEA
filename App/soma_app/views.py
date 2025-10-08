from django.shortcuts import render

# View para o Dashboard (Index)
def dashboard_index(request):
    # Aqui você passaria os dados do gráfico quando estiverem prontos.
    context = {} 
    return render(request, 'soma_app/dashboard.html', context)

# View para a página "Sobre Nós"
def sobre_nos(request):
    context = {}
    return render(request, 'soma_app/sobre_nos.html', context)

# View para a página "Sobre o SOMA"
def sobre_soma(request):
    context = {}
    return render(request, 'soma_app/sobre_soma.html', context)