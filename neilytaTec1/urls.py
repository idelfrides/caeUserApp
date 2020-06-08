"""neilytaTec1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from app_saada_ong.views import home
from app_saada_ong.views import listagem
from app_saada_ong.views import listarProf
from app_saada_ong.views import listarAlunos
from app_saada_ong.views import showProjeto
from app_saada_ong.views import listAllNews
from app_saada_ong.views import showOneNews
from app_saada_ong.views import listagem
from app_saada_ong.views import update
from app_saada_ong.views import remove
from app_saada_ong.views import create
from app_saada_ong.views import cae_login
from app_saada_ong.views import cae_register

# app_neilytaTec1
# app_saada_ong

urlpatterns = [
    # admin route
    path('admin/', admin.site.urls),
    # path('login/', include('admin.site.urls'), name='url__real_login'),


    path('', home, name='url_home'),
    path('listagem/', listagem, name='url_listagem'),
    path('register/', cae_register, name='url_register'),
    path('login2/', cae_login, name='url_login'),
    path('projeto/<int:id_project>/', showProjeto, name='go2thisproject'),
    path('allnoticias/', listAllNews, name='go2allnews'),
    path('noticia/<int:id_news>/', showOneNews, name='go2showonenews'),


    path('create/<int:pk>/', create, name='go2create'),
    path('listar_prof/', listarProf, name='go2listarprof'),
    path('listar_alunos/', listarAlunos, name='go2listaralunos'),
    # path('listar_cursos/', listarCursos, name='go2listarcursos'),
    path('update/<int:code>/<int:pk>/', update, name='url_update'),
    path('remove/<int:code>/<int:pk>/', remove, name='url_remove'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
