from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 🚨 Esta linha usa o nome 'soma_app' (nome do seu app), não 'SOMA'.
    # Isso direciona o tráfego da URL base para o seu aplicativo.
    path('', include('soma_app.urls')),
]